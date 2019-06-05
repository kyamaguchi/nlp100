#!/usr/bin/env python

def question():
    print("29. 国旗画像のURLを取得する")
    print("テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）")

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

filename = info['国旗画像'].replace(' ', '_')

import urllib.parse

import requests
import json

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(filename) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

res = requests.get(url)
res.raise_for_status()
data = res.json()

def main():
    print("https://ja.wikipedia.org/wiki/ファイル:%s" %(filename))
    print("https://ja.wikipedia.org/wiki/%s:%s" %(urllib.parse.quote('ファイル'), filename))

    print(url)
    print(data['query']['pages']['-1']['imageinfo'][0]['url'])

if __name__ == '__main__':
    question()
    main()
