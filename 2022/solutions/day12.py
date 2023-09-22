#!/usr/bin/env python3
from dataclasses import dataclass
import numpy as np
import os
from time import sleep
import heapq
from rich import print
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy import interpolate
GRID_SIZE = (5, 8)

class Node:
    @classmethod
    def loadData(cls):
        with open('../data/day12.txt') as f:
            cls.GRID = f.read().strip().split('\n')
        cls.GRID_SIZE = (len(cls.GRID), len(cls.GRID[0]))
        print(cls.GRID)
        cls.ORIGIN = [0,0]
        cls.dirsToCheck = [[-1,0], [1,0], [0,-1], [0,1]]
        for x, line in enumerate(cls.GRID):
            for y, char in enumerate(line):
                if char == 'E':
                    cls.TARGET = (x, y)
                    cls.GRID[x] = cls.GRID[x][:y] + 'z' + cls.GRID[x][y + 1:]
                elif char == 'S':
                    cls.ORIGIN = (x, y)
    def __lt__(self, other):
        return self.fCost < other.fCost

    def __init__(self, x, y, parent):
        if x == None:
            x, y = self.ORIGIN
        self.height = ord(self.GRID[x][y].lower())
        self.gridX = int(x)
        self.gridY = int(y)
        self.coords = (self.gridX, self.gridY)

        self.parent = parent
        if self.parent:
            self.gCost = parent.gCost + 1
        else:
            self.gCost = 0
        self.neighbors = []
    @property
    def hCost(self):
        return abs(self.TARGET[0] - self.gridX) + abs(self.TARGET[1] - self.gridY)
    @property
    def fCost(self):
        return self.hCost + self.gCost

    def getNeighbors(self):
        for x,y in self.dirsToCheck:
            if abs(x) == abs(y):
                continue
            #print(f'adjusting by {x},{y}')
            x = self.gridX + x
            y = self.gridY + y
            # check and neighbor not closed and if open < hash
            if self.GRID_SIZE[0] > x >= 0 and self.GRID_SIZE[1] > y >= 0:
                newNode = Node(x, y, self)
                if newNode.height <= self.height + 1:
                    self.neighbors.append(newNode)
                    # print('added node')
                else:
                    pass
                    # print('too tall')
            else:
                pass
                # print('outside grid')
        return self.neighbors
    # testing
    def __repr__(self):
        return f'x:{self.gridX},\ty:{self.gridY}\the:{self.height}\tc:{chr(self.height)}\tg:{self.gCost}\th:{self.hCost}\tf:{self.fCost}'
    def printGrid(self, printNeighbors=True):
        if printNeighbors:
            neighborLocs = [(neighbor.gridX, neighbor.gridY) for neighbor in self.neighbors]
            #print(neighborLocs)
        for x in range(len(self.GRID)):
            for y in range(len(self.GRID)):
                if x == self.gridX and y == self.gridY:
                    print('[red]' + self.GRID[x][y] + '[/red]', end='')
                elif printNeighbors and (x, y) in neighborLocs:
                    print('[green]' + self.GRID[x][y] + '[/green]', end='')
                else:
                    print(self.GRID[x][y], end='')
            print()
def printGrid(grid, openN, closedN):
    string = ''
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (x,y) in [n.coords for n in closedN]:
                string += '[red]' + grid[x][y] + '[/red]'
            elif (x,y) in [n.coords for n in openN]:
                string += '[green]' + grid[x][y] + '[/green]'
            else:
                string += grid[x][y]
        string += '\n'
    print(string)
def aStar():
    Node.loadData()
    startNode = Node(None, None, None)
    openNodes = [startNode]
    closedNodes = []
    while startNode:
        # TODO (use heap)
        current = None
        for node in openNodes:
            if current == None or node.fCost < current.fCost:
                current = node
        # remove will fix this with heap
        #print('current:',current)
        openNodes = [n for n in openNodes if n.coords != current.coords]
        closedNodes.append(current)
        #print('Open Nodes:', openNodes)
        #print('closed Nodes:', closedNodes)
        if current.coords == Node.TARGET:
            return current
        for neighbor in current.getNeighbors():
            #print('neighbors:',neighbor)
            if neighbor in closedNodes:
                continue
            if neighbor.coords in [n.coords for n in openNodes] and neighbor.gCost - 1 > current.gCost:
               if neighbor in openNodes:
                   #print('in openNodes')
                   neighbor.gCost = current.gCost + 1
            elif neighbor.coords not in [n.coords for n in closedNodes]:
                #print('appending')
                openNodes.append(Node(neighbor.gridX, neighbor.gridY, current))
        #print('current grid')
        #printGrid(current.GRID, openNodes, closedNodes)
def aStar2():
    Node.loadData()
    startNode = Node(None, None, None)
    openNodes = [(startNode.fCost, startNode)]  # Use a heap of (fCost, Node) tuples
    closedNodes = []

    while openNodes:
        _, current = heapq.heappop(openNodes)  # Get the node with the lowest fCost

        closedNodes.append(current)

        if current.coords == Node.TARGET:
            return current

        for neighbor in current.getNeighbors():
            if neighbor in closedNodes:
                continue

            gCost = current.gCost + 1
            if neighbor.coords in [n[1].coords for n in openNodes]:
                # If neighbor is already in openNodes, update its gCost if it's better
                index = [n[1].coords for n in openNodes].index(neighbor.coords)
                if gCost < openNodes[index][1].gCost:
                    openNodes[index] = (gCost + neighbor.hCost, neighbor)
            elif neighbor.coords not in [n.coords for n in closedNodes]:
                # If neighbor is not in openNodes or closedNodes, add it to openNodes
                heapq.heappush(openNodes, (gCost + neighbor.hCost, neighbor))
        #printGrid(current.GRID, [n[1] for n in openNodes], closedNodes)
    # If the loop ends without finding the target, there's no solution
    return None
# Node.loadData()
# n = Node(0, 0, None)
# print(n.GRID)
# print(n.ORIGIN)
# print(n.TARGET)
# n.printGrid()
# n.getNeighbors()
# n.printGrid()
# print(n)
# for neigh in n.neighbors:
#     print(neigh)
# print()
# n = n.neighbors[0]
# print(n)
# n.printGrid()
# n.getNeighbors()
# n.printGrid()
# for neigh in n.neighbors:
#     print(neigh)
# print()
# n = n.neighbors[1]
# print(n)
# n.printGrid()
# n.getNeighbors()
# n.printGrid()
# for neigh in n.neighbors:
#     print(neigh)
# n = n.neighbors[3]
# print(n)
# n.printGrid()
# n.getNeighbors()
# n.printGrid()
# for neigh in n.neighbors:
#     print(neigh)
def getHeightMap(grid):
    newGrid = []
    for row in grid:
        newRow = []
        for char in row:
            newRow.append(ord(char.lower()) - ord('a'))
        newGrid.append(newRow)
    return newGrid
end = aStar2()
grid = end.GRID
s = -1
indexes = []
while end:
    indexes.append(end.coords)
    s += 1
    end = end.parent
N = Node(None,None,None)
grid = N.GRID
string = ''
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x, y) in indexes:
            string += '[green]' + grid[x][y] + '[/green]'
        else:
            string += grid[x][y]
    string += '\n'
print(string)
print(s)



z = np.array(getHeightMap(grid))
x, y = np.meshgrid(range(len(z)), range(len(z[0])))
x = x.T
y = y.T

# show hight map in 2d
plt.figure()
plt.title('letter height')
p = plt.imshow(z)
plt.colorbar(p)
plt.show()

num_points = 100  # Adjust this as needed for smoother or coarser results

# Create a new grid with more points for interpolation
x_fine = np.linspace(x.min(), x.max(), num_points)
y_fine = np.linspace(y.min(), y.max(), num_points)
x_fine, y_fine = np.meshgrid(x_fine, y_fine)
z_fine = interpolate.griddata((x.flatten(), y.flatten()), z.flatten(), (x_fine, y_fine), method='cubic')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_fine, y_fine, z_fine, cmap='viridis')
x_ticks = len(ax.get_xticks())
y_ticks = len(ax.get_yticks())
aspect_ratio =   y_ticks/x_ticks

# Set the aspect ratio based on the calculated ratio
ax.set_xlim(80, 120)
ax.set_ylim(0, 40)
ax.set_box_aspect([1, 1, 1])
plt.title('3d height map')
plt.show()
