#!/usr/bin/env python

print("38. ヒストグラム")
print("単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')
counts = common.word_counts(groups)

freq = list(counts.values())
freq.sort(reverse=True)

import matplotlib.pyplot as plt

plt.hist(freq, bins=50, range=(0, 50))
plt.show()
