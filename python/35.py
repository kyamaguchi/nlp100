#!/usr/bin/env python

print("35. 名詞の連接")
print("名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')

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
