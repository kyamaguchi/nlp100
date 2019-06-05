#!/usr/bin/env python

def question():
    print("17. １列目の文字列の異なり")
    print("1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．")

words = set([])
for line in open('hightemp.txt').readlines():
    words.add(line.split('\t')[0])
# print(words)

lst = list(words)
lst.sort()
# print('\n'.join(sorted(words)))

import subprocess
res = subprocess.check_output('cut -f 1 hightemp.txt | sort | uniq', shell=True, universal_newlines=True)

def main():
    print('\n'.join(lst))
    print()

    print(res)

if __name__ == '__main__':
    question()
    main()
