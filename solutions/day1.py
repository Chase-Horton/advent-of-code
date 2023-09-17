#practicing vim and never nesting
import requests
def solve(listString, solutionOne):
    s = 0
    sums = []
    splitList = listString.split('\n')
    for splitItem in splitList:
        if splitItem != '':
            s += int(splitItem)
        else:
            sums.append(s)
            s = 0
        sums.sort()
    if solutionOne:
        m = sums[-1]
        return m
    m = sum(sums[-3:])
    return m
with open('../data/day1.txt') as f:
    validationInput = f.read()
print("Solution 1: ", solve(validationInput, True))
print("Solution 2: ", solve(validationInput, False))
