#!/usr/bin/env python3
# --- Day 11: Monkey in the Middle ---
#Starting items: 79, 98
# Operation: new = old * 19
# Test: divisible by 23
#   If true: throw to monkey 2
#   If false: throw to monkey 3
import math

class Monkey:
    def __init__(self, startingItems, operation, test):
        self.items = self.splitIntoWords(startingItems, ', ')
        self.operation = self.splitIntoWords(operation)[3:]
        self.testNum = int(self.splitIntoWords(test[0])[2])
        self.throwTo = [int(self.splitIntoWords(monkey)[3]) for monkey in test[1:]]
        self.inspectCount = 0

    def splitIntoWords(self, string, splitStr=' '):
        return string.split(':')[1].strip(' ').split(splitStr)

    def run(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            if self.operation[1] != 'old':
                item = eval(f'int(item) {self.operation[0]} {self.operation[1]}')
            else:
                item = int(item) * int(item)
            item = math.floor(item / 3)
            self.inspectCount += 1
            if item % self.testNum == 0:
                yield (self.throwTo[0], item)
            else:
                yield (self.throwTo[1], item)
#solution 1
with open('../data/day11.txt') as f:
    data = f.read().strip().split('\n\n')
monkeys = []
for monkey in data:
    lines = monkey.split('\n')[1:]
    monkeys.append(Monkey(lines[0], lines[1], lines[2:]))
for rounds in range(20):
    for monkey in monkeys:
        for throwTo, worryAmt in monkey.run():
            monkeys[throwTo].items.append(worryAmt)

for i, monkey in enumerate(monkeys):
    print(i, monkey.inspectCount)
monkeyBusiness = sorted([monkey.inspectCount for monkey in monkeys])[-2:]
print(monkeyBusiness)
print(monkeyBusiness[0] * monkeyBusiness[1])
