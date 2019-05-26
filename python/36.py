#!/usr/bin/env python

print("36. 単語の出現頻度")
print("文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．")

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

for k, v in sorted(counts.items(), key=lambda x: [x[1], x[0]], reverse=True):
    print(v, k)


from collections import Counter
word_counter = Counter()
for group in groups:
    word_counter.update([e['surface'] for e in group])

# 出現頻度順のリストを取得
list_word = word_counter.most_common()
print(list_word)
