# 第3回
- 11/13(月)
- 14:40~
## 内容
- ECAPA-TDNNでの話者照合
- https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb
### 音声データ
- ymgt, shina, yskwの3人の音声を用意した．
- 各人について，4つの発話を録音した．
  - 16000Hz, 320kbps
  - 名前の名乗り: ○○です
  - 好きな単語3つ
### プログラム
- colab上で実行した．
  - https://drive.google.com/file/d/18bvohFgvplbQDs1z7Ytxsn-vDY03Qxm4/view?usp=sharing
- `src/list.txt`
  - 二つの音声ファイル組について，以下を` `区切りで列挙
    - 同一話者であるか否か(1: same, 0: diff)
    - 1つ目のwavファイルパス
    - 2つ目のwavファイルパス
  - https://chat.openai.com/share/6204bcba-a9ea-404c-b13d-4bf00497482e