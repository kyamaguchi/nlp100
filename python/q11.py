#!/usr/bin/env python

print("11. タブをスペースに置換")
print("タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．")

print(open('hightemp.txt').read().replace("\t", " "))

import subprocess
res = subprocess.check_output("cat hightemp.txt | tr '\t' ' ' ", shell=True, universal_newlines=True)
print(res)
