# 山口が用意したファイルの情報
- `../data/wav/`
- 7人分の発話
  - ayu, ktg, shina, tani, ymgt, yskw, ntm
- マスクor録音機械の条件につき，名乗り(`*/0*.wav`)と任意の3発話，計4発話
  - マスクの有無で発話内容は異なる．
  - `_sp` or `_pc`で発話内容は異なる．
  - ayu, shina, yskw
    - マスク無し
      - ノイズ無し\*3 + ノイズあり\*3
    - マスク有り
      - None
  - tani, ntm
    - マスク無し
      - ノイズ無し\*3 + ノイズあり\*3
    - マスク有り
      - ノイズ無し\*3 + ノイズあり\*3
  - ktg
    - マスク無し
      - ノイズ無し\*6 + ノイズあり\*6
    - マスク有り
      - None
  - ymgt
    - マスク無し
      - ノイズ無し\*8 + ノイズあり\*8
    - マスク有り
      - ノイズ無し\*8 + ノイズあり\*8
- 合計発話数
  - 6\*3 + 12\*2 + 12 + 32 = 86
- 組み合わせ総数
  - 86C2=3655通り
- 録音環境等
  - `__`
    - ノイズ無し，マスク無し
  - `_n`
    - ノイズあり，マスク無し
  - `m_`
    - ノイズ無し，マスク有り
  - `mn`
    - ノイズあり，マスク有り
  - 他の要素はファイル名の末尾に'_'で追記表現．
    - *_sp
      - スマートフォンのマイク
      - 16khz
      - 320kbps
    - *_pc
      - ノートパソコンのマイク
      - 16khz
      - 320kbps
    - *_{char}
      - 録音環境コード，英単文字
      - 録音環境は3種類
        - a(部室)
        - b(会議室)
        - c(和室)