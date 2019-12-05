def FindFuel(Mass, Total):
    Total += int(Mass/3) - 2
    Mass = int(Mass/3) - 2
    if Mass > 6 :
        return FindFuel(Mass, Total)
    else:
        return Total  

FuelInput = []
total = 0

with open('C:/Users/wbouw/Desktop/fuel.txt', 'r') as file:
    MassInput = [line.strip() for line in file.readlines()]

for element in MassInput:
    total += FindFuel(int(element), 0)

print(total)


