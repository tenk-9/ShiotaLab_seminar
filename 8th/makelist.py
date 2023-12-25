import os
import itertools

def is_same_speaker(path1, path2):
  # path文字列を解析して，パス対が同じ話者であるかを判定
  name1 = path1.split('/')[-3]
  name2 = path2.split('/')[-3]
  # # re(正規表現)による実装．今回のpathであればsplit('/')でいいが，複雑な区切り文字とかになると正規表現を用いた方が良い場面も出てくる．
  # dir1 = re.match(r"(.*/).+\.wav", path1).group(1)
  # dir2 = re.match(r"(.*/).+\.wav", path2).group(1)
  return int(name1 == name2)

def gen_2pair_listfile(path_list, outfile_path):
  outfile = open(outfile_path, 'w')
  out_info = {
      "filename": outfile_path,
      "total_wavs": len(path_list),
      "total_pairs": len(path_list) * (len(path_list)-1) // 2,
      "same_pair": 0,
      "diff_pair": 0,
  }
  # itertools.combinations()による実装．
  # 組み合わせをforで構築するのは，`CS_seminar/4th/*/gen_list.py`を参照のこと．
  pairs = list(itertools.combinations(path_list, 2))
  for pair in pairs:
    same_spk = is_same_speaker(*pair)
    outstr = f"{same_spk} {pair[0]} {pair[1]}\n"
    outfile.write(outstr)
    # ペア数を記録
    if same_spk:
      out_info["same_pair"] += 1
    else:
      out_info["diff_pair"] += 1
  outfile.close()
  return out_info