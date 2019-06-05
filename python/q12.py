#!/usr/bin/env python

def question():
    print("12. 1列目をcol1.txtに，2列目をcol2.txtに保存")
    print("各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．")

col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')

for line in open('hightemp.txt').readlines():
    cells = line.split("\t")
    col1.write(cells[0] + "\n")
    col2.write(cells[1] + "\n")

col1.close()
col2.close()

import subprocess
res1 = subprocess.check_output("cut -f 1 hightemp.txt", shell=True, universal_newlines=True)
res2 = subprocess.check_output("cut -f 2 hightemp.txt", shell=True, universal_newlines=True)

def main():
    print(open('col1.txt').read())
    print(open('col2.txt').read())
    print(res1)
    print(res2)

if __name__ == '__main__':
    question()
    main()
