#!/usr/bin/env python

print("31. 動詞")
print("動詞の表層形をすべて抽出せよ．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')

items = set()
for group in groups:
    for e in group:
        if e['pos'] == '動詞':
            items.add(e['surface'])

print(sorted(list(items)))
print(len(items))
