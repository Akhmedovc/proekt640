def funk320QJK():
    arr = [int(x) for x in input("Введите числа через пробел: ").split()]
    if len(arr) < 2:
        return None

    arr.sort()

    return arr[len(arr) - 2]