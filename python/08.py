#!/usr/bin/env python

print("08. 暗号文")
print("与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．")
print("英小文字ならば(219 - 文字コード)の文字に置換, その他の文字はそのまま出力")
print("この関数を用い，英語のメッセージを暗号化・復号化せよ．")

def cipher(message):
    result = ""
    for ch in message:
        if ch.islower():
            result += chr(219 - ord(ch))
        else:
            result += ch
    return result

message = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(cipher(message))
print(cipher(cipher(message)))

message2 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(cipher(message2))
print(cipher(cipher(message2)))
