#!/usr/bin/env python

print("15. 末尾のN行を出力")
print("自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．")

n = input('please type a positive number: ')

for line in open('hightemp.txt').readlines()[-int(n):]:
    print(line, end='')

print()

import subprocess
res = subprocess.check_output('tail -%s hightemp.txt' %(n), shell=True, universal_newlines=True)
print(res)
