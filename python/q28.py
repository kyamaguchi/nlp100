#!/usr/bin/env python

def question():
    print("28. MediaWikiマークアップの除去")
    print("27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．")

import re
import collections

def remove_markup(line):
    tmp = line.replace("'''", '').replace("[[", '').replace("]]", '').replace('\n', '')
    tmp2 = re.sub('<.*?>', ' ', tmp)
    tmp3 = re.sub('\[http.*\]', '', tmp2)
    return re.sub(r'{{lang\|[^\|]+\|(.*?)}}', r'\1', tmp3)

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
            buf = remove_markup(l)
        else:
            buf += remove_markup(l)

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
