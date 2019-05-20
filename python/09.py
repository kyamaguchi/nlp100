#!/usr/bin/env python

print("09. Typoglycemia")
print("スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば\"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .\"）を与え，その実行結果を確認せよ．")

import random

def convert(message):
    new_words = []
    words = message.split()
    for word in words:
        if len(word) <= 4:
            new_words.append(word)
        else:
            randomized = random.sample([char for char in word[1:-1]], len(word[1:-1]))
            new_words.append(word[0] + ''.join(randomized) + word[-1])
    return ' '.join(new_words)

message = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(convert(message))

def convert2(message):
    new_words = []
    words = message.split()
    for word in words:
        if len(word) <= 4:
            new_words.append(word)
        else:
            chr_list = list(word[1:-1])
            random.shuffle(chr_list)
            new_words.append(word[0] + ''.join(chr_list) + word[-1])
    return ' '.join(new_words)

message = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(convert2(message))
