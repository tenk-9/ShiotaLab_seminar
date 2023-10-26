# 第3回
- 10/26(木)
- 13:00~
## 内容
- Audacity+PCのマイクで音声をサンプリング周波数16kHzにして撮り直してスペクトログラムを見直す
- 自分のスマホのアプリで音声収録してスペクトログラムを見る（16kHz, 非圧縮）
- 下記論文についてまとめてくる
  - https://www.jstage.jst.go.jp/article/jasj/78/6/78_338/_article/-char/ja/
- 先週の機械学習の部分を読んで見る（まとめなくて良い）
- 評価方法としてEER（等価エラー率）DCF， ROCカーブについて調べる
### サンプリング周波数16kHzで録りなおす
`re_spectrogram_16k/`
![16k](./re_spectrogram_16k/windowFunc_16k.png)
### スマホで音声収録し，スペクトログラムを見る
`handy_record_spectrogram/`
![16k](./handy_record_spectrogram/windowFunc_16k_sp.png)
- パソコンのマイクで録音したものよりノイズが多い
  - 高周波の成分が多い
- 音声を聞いてみると，こっちの方がクリアに聞こえる
  - パソコンの方は若干籠っている
### 「話者認識システムとなりすまし対策」を読み，まとめる
- https://www.jstage.jst.go.jp/article/jasj/78/6/78_338/_article/-char/ja/
- `paper.md`

### 先週の機械学習の部分を読み直す
`paper.md`
### 評価方法について調べる
#### EER
- https://www.mofiria.com/biometrics-and-security-blog/biometrics/biometrics-terminology/
- 等価エラー率
- FARとFRRが一致するように閾値を調整した際のエラー率
  - FAR
    - 他人受け入れ率
    - False Acceptance Rate
    - FP/(TN+TP)
  - FRR
    - 本人拒否率
    - False Rejection Rate
    - FN/(FN+TP)
- 認証技術の精度性能の目安とされることが多い
- 小さいほど精度が高い
#### DCF
- https://ai.stackexchange.com/questions/27936/what-is-the-difference-between-the-equal-error-rate-and-detection-cost-functi
- 偽陽性(False positive)と偽陰性(False negative)に関連するコストを考慮
- 閾値を変化させ，DCFを最小化する
- DCFが最小となる閾値がベスト_?

#### ROC曲線
- 受信者操作特性
- Receiver Oparating Characteristic
- 偽陽性率を横軸に，真陽性率を縦軸にとる
  - 偽陽性率, FPR
    - 間違えて陽性だと判断した割合
    - FalsePositive/Negatives = FP/(FP+TN)
  - 真陽性率, TPR
    - 正しく陽性だと判断できた割合
    - TruePositive/Positives = TP/(TP+FN)
- 閾値を変えると，偽陽性率，真陽性率がかわる
  - 閾値を上げるほどTPR+, FPR-
  - ランダムだと対角線上に収束
  - 良い分類器ほど左上に膨らむ
  - 分類器の理論値は左上張り付き
- Area Under the Curve, AUC: 曲線下面積
  - 膨らみ具合を数値化している
  - 1に近いほどd精度がいい