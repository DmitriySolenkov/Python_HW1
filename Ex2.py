x = int(input('Введите координату х: '))
y = int(input('Введите координату y: '))
if x == 0 or y == 0:
    print('Неверные координаты!')
elif x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')
