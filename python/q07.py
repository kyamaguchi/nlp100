#!/usr/bin/env python

def question():
    print("07. テンプレートによる文生成")
    print("引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=\"気温\", z=22.4として，実行結果を確認せよ．")

def xyz(x, y, z):
    return str(x) + "時の" + str(y) + "は" + str(z)

def format_string(x, y, z):
    return '{hour}時の{target}は{value}'.format(hour=x, target=y, value=z)

def main():
    print(xyz(12, "気温", 22.4))
    print(format_string(12, '気温', 22.4))

if __name__ == '__main__':
    question()
    main()
