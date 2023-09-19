def loadAssignments():
    with open('../data/day4.txt') as f:
        data = f.read()
    assignments = []
    for line in data.strip().split('\n'):
        as1, as2 = line.split(',')
        assignments.append([as1.split('-'), as2.split('-')])
    return assignments

def doesListContain(outer, inner):
    if int(inner[0]) < int(outer[0]):
        return False
    if int(inner[1]) > int(outer[1]):
        return False
    return True

#solution 1
assignments = loadAssignments()
pairs = 0
for assignment in assignments:
    pairIsMatch = doesListContain(*assignment)
    if not pairIsMatch:
        assignment.reverse()
        pairIsMatch = doesListContain(*assignment)
    if pairIsMatch:
        pairs += 1

print('Solution 1:', pairs)
# solution 2
def doesListOverlapAtAll(outer, inner):
    outer = set(range(int(outer[0]), int(outer[1]) + 1))
    inner = set(range(int(inner[0]), int(inner[1]) + 1))
    overlaps = len( outer & inner )
    return overlaps > 0
pairs = 0
for assignment in assignments:
    pairIsMatch = doesListOverlapAtAll(*assignment)
    if pairIsMatch:
        pairs += 1
print('Solution 2:', pairs)
