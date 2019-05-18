#!/usr/bin/env python

print("03. 円周率")
print("\"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.\"という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．")

import re
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = re.sub('[,.]', '', sentence).split()
print(list(map(len, words)))
