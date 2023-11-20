import os

DIR = os.path.dirname(__file__)
# speakers = ["ayu", "ktg", "shina", "tani",
#             "yskw", "abe", "hre", "mrym", "tmng", "ymgt"]

speakers = ["ayu", "ktg", "shina", "tani",
            "yskw", "hre", "mrym", "tmng", "ymgt"]
# thx shinboon_
with open(f"{DIR}/list.txt", "w") as file:
    for A_idx in range(len(speakers)):
        same = 1
        pair_str = f"{same} ../../../_data/wav/{speakers[A_idx]}/1.wav ../../../_data/wav/{speakers[A_idx]}/2.wav"
        file.write(pair_str+'\n')
    for A_idx in range(len(speakers)):
        for B_idx in range(A_idx + 1, len(speakers)):
            for wav_a in [1,2]:
                for wav_b in [1,2]:
                    same = 0
                    pair_str = f"{same} ../../../_data/wav/{speakers[A_idx]}/{wav_a}.wav ../../../_data/wav/{speakers[B_idx]}/{wav_b}.wav"
                    file.write(pair_str+'\n')
