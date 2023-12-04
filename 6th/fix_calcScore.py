"""
先輩が共有してくれた.ipynbのうち，スコアを計算するセルのコードを置き換えてください．
そうすれば，多分キャッシュの名前衝突が解消される…はず…

スコアを計算するセル↓
scores = []
for i in range(len(labels)):
    score, prediction = verification.verify_files(wav1[i], wav2[i])
    scores.append(score.item())
print(scores)
"""

# 以下に置き換えてください
import re

def gen_audio_cache_filename(wav_path):
    result = re.match(r".*/(.+?)/([_mn]+)/(.+?)\.wav", wav_path)
    spk, cond, wavname = result.groups()
    return f"{spk}-{cond}-{wavname}"


scores = []
for i in range(len(labels)):
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

print(scores)
