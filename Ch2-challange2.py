#!/usr/bin/python3

numList = [int(x) for x in input().split()]

for i in range(0, len(numList)):
    maxPos = i
    for j in range(i, len(numList)):
        if numList[maxPos] < numList[j]:
            maxPos = j
    numList[i], numList[maxPos] = numList[maxPos], numList[i]

print(numList)
