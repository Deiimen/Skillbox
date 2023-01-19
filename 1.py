def test():
    n = int(input('Введите число: '))
    summ = 1
    print('числа ряда кратных',n, end=' ')
    for i in range(1, 50+1):
        if i % n == 0:
            print(i, end=' ')
            summ += i
    print('\n\nСумма равна:', summ)


test()
