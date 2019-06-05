#!/usr/bin/env python

print("33. サ変名詞")
print("サ変接続の名詞をすべて抽出せよ．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')

items = set()
for group in groups:
    for e in group:
        if e['pos1'] == 'サ変接続':
            items.add(e['surface'])

print(sorted(list(items)))
print(len(items))
