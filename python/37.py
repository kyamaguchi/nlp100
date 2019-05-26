#!/usr/bin/env python

print("37. 頻度上位10語")
print("出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．")

groups = []
group = []

for line in open('neko.txt.mecab').readlines():
    if line.startswith('EOS'):
        if len(group) > 0:
            groups.append(group)
            group = []
        continue

    elm = {}
    parts = line.split('\t')
    elm['surface'] = parts[0]
    parts2 = parts[1].split(',')
    elm['pos'] = parts2[0]
    elm['pos1'] = parts2[1]
    if len(parts2) == 9:
        elm['base'] = parts2[6]
    group.append(elm)

counts = {}
for group in groups:
    for e in group:
        x = e['surface']
        if x in counts.keys():
            counts[x] += 1
        else:
            counts[x] = 1

top10 = sorted(counts.items(), key=lambda x: [x[1], x[0]], reverse=True)[0:10]

import matplotlib.pyplot as plt

y = [v for k,v in top10]
labels = [k for k,v in top10]
x = range(0, len(labels))
plt.bar(x, y, tick_label=labels)
plt.show()

# for k, v in top10:
#     print(k, v)
