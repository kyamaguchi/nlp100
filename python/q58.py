#!/usr/bin/env python

def question():
    print("58. タプルの抽出")
    print("Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．")
    print("述語: nsubj関係とdobj関係の子（dependant）を持つ単語, 主語: 述語からnsubj関係にある子（dependent）, 目的語: 述語からdobj関係にある子（dependent）")

def main():
    pass

if __name__ == '__main__':
    question()
    main()
