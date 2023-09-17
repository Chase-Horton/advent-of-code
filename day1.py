import requests
def solve(listString):
    s = 0
    sums = []
    splitList = listString.split('\n')
    for splitItem in splitList:
        if splitItem != '':
            s += int(splitItem)
        else:
            sums.append(s)
            s = 0
    m = max(sums)
    return m, sums.index(m)
f = open('day1.txt')
validationInput = f.read()
f.close()
if (validationInput):
    print(solve(validationInput))
else:
    print(validationInput)
