from proekt640AxmedovDilmurod import funk640DILMUROD
from proekt640KosyanenkoBogdan import funk640BOGDAN
from proekt320QobilovJahongir import funk320QJK
from proekt640AbutolipovAbdulaziz import funk640ABDULAZIZ
from proect640Kuchkarova_Sarvinoz import funk640Sarvina


request = int(input(
    "Введите номер функции:\n"
    "1 - DILMUROD\n"
    "2 - BOGDAN\n"
    "3 - QJK\n"
    "4 - ABDULAZIZ\n"
    "5 - Sarvina\n"
))

if request == 1:
    y = int(input("Введите число y: "))
    funk640DILMUROD(y)
elif request == 2:
    x = int(input("Введите число x: "))
    funk640BOGDAN(x)
elif request == 3: 
    arr = list(map(int, input("Введите массив чисел через пробел: ").split()))
    result = funk320QJK(arr)
    if result is not None:
        print(f"Второй по величине элемент: {result}")
    else:
        print("Массив должен содержать хотя бы два элемента.")
elif request == 4:
    x = int(input("Введите число x: "))
    y = int(input("Введите число y: "))
    result_x, result_y = funk640ABDULAZIZ(x, y)
    print(f"Число x: {result_x}, Число y: {result_y}")
elif request == 5:
    x = float(input("Введите угол в градусах: "))
    funk640Sarvina(x)
else:
    print("Неверный номер функции. Пожалуйста, выберите от 1 до 5.")