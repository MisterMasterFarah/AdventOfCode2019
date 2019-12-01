import math

def FindFuel(mass):
    return (math.floor(int(mass)/3)) - 2

FuelInput = []
total = 0

with open('C:/Users/wbouw/Desktop/fuel.txt', 'r') as file:
    MassInput = [line.strip() for line in file.readlines()]


for element in MassInput:
    total += FindFuel(element)

print(total)


