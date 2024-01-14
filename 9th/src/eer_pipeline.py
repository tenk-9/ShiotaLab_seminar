from speechbrain.pretrained import SpeakerRecognition
from typing import List
from scipy.interpolate import interp1d
from scipy.optimize import brentq
from sklearn.metrics import roc_curve ,auc
import matplotlib.pyplot as plt
from tqdm import tqdm
import re
import shutil
import os

verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec-ecapa-voxceleb",
    run_opts={"device":"cuda"},
    )

#EERを求める関数
#FRR=1-TPRであることに留意
def compute_eer(labels: List[int], scores: List[float]):
    fpr, tpr, thresholds = roc_curve(labels, scores, pos_label=1)
    eer = brentq(lambda x: 1.0 - x - interp1d(fpr, tpr)(x), 0.0, 1.0)
    eer_threshold = interp1d(fpr, thresholds)(eer)
    return fpr, tpr, thresholds, eer, eer_threshold

def parse_listfile(wav_list_path):
  labels = []
  wav1 = []
  wav2 = []

  with open(wav_list_path) as f:
    for line in f:
      line = line.rstrip().split(' ')
      labels.append(int(line[0]))
      wav1.append(line[1])
      wav2.append(line[2])
  return labels, wav1, wav2

def gen_audio_cache_filename(wav_path: str) -> str:
  result = re.match(r".*/(.+?)/(.+)/(.+?)\.wav", wav_path)
  spk, cond, wavname = result.groups()
  return f"{spk}-{cond}-{wavname}"

def calc_scores(labels: List[int], wav1: List[str], wav2: List[str]) -> List[float]:
  scores = []
  for i in tqdm(range(len(labels))):
###
    waveform_x = verification.load_audio(
        wav1[i],
        save_filename=gen_audio_cache_filename(wav1[i])
        )
    waveform_y = verification.load_audio(
        wav2[i],
        save_filename=gen_audio_cache_filename(wav2[i])
        )
    # Fake batches:
    batch_x = waveform_x.unsqueeze(0)
    batch_y = waveform_y.unsqueeze(0)
    # Verify:
    score, decision = verification.verify_batch(batch_x, batch_y)
    # Squeeze:
    score, prediction = score[0], decision[0]
###
    scores.append(score.item())
  return scores

def eer_roc_pipeline(wav_list_path: str, save_dir_root: str):
  # 音声対が列挙されたファイルを，ラベル，音声1，音声2のリストに分割
  labels, wav1, wav2 = parse_listfile(wav_list_path)
  # 音声ファイル対について，スコアを計測
  scores = calc_scores(labels, wav1, wav2)
  # 評価値を計算
  fpr, tpr, th, eer, eer_th = compute_eer(labels, scores)

  #FAR,FRR,EERの図のプロット
  title = re.match(r".*/(.+).txt", wav_list_path).group(1)
  os.makedirs(f"{save_dir_root}/fig/{title}", exist_ok=True)
  
  plt.figure()
  plt.plot(th, fpr, marker='o', markersize=1, label="FAR")
  plt.plot(th, 1-tpr, marker='o', markersize=1, label="FRR")
  plt.plot(eer_th,eer,marker='*', markersize=10, color="red")
  plt.xlabel('Threshold')
  plt.ylabel('Error Rate')
  plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0, fontsize=10)
  plt.title(f"Error Rate Curve: {title}, EER: {eer:.5f}")
  plt.grid()
  plt.savefig(f"{save_dir_root}/fig/{title}/eer", bbox_inches='tight', dpi=600)

  # scoreの箱ひげ図をプロット
  true_pair_scores: List[float] = []
  false_pair_scores: List[float] = []
  for idx, score in enumerate(scores):
    if labels[idx] == 1:
      true_pair_scores.append(score)
    else:
      false_pair_scores.append(score)
  # plot
  plt.figure()
  plt.boxplot(
      [true_pair_scores, false_pair_scores],
      labels = ["true-pairs", "false-pairs"],
  )
  plt.title(f"Boxplot of Scores for Each Labels")
  plt.hlines(eer_th, 0.8, 2.2)
  plt.ylim(-0.3, 0.8)
  plt.grid()
  plt.savefig(f"{save_dir_root}/fig/{title}/box", bbox_inches='tight', dpi=600)

  # 詳細を出力
  print(f"wav_list:{wav_list_path}")
  print(f"pairs:{len(labels)}")
  # print("fpr:", fpr)
  # print("tpr:", tpr)
  # print("roc_th:", th)
  print("eer:", eer)
  print("eer_th:", eer_th)


  # pcのtrue_pairのscoreが全体的に低い気がするので，trueでscore < eer_thの対を出力してみる．
  print(f"FalseNegatives(eer_th:{eer_th})")
  for idx, score in enumerate(scores):
    if score < eer_th and labels[idx] == 1:
      print(f"score:{score} {wav1[idx]}, {wav2[idx]}")
  
  shutil.rmtree("/content/audio_cache/")