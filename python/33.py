#!/usr/bin/env python

print("33. サ変名詞")
print("サ変接続の名詞をすべて抽出せよ．")

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
    for e in group:
        if e['pos1'] == 'サ変接続':
            items.add(e['surface'])

print(sorted(list(items)))
print(len(items))
