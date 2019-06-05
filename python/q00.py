#!/usr/bin/env python

def question():
    print("00. 文字列の逆順")
    print("文字列\"stressed\"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．")

def main():
    string = "stressed"
    print(string[::-1])

if __name__ == '__main__':
    question()
    main()
