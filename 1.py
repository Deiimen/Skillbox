def test():
    n = int(input('Введите число: '))
    summ = 1
    for i in range(1, 50+1):
        if i % n == 0:
            print('числа ряда',i, end=' ')
            summ += i
    print('\n\nСумма равна:', summ)


test()
