#!/usr/bin/env python

print("10. 行数のカウント")
print("行数をカウントせよ．確認にはwcコマンドを用いよ．")

print(len(open('hightemp.txt').readlines()))

import subprocess
res = subprocess.check_output('cat hightemp.txt | wc -l', shell=True, universal_newlines=True)
print(res.strip())
