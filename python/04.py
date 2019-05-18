#!/usr/bin/env python

print("04. 元素記号")
print("\"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.\"という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．")

import re
sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = re.sub('[,.]', '', sentence).split()
indexes = [1, 5, 6, 7, 8, 9, 15, 16, 19]

result = []
for i in range(len(words)):
    word = words[i]
    if i+1 in indexes:
        result.append((word[0:1], i+1))
    else:
        result.append((word[0:2], i+1))

print(result)


result2 = {}
for i in range(len(words)):
    word = words[i]
    if i+1 in indexes:
        result2[word[0:1]] = i+1
    else:
        result2[word[0:2]] = i+1

print(result2)
