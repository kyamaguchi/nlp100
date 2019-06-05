#!/usr/bin/env python

print("22. カテゴリ名の抽出")
print("記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．")

import re

filename = 'United_Kingdom.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

    categories = []
    for l in lines:
        m = re.search('\[\[Category:([^]|]+)', l)
        if m:
            categories.append(m.group(1))
    print('\n'.join(categories))
