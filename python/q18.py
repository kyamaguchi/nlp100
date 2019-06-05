#!/usr/bin/env python

def question():
    print("18. 各行を3コラム目の数値の降順にソート")
    print("各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．")

lines = open('hightemp.txt').readlines()
lines.sort(key=lambda x:x.split('\t')[2])

import subprocess
res = subprocess.check_output('sort -n -k 3 hightemp.txt', shell=True, universal_newlines=True)

def main():
    print(''.join(lines), end='')
    print()

    print(res)

if __name__ == '__main__':
    question()
    main()
