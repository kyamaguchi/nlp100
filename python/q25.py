#!/usr/bin/env python

def question():
    print("25. テンプレートの抽出")
    print("記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．")

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
            buf = l.replace('\n', '')
        else:
            buf += l.replace('\n', '')

# print('\n\n'.join(infolines))

info = collections.OrderedDict()
for l in infolines:
    m = re.match('\|(.*) = (.*)', l)
    if m:
        info[m.group(1)] = m.group(2)

def main():
    for k,v in info.items():
        print('{k} = {v}'.format(k=k, v=v))

if __name__ == '__main__':
    question()
    main()
