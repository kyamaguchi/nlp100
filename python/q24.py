#!/usr/bin/env python

def question():
    print("24. ファイル参照の抽出")
    print("記事から参照されているメディアファイルをすべて抜き出せ．")

import re

filename = 'United_Kingdom.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

    media = []
    for l in lines:
        m = re.search('\[\[(?:ファイル|File):([^]|]+)', l)
        if m:
            media.append(m.group(1))
        m2 = re.search('^ファイル:([^|]+)\|', l)
        if m2:
            media.append(m2.group(1))

def main():
    print('\n'.join(media))

if __name__ == '__main__':
    question()
    main()
