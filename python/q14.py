#!/usr/bin/env python

def question():
    print("14. 先頭からN行を出力")
    print("自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．")

n = input('please type a positive number: ')

import subprocess
res = subprocess.check_output('head -%s hightemp.txt' %(n), shell=True, universal_newlines=True)

def main():
    for line in open('hightemp.txt').readlines()[:int(n)]:
        print(line, end='')
    print()

    print(res)

if __name__ == '__main__':
    question()
    main()
