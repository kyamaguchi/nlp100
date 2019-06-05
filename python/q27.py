#!/usr/bin/env python

print("27. 内部リンクの除去")
print("26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．")

import re
import collections

filename = 'United_Kingdom.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

    infolines = []
    buf = ""
    for l in lines:
        if re.match('}}', l):
            infolines.append(buf)
            break
        if re.match('\|', l):
            infolines.append(buf)
            buf = l.replace("'''", '').replace("[[", '').replace("]]", '').replace('\n', '')
        else:
            buf += l.replace("'''", '').replace("[[", '').replace("]]", '').replace('\n', '')

info = collections.OrderedDict()
for l in infolines:
    m = re.match('\|(.*) = (.*)', l)
    if m:
        info[m.group(1)] = m.group(2)

for k,v in info.items():
    print('{k} = {v}'.format(k=k, v=v))
