#!/usr/bin/env python

def question():
    print("19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる")
    print("各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．")

lines = open('hightemp.txt').readlines()
words = [x.split('\t')[0] for x in lines]

counts = {}
for x in words:
    if x in counts.keys():
        counts[x] += 1
    else:
        counts[x] = 1

import subprocess
res = subprocess.check_output('cut -f 1 hightemp.txt | sort | uniq -c | sort -r -n -k 1', shell=True, universal_newlines=True)

def main():
    for k, v in sorted(counts.items(), key=lambda x: [x[1], x[0]], reverse=True):
        print(v, k)
    print()

    print(res)

if __name__ == '__main__':
    question()
    main()
