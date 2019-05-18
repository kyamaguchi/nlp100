#!/usr/bin/env python

print("06. 集合")
print("\"paraparaparadise\"と\"paragraph\"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．")

def ngram(n, lst):
    result = []
    for i in range(len(lst) - n + 1):
        result.append(lst[i:i+n])
    return result

X = set(ngram(2, "paraparaparadise"))
Y = set(ngram(2, "paragraph"))

print("X: " + str(X))
print("Y: " + str(Y))

print("和集合: " + str(X | Y))
print("積集合: " + str(X & Y))
print("差集合: " + str(X - Y))

print("'se' in X ? " + str('se' in X))
print("'se' in Y ? " + str('se' in Y))
