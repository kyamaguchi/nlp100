#!/usr/bin/env python

print("21. カテゴリ名を含む行を抽出")
print("記事中でカテゴリ名を宣言している行を抽出せよ．")

import json
import re
import pprint

filename = 'United_Kingdom_raw.json'

with open(filename, 'r') as f:
    json = json.load(f)
    lines = list(json['query']['pages'].values())[0]['revisions'][0]['*'].split('\n')
    # pprint.pprint(lines)
    # print(len(lines))

    categories = [l for l in lines if re.search('\[\[Category', l)]
    print(categories)
