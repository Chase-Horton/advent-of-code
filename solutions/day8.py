from copy import deepcopy

def countRow(row, ids = []):
    visible = 0
    tallest = row[0]
    newIds = []
    newIds.append(tallest["tree_id"])
    if tallest["tree_id"] not in ids:
        newIds.append(tallest["tree_id"])
        visible += 1
    for tree in row[1:]:
        if tree["value"] > tallest["value"]:
            tallest = tree
            if tallest["tree_id"] not in ids:
                visible += 1
                newIds.append(tallest["tree_id"])
    return visible, newIds
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
i = 0
rows = []
for string in data:
    row = []
    for x in string:
        obj = {'tree_id':i, 'value':int(x)}
        row.append(obj)
        i += 1
    rows.append(row)
data = formRows(rows)
visible = 0
ids = []
for lst in data:
    for row in lst:
        newVisible, newIds = countRow(row, ids)
        ids += newIds
        visible += newVisible
print('Solution 1:', visible)
#seeing solution 2 should refactor one to use functions to simply look below or above and object and treat this like linked list, then I can just call look up for each d