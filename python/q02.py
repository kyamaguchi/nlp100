#!/usr/bin/env python

def question():
    print("02. 「パトカー」＋「タクシー」＝「パタトクカシーー」")
    print("「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．")

def main():
    str1 = "パトカー"
    str2 = "タクシー"
    print(''.join([x[0] + x[1] for x in zip(str1, str2)]))

if __name__ == '__main__':
    question()
    main()
