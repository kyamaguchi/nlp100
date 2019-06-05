#!/usr/bin/env python

def question():
    print("05. n-gram")
    print("与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，\"I am an NLPer\"という文から単語bi-gram，文字bi-gramを得よ．")

def ngram(n, lst):
    result = []
    for i in range(len(lst) - n + 1):
        result.append(lst[i:i+n])
    return result

sentence = "I am an NLPer"
words = sentence.split()

def main():
    print(ngram(2, words))
    print(ngram(2, sentence))

if __name__ == '__main__':
    question()
    main()
