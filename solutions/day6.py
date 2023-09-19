#!/usr/bin/env python3
with open('../data/day6.txt') as f:
    data = f.read()
splitStr = data.strip().split('\n')
print(splitStr)
def getMatches(splitStr):
    for line in splitStr:
        testChars = line[:4]
        charSet = set(testChars)
        print(charSet)
        if len(set(testChars)) == 4:
                return 4
        i = 5
        for char in line[4:]:
            print(testChars)
            testChars = testChars[1:]
            print(testChars)
            testChars += char
            print(testChars)
            if len(set(testChars)) == 4:
                return i
            i += 1
    return outputs
print(getMatches(splitStr))
