#!/usr/bin/env python

def question():
    print("10. 行数のカウント")
    print("行数をカウントせよ．確認にはwcコマンドを用いよ．")

import subprocess
res = subprocess.check_output('cat hightemp.txt | wc -l', shell=True, universal_newlines=True)

def main():
    print(len(open('hightemp.txt').readlines()))
    print(res.strip())

if __name__ == '__main__':
    question()
    main()
