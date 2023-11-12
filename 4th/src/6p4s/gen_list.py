import os

DIR = os.path.dirname(__file__)
speakers = ["ayu", "ktg", "shina", "tani", "ymgt", "yskw"]

# thx shinboon_
with open(f"{DIR}/list.txt", "w") as file:
    for A_idx in range(len(speakers)):
        same = 1
        for wav_a in range(4):
            for wav_b in range(wav_a+1, 4):
                pair_str = f"{same} ../../wav/{speakers[A_idx]}/{wav_a}.wav ../../wav/{speakers[A_idx]}/{wav_b}.wav"
                file.write(pair_str+'\n')
    for A_idx in range(len(speakers)):
        for B_idx in range(A_idx + 1, len(speakers)):
            for wav_a in range(4):
                for wav_b in range(4):
                    same = 0
                    pair_str = f"{same} ../../wav/{speakers[A_idx]}/{wav_a}.wav ../../wav/{speakers[B_idx]}/{wav_b}.wav"
                    file.write(pair_str+'\n')
