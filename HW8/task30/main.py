# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = float(input("Введите первый член арифметической прогрессии\n"))
    d = float(input("Введите разность арифметической прогрессии\n"))
    n = int(input("Введите  количество членов арифметической прогрессии\n"))
    res = [ a+i*d for i in range(n)]
    for  an in res:
        print(an)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
