keys = {"A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}
def compare(a, b):
    a, b = keys[a], keys[b]
    points = b
    # draw
    if a == b:
        return points + 3
    # win
    if a == b - 1 or a == 3 and b == 1:
        return points + 6
    # loss
    return points
with open('../data/day2.txt') as f:
    data = f.read()
points = 0
for line in data.split('\n')[:-1]:
    a, b = line.split(' ')
    points += compare(a, b)
print('Solution:', points)
