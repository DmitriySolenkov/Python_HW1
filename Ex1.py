num= int(input('Введите день недели 1..7: '))
if 1<=num<=5:
    print('Будний')
elif 6<=num<=7:
    print('Выходной')
else:
    print('Неверный день недели!')
