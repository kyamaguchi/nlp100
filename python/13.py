#!/usr/bin/env python

print("13. col1.txtとcol2.txtをマージ")
print("12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．")

fname = 'hightemp.txt'
with open('cols.txt', mode='w') as cols_file, \
        open('col1.txt') as col1_file, \
        open('col2.txt') as col2_file:
    for line in zip(col1_file.readlines(), col2_file.readlines()):
        cols_file.write('\t'.join([x.rstrip() for x in line]) + '\n')

print(open('cols.txt').read())

import subprocess
res = subprocess.check_output("paste col1.txt col2.txt", shell=True, universal_newlines=True)
print(res)
