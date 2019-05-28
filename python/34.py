#!/usr/bin/env python

print("34. 「AのB」")
print("2つの名詞が「の」で連結されている名詞句を抽出せよ．")

import common
groups = common.extract_groups_from_mecab('neko.txt.mecab')

items = set()
for group in groups:
    for i in range(0, len(group)-2):
        elements = group[i:i+3]
        if elements[1]['surface'] == 'の' and elements[0]['pos'] == '名詞' and elements[2]['pos'] == '名詞':
            items.add(''.join([x['surface'] for x in elements]))

print(sorted(list(items)))
print(len(items))

# print('-----')
# items = set()
# for group in groups:
#     for i in range(0, len(group)-2):
#         elements = group[i:i+3]
#         if elements[1]['surface'] == 'の' and elements[0]['pos'] == '名詞' and elements[2]['pos'] == '名詞' and elements[0]['pos1'] == '一般' and elements[2]['pos1'] == '一般':
#             items.add(''.join([x['surface'] for x in elements]))

# print(sorted(list(items)))
# print(len(items))
