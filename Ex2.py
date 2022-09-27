x = int(input('Введите координату х: '))
y = int(input('Введите координату y: '))
if x == 0 and y == 0:
    print('Неверные координаты!')
elif x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y > 0:
    print('2  четверть')
elif x < 0 and y < 0:
    print('3  четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif x == 0:
    print('Ось Х')
else:
    print('Ось Y')
