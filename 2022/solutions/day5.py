import re
class Stacker:
    def __init__(self, listTop):
        self.keys = {}
        self.stacks = {}
        layers = listTop.split('\n')
        layer = layers.pop()
        #get index and id for each column
        self.getKeysAndStacks(layer)
        #fill stacklists with obj from column
        self.populateStacks(layers)
    def getKeysAndStacks(self, baseLayer):
        for i, item in enumerate(baseLayer):
            if item != ' ':
                self.keys[item] = i
                self.stacks[item] = []
    def populateStacks(self, layers):
        for layer in reversed(layers):
          for key in self.keys:
              indexVal = layer[self.keys[key]]
              if indexVal != ' ':
                  self.stacks[key].append(indexVal)
    def move(self, string):
        amt, fromId, toId = re.findall(r'\b\d+\b', string)
        for _ in range(int(amt)):
            self.stacks[toId].append(self.stacks[fromId].pop())
    def moveSlice(self, string):
        amt, fromId, toId = re.findall(r'\b\d+\b', string)
        if amt == 1:
            self.stacks[toId].append(self.stacks[fromId].pop())
            return
        self.stacks[toId] += self.stacks[fromId][-int(amt):]
        self.stacks[fromId] = self.stacks[fromId][:-int(amt)]
    def printTops(self):
        finalStr = ''
        for key in self.stacks:
            top = self.stacks[key].pop()
            print(f'{key}:{self.stacks[key]}')
            finalStr += top
        print('Stack Out:', finalStr)
with open('../data/day5.txt') as f:
    data = f.read()
# solution 1
data = data.split('\n\n')
stacks = data[0]
S = Stacker(stacks)
for line in data[1].split('\n'):
    if line == '':
        break
    S.move(line)
S.printTops()

# solution 2
S = Stacker(stacks)
for line in data[1].split('\n'):
    if line == '':
        break
    S.moveSlice(line)
S.printTops()
