#!/usr/bin/env python

print("40. 係り受け解析結果の読み込み（形態素）")
print("形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．")

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self) -> str: return 'surface: {}, base: {}, pos: {}, pos1: {}'.format(self.surface, self.base, self.pos, self.pos1)

groups = []
group = []

for line in open('neko.txt.cabocha').readlines():
    if line.startswith('*'):
        continue

    if line.startswith('EOS'):
        if len(group) > 0:
            groups.append(group)
            group = []
        continue

    parts = line.split('\t')
    parts2 = parts[1].split(',')

    morph = Morph(surface=parts[0], base=parts2[6], pos=parts2[0], pos1=parts2[1])
    group.append(morph)

for morph in groups[2]:
    print(str(morph))
