from math import hypot
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
dist = hypot(abs(x1-x2), abs(y1-y2))
print(dist)
