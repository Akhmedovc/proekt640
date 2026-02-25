def funk320FIO(x, y):
    x = int(input("Введите число x: "))
    y = int(input("Введите число y: "))

    if x % 2 == 0:
        result_x = "Четное"   
    else:
        result_x = "Нечетное"    

    if y % 2 == 0:
        result_y = "Четное"
    else:
        result_y = "Нечетное"

    return result_x, result_y
