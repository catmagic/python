if __name__ == '__main__':
    minimum = float(input("Введите минимум\n"))
    maximum = float(input("Введите максимум\n"))
    mylist = list(map(float, input("Введите  диапозон\n").split()))
    res = []
    for i in range(len(mylist)):
        if (mylist[i] >= minimum and mylist[i] <= maximum):
            res.append(i)
    print(*res)
