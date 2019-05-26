#!/usr/bin/env python

print("35. 名詞の連接")
print("名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．")

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

items = set()
for group in groups:
    nouns = []
    for e in group:
        if e['pos'] == '名詞':
            nouns.append(e['surface'])
        else:
            if len(nouns) >= 2:
                items.add(''.join(nouns))
            nouns = []

print(sorted(list(items)))
print(len(items))
