from copy import deepcopy

#maybe can use sets
def countRow(row):
    visible = 1
    tallest = row[0]
    for tree in row[1:]:
        if tree > tallest:
            tallest = tree
            visible += 1
    return visible
def formRows(table):
    fromLeft = deepcopy(table)
    fromRight = deepcopy(table)
    for row in fromRight:
        row.reverse()
    fromTop = [[] for _ in range(len(table[0]))]
    for row in table:
        for i, columnItem in enumerate(row):
            fromTop[i].append(columnItem)
    fromBottom = deepcopy(fromTop)
    for row in fromBottom:
        row.reverse()
    return (fromLeft, fromRight, fromTop, fromBottom)


#t = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
#print(f'{t[0]}\n{t[1]}\n{t[2]}\n{t[3]}')
#x = formRows(t)
#print(countRow(x[1][0]))
# solution 1
with open('../data/day8.txt') as f:
    data = f.read()
    data = data.strip().split('\n')
data = [[int(x) for x in string] for string in data]
rows = formRows(data)
visible = 0
for row in rows:
    visible += countRow(row)
print('Solution 1:', visible)