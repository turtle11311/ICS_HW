#!/usr/bin/python3

import sys

ALPHABET_NUM = 26

line = str(input())

line, k = line.split(sep='$')
k = int(k)

answer = ""

for ch in line:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        offset = ord(ch) - base
        ch = chr(base + (offset + k) % ALPHABET_NUM)
    answer += ch

print(answer)
