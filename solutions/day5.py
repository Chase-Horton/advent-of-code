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
        #print(self.stacks)
        #print(f'moving {amt} from {fromId} to {toId}')
        for _ in range(int(amt)):
            self.stacks[toId].append(self.stacks[fromId].pop())
        #print(self.stacks)
    def printTops(self):
        finalStr = ''
        for key in self.stacks:
            top = self.stacks[key].pop()
            print(f'{key}:{top}')
            finalStr += top
        print(finalStr)
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
