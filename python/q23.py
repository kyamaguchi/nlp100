#!/usr/bin/env python

def question():
    print("23. セクション構造")
    print("記事中に含まれるセクション名とそのレベル（例えば\"== セクション名 ==\"なら1）を表示せよ．")

import re

filename = 'United_Kingdom.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

    levels = []
    for l in lines:
        m = re.match('(=+)([^=]+)=', l)
        if m:
            levels.append((m.group(2), len(m.group(1))-1))

def main():
    [print(x) for x in levels]

if __name__ == '__main__':
    question()
    main()
