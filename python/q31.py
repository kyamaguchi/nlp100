#!/usr/bin/env python

def question():
    print("31. 動詞")
    print("動詞の表層形をすべて抽出せよ．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')

items = set()
for group in groups:
    for e in group:
        if e['pos'] == '動詞':
            items.add(e['surface'])

def main():
    print(sorted(list(items)))
    print(len(items))

if __name__ == '__main__':
    question()
    main()
