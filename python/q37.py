#!/usr/bin/env python

print("37. 頻度上位10語")
print("出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')
counts = common.word_counts(groups)

top10 = sorted(counts.items(), key=lambda x: [x[1], x[0]], reverse=True)[0:10]

import matplotlib.pyplot as plt

y = [v for k,v in top10]
labels = [k for k,v in top10]
x = range(0, len(labels))
plt.bar(x, y, tick_label=labels)
plt.show()

# for k, v in top10:
#     print(k, v)
