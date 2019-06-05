#!/usr/bin/env python

def question():
    print("11. タブをスペースに置換")
    print("タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．")

import subprocess
res = subprocess.check_output("cat hightemp.txt | tr '\t' ' ' ", shell=True, universal_newlines=True)

def main():
    print(open('hightemp.txt').read().replace("\t", " "))
    print(res)

if __name__ == '__main__':
    question()
    main()
