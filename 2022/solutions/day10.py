#!/usr/bin/env python3
import os
from time import sleep
with open('../data/day10.txt') as f:
    data = f.read().strip()
class VM:
    def __init__(self, words, verbose = False, pretty = False):
        self.clock = 0
        self.CRT = ''
        self.words = words
        self.reg = 1
        self.s = 0
        self.verbose = verbose
        self.pretty = pretty
    def getCRT(self):
        return self.clock - 1
    def startCycle(self):
        self.clock += 1
        if self.verbose:
            print(f'start cycle {self.clock}')
    def endCycle(self, word):
        if word != 'noop' and word != 'addx':
            self.reg += int(word)
            endStr = f'End of cycle: added {int(word)}, Register X is now {self.reg}\n'
        else:
            endStr = f'End of cycle: {word}\n'
        if self.verbose:
            print(endStr)
    def cycle(self):
        # print(f'Clock:{self.clock}, reg:{self.reg}')
        if self.verbose:
            print(f'In Cycle: clock/{self.clock}, register/{self.reg}')
        if (self.reg -1 <= (self.clock % 40) - 1 <= self.reg + 1):
            self.CRT += '#'
        else:
            self.CRT += '.'
        if (self.clock % 40) == 20:
            self.s += self.clock * self.reg
        if(self.clock % 40) == 0:
            self.CRT += '\n'
        if self.pretty:
            os.system('clear')
            print(self.CRT)
            sleep(0.17)
        #self.outPut
    def run(self):
        for word in self.words:
            #noop
            self.startCycle()
            self.cycle()
            self.endCycle(word)
        print(self.s)
flatWords = []
for line in data.split('\n'):
    flatWords += line.split(' ')
#swap addxs for noop as we can just treat them that way and since addition happens 1 cycle after treat numbers as addition instructions
V = VM(flatWords, pretty=True)
V.run()
print(V.CRT)
