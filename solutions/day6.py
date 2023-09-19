#!/usr/bin/env python3
with open('../data/day6.txt') as f:
    data = f.read()
splitStr = data.strip().split('\n')
def getMatches(splitStr, numOfMarkers):
    for line in splitStr:
        testChars = line[:numOfMarkers]
        charSet = set(testChars)
        if len(set(testChars)) == numOfMarkers:
                return numOfMarkers
        i = numOfMarkers + 1
        for char in line[numOfMarkers:]:
            testChars = testChars[1:]
            testChars += char
            if len(set(testChars)) == numOfMarkers:
                return i
            i += 1
    return outputs
print('Solution 1:', getMatches(splitStr, 4))
print('Solution 2:', getMatches(splitStr, 14))
