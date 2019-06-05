#!/usr/bin/env python

def question():
    print("39. Zipfの法則")
    print("単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')
counts = common.word_counts(groups)

# print(counts)
freq = list(counts.values())
freq.sort(reverse=True)

freq_rank = []
for v in freq:
    freq_rank.append(freq.index(v)+1)

# print(list(zip(freq, freq_rank)))
import matplotlib.pyplot as plt

def main():
    plt.plot(freq_rank, freq)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

if __name__ == '__main__':
    question()
    main()

