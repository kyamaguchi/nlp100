#!/usr/bin/env python

print("02. 「パトカー」＋「タクシー」＝「パタトクカシーー」")
print("「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．")

str1 = "パトカー"
str2 = "タクシー"
print(''.join([x[0] + x[1] for x in zip(str1, str2)]))
