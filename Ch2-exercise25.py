#!/usr/bin/python3
import sys

numList = []


def adjacent_equal(container):
    for i in range(0, len(container) - 1):
        if container[i] == container[i + 1]:
            return True

    return False

stopFlag = False
for line in sys.stdin:
    for elem in line.split():
        elem = int(elem)
        if elem == -1:
            stopFlag = True
            break
        numList.append(elem)
    if stopFlag:
        break

if adjacent_equal(numList):
    print("Yes")
else:
    print("No")
