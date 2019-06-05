#!/usr/bin/env python

def question():
    print("36. 単語の出現頻度")
    print("文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')
counts = common.word_counts(groups)

from collections import Counter
word_counter = Counter()
for group in groups:
    word_counter.update([e['surface'] for e in group])

# 出現頻度順のリストを取得
list_word = word_counter.most_common()

def main():
    for k, v in sorted(counts.items(), key=lambda x: [x[1], x[0]], reverse=True):
        print(v, k)

    print(list_word)

if __name__ == '__main__':
    question()
    main()

