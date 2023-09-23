#!/usr/bin/env python3
with open('../data/day1.txt') as f:
    data = f.read().strip().split('\n')
sol1 = sum([int(module) // 3 - 2 for module in data])
print('Solution One:', sol1)

def calculateFuelRequired(module:int):
    fuelRequired = module // 3 - 2
    if fuelRequired <= 0:
        return 0
    return fuelRequired + calculateFuelRequired(fuelRequired)
sol2 = sum(calculateFuelRequired(int(module)) for module in data)
print('Solution Two:', sol2)
