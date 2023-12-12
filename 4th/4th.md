# 第4回
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
- `src/`
  - ソースコード．
  - `6p4s/`
    - 6人，各4発話
    - AR会メンバー6人
  - `10p2s/`
    - 10人，各2発話
    - ゼミメンバー and AR会メンバー
  - `5p2s/`
    - 5人，各2発話
    - ゼミメンバー
- `../../../_data/wav/`
  - 音声ファイル群．
  - AR会メンバーには4発話してもらった．
    - 自分の名前
    - 任意のフレーズ * 3
  - .gitignore'd
    - AR会メンバーの発話のうち，名前を名乗る音声
    - ゼミメンバーの発話
- EER
  - 今回は丁度交点だったが，閾値は離散的に変化するので，交点でないときは関数的に求める

- next
  - 全部の音声でもう一度やってみる
  - 全ペア数，性別，収録環境等，詳細な情報も併記する
  - 音声にノイズを載せて，変化を見る．
  - マスクあり，無しで音声を録音，スコアの変化をみる
  - 自分の設定した条件と考察を書いてくる
  - 