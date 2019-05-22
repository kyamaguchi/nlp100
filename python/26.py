#!/usr/bin/env python

print("26. 強調マークアップの除去")
print("25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．")

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
            buf = l.replace("'''", '').replace('\n', '')
        else:
            buf += l.replace("'''", '').replace('\n', '')

# print('\n\n'.join(infolines))

info = collections.OrderedDict()
for l in infolines:
    m = re.match('\|(.*) = (.*)', l)
    if m:
        info[m.group(1)] = m.group(2)

for k,v in info.items():
    print('{k} = {v}'.format(k=k, v=v))
