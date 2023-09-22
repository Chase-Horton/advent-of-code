#!/usr/bin/env python3
with open('../data/day1.txt') as d:
    # solution 1
    data = d.read()
    print(sum([1 if i =='(' else -1 for i in data]))
    # solution 2
    f = 0
    for i, c in enumerate(data):
        if c == '(':
            f += 1
        else:
            f -= 1
        if f == -1:
            print(i)
            break
