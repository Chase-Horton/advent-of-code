#!/usr/bin/env python3
def checkPass(pwd):
    #for i in range(136760, 595730+1):
    #for i in range(136799, 136800):
    hasRepeat = False
    ascending = True
    strNum = str(pwd)
    highest = int(strNum[0])
    last = None
    for char in strNum:
        if int(char) < int(highest):
            ascending = False
            break
        elif int(char) > int(highest):
            highest = char
        if last == char:
            hasRepeat = True
        last = char
    if hasRepeat and ascending:
        return 1
    else:
        return 0

print('Solution 1:', sum([checkPass(x) for x in range(136760, 595730+1)]))
