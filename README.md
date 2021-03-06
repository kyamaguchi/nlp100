# NLP 100 practice

## Question

### Source

http://www.cl.ecei.tohoku.ac.jp/nlp100/

#### Data

##### 第2章: UNIXコマンドの基礎 (10〜)

hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．

##### 第3章: 正規表現 (20〜)

Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．

1行に1記事の情報がJSON形式で格納される
各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
ファイル全体はgzipで圧縮される

##### 第4章: 形態素解析 (30〜)

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

```
mecab neko.txt -o neko.txt.mecab
```

##### 第5章: 係り受け解析 (40〜)

夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

```
cabocha -f1 neko.txt -o neko.txt.cabocha
```

### Sample answers

https://qiita.com/search?sort=rel&q=tag%3Apython+100%E6%9C%AC%E3%83%8E%E3%83%83%E3%82%AF
https://qiita.com/segavvy/items/fb50ba8097d59475f760
https://qiita.com/ikura1/items/e98c769b43f56d0f2f85
https://qiita.com/masassy/items/b969bc065888ee6f469f

## Development

### Generate scaffold of script files

```
generate_files.py
```

### Run all script

```
cd python

for f in *.py; do
  python "$f"
done
```

## Note

### Environment

Python 3.5.4
Anaconda 4.1.0 (x86_64)
