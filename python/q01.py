#!/usr/bin/env python

def question():
    print("01. 「パタトクカシーー」")
    print("「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．")

def main():
    string = "パタトクカシーー"
    print(string[::2])

if __name__ == '__main__':
    question()
    main()
