#!/usr/bin/env python

def question():
    print("21. カテゴリ名を含む行を抽出")
    print("記事中でカテゴリ名を宣言している行を抽出せよ．")

import json
import re
import pprint

filename = 'United_Kingdom.txt'

def main():
    with open(filename, 'r') as f:
        lines = f.readlines()
        # pprint.pprint(lines)
        # print(len(lines))

        categories = [l for l in lines if re.search('\[\[Category', l)]
        print(''.join(categories))

if __name__ == '__main__':
    question()
    main()
