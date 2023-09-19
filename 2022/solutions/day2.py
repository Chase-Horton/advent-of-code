keys = {"A" : 1, "B" : 2, "C" : 3, "X" : 1, "Y" : 2, "Z" : 3}
def compare(a, b):
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
# solution 1
for line in data.split('\n')[:-1]:
    a, b = line.split(' ')
    points += compare(keys[a], keys[b])
print('Solution 1:', points)
#solution 2
points = 0
for line in data.split('\n')[:-1]:
    a, b = line.split(' ')
    a, b = keys[a], keys[b]
    # need to lose
    if b == 1:
        b = a - 1
        if b < 1:
            b = 3
    # need to draw
    elif b == 2:
        b = a
    # need to win
    elif b == 3:
        b = (a % 3) + 1
    points += compare(a, b)
print('Solution 2:', points)
