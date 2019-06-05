#!/usr/bin/env python

print("16. ファイルをN分割する")
print("自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．")

import subprocess

n = int(input('please type a positive number: '))
subprocess.check_output('rm -rf py_hightemp*', shell=True)
subprocess.check_output('rm -rf sp_hightemp_*', shell=True)

lines = open('hightemp.txt').readlines()
groups = [lines[i:i + n] for i in range(0, len(lines), n)]

for i, group in enumerate(groups):
    with open("py_hightemp%s.txt" %(str(i+1).rjust(3, '0')), mode='w') as out_file:
        for line in group:
            out_file.write(line)

res1 = subprocess.check_output('head py_hightemp*', shell=True, universal_newlines=True)
print(res1)

subprocess.check_output('split -a 3 -l %s hightemp.txt sp_hightemp_' %(n), shell=True, universal_newlines=True)
res2 = subprocess.check_output('head sp_hightemp_*', shell=True, universal_newlines=True)
print(res2)
