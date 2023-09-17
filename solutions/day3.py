def getCode(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    return ord(char) - ord('A') + 27

def splitList(lst):
    midPoint = len(lst) // 2
    return set(lst[:midPoint]), set(lst[midPoint:])

def findMatchingCharCode(line):
    set1, set2 = splitList(line)
    char = next(iter(set1.intersection(set2)))
    return getCode(char)
def findMatchingTriplet(l):
    s1, s2, s3 = set(l[0]), set(l[1]), set(l[2])
    commonSet = s1 & s2 & s3
    char = next(iter(commonSet))
    return getCode(char)
# solution 1
with open('../data/day3.txt') as f:
    data = f.read()
codeSum = 0
for line in data.strip().split('\n'):
    codeSum += findMatchingCharCode(line)
print('Solution 1:', codeSum)

# solution 2
codeSum = 0
lines = data.strip().split('\n')
i = 0
for i in range(0, len(lines), 3):
    l = lines[i:i+3]
    codeSum += findMatchingTriplet(l)
print('Solution 2:', codeSum)
