#!/usr/bin/env python

def question():
    print("20. JSONデータの読み込み")
    print("Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．")

import os
import gzip
import json
fname = 'jawiki-country.json.gz'

text_file_name = 'United_Kingdom.txt'

if not os.path.exists(text_file_name):
    with open(text_file_name, mode='w') as outfile:
        with gzip.open(fname, "rt") as f:
            for line in f:
                data_json = json.loads(line)
                # print(data_json['title'])
                if data_json['title'] == 'イギリス':
                    # print(data_json['text'])
                    outfile.write(data_json['text'])

def main():
    print(open(text_file_name).read())

if __name__ == '__main__':
    question()
    main()

# import os
# import urllib.parse
# import requests
# import json
# import pprint

# title = urllib.parse.quote('イギリス')
# url = "https://ja.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&titles=%s&format=json" %(title)

# filename = 'United_Kingdom_raw.json'

# if not os.path.exists(filename):
#     res = requests.get(url)
#     res.raise_for_status()
#     with open(filename, mode='wb') as outfile:
#         print(res.content)
#         outfile.write(res.content)

# with open(filename, 'r') as f:
#     json = json.load(f)
#     pprint.pprint(json)
