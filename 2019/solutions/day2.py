#!/usr/bin/env python3
# 1, x, y, z addition, loc 1, loc 2, output loc
# 2 mult

class CPU:
    def __init__(self, tape=None):
        if tape:
            self.tape = tape
        self.i = 0
        self.halt = False
        self.codesDict = {
            1 : self.opAdd,
            2 : self.opMult,
            99: self.opHalt
        }

    def run(self, tape=None):
        if tape:
            self.tape = tape
        self.i = 0
        self.halt = False
        while not self.halt:
            self.evaluateCode()
            if not self.halt:
                pass
                #print(self.tape)
        print('HALTED')
        #print(self.tape)
        return self.tape[0]

    def evaluateCode(self):
        code = self.tape[self.i]
        # do action
        self.codesDict[code]()
        self.i += 4

    def opAdd(self):
        index1, index2, index3 = self.tape[self.i + 1], self.tape[self.i + 2], self.tape[self.i + 3]
        print(f'adding {self.tape[index1]} + {self.tape[index2]}')
        self.tape[index3] = self.tape[index1] + self.tape[index2]

    def opMult(self):
        index1, index2, index3 = self.tape[self.i + 1], self.tape[self.i + 2], self.tape[self.i + 3]
        print(f'mult {self.tape[index1]} * {self.tape[index2]}')
        self.tape[index3] = self.tape[index1] * self.tape[index2]

    def opHalt(self):
        self.halt = True

with open('../data/day2.txt') as f:
    data = [int(d) for d in f.read().strip().split(',')]

intCoder = CPU()
intCoder.run(data.copy())
print('Solution 1:', intCoder.tape[0])

out = 0
foundAnswer = False
for x in range(100):
    for y in range(100):
        newData = data.copy()
        newData[1] = x
        newData[2] = y
        out = intCoder.run(newData)
        print(out)
        if out == 19690720:
            foundAnswer = [x, y]
            break
    if foundAnswer:
        break
print('Solution 2:', foundAnswer[0] * 100 + foundAnswer[1])
