def test():
    n = int(input('Введите число: '))
    summ = 1
    for i in range(1,7+1):
        if i % n == 0:
            print(i, end=' ')
            summ *= 1/(2**i)
    print('\n\nСумма равна:', summ)


test()
