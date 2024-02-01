これから，塩田研究室における情報科学ゼミナールの成果発表を行います．


塩田研究室では，話者照合をテーマとして学習を行いました．
ここでは，話者照合とは何であるかということと，それに関連する基礎知識，行った話者照合の実験について説明します．


まず，話者照合とは，音声の発話者が特定の人物であるか否かを判断することです．
使いどころとしては，電話の音声を用いて本人確認を行ったり，音声鑑定等の科学捜査に用いたりといったことができます．


次に，話者照合の関連知識の一つである短時間フーリエ変換について説明します．
（slide）
短時間フーリエ変換とは，窓関数をシフトしつつ信号の短時間区間を切り出して，フーリエ変換したものです．
この窓関数の種類や形状・シフト量等によって性能が変化するという特徴があります．


次に短時間フーリエ変換の応用例であるスペクトログラムについて節異名します．これです(スペクトログラムを指す)．
これは短時間フーリエ変換の結果のうち，振幅成分のみを抽出したもので，音声信号に含まれる周波数成分の時間変化を可視化することができます．
(slide)
一般的にスペクトログラムの縦軸は周波数を，横軸は時間を表します．
ここに示しているのは短時間フーリエ変換のパラメータの一つであるフレーム長（窓関数の時間方向の幅のことです）を変化させた際の性能の変化を示したものです．
フレーム長を長くすると周波数分解能（縦軸方向の解像度）が高くなる様子が確認できます．


次に話者照合の評価指標の一つである等価エラー率，EERについて説明します．
これは，他人を誤って受け入れてしまう割合と，本人を誤って拒否してしまう割合が等しいときのエラー率のことです．
判定の閾値を変化させると，両者はトレードオフの関係で変化し，両者の値が等しいとき（ここですね）のエラー率がEERです．
一般的にこれが低いほど良いモデルと言えます．


ここからは私たちが行った，話者照合の実験についての概要を説明します．
どのような実験かというと，発話音声の対を用意し，それらが同一話者によるものか否かを判定するものです．
ECAPA-TDNNという最新の深層学習モデルを用いて話者埋め込み（これは話者の特徴を含むベクトルのことですが）これを抽出し，コサイン類似度をもって同一の話者か否かを判定します．

実験では，録音するデバイスの違いや，ホワイトノイズ，音声に含まれる周波数成分のそれぞれについて，どれほど照合制度に影響があるかを調査しました．

実験に用いた音声は自分たちで用意したもので，スマホとパソコンで同時に発話を録音しました．サンプリング周波数は16kHzで，発話内容は任意の単語，発話当たりの長さは1秒ほどです．