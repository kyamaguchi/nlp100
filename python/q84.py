#!/usr/bin/env python

def question():
    print("84. 単語文脈行列の作成")
    print("83の出力を利用し，単語文脈行列\(X\)を作成せよ．ただし，行列\(X\)の各要素\(X_{tc}\)は次のように定義する．")
    print("\(f(t, c) \geq 10\)ならば，\(X_{tc} = {\rm PPMI}(t, c) = \max\{\log \frac{N \times f(t,c)}{f(t,*) \times f(*,c)}, 0\}\), \(f(t, c) < 10\)ならば，\(X_{tc} = 0\)")
    print("ここで，\({\rm PPMI}(t, c)\)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．なお，行列\(X\)の行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．幸い，行列\(X\)のほとんどの要素は\(0\)になるので，非\(0\)の要素だけを書き出せばよい．")

def main():
    pass

if __name__ == '__main__':
    question()
    main()
