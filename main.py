from proekt640AxmedovDilmurod import funk640DILMUROD

from proekt640KosyanenkoBogdan import funk640

from proekt320QobilovJahongir import funk320QJK

from proekt640AbutolipovAbdulaziz import funk320FIO

#Дильмурод добавляет свой код
funk640DILMUROD(0)

#Богдан добавляет свой код
funk640(3)

#Кобилов добавляет свой код
user_input = input("Введите числа через пробел: ")

nums = [int(x) for x in user_input.split()]

result = funk320QJK(nums)

if result is None:
    print("Второго по величине элемента нет")
else:
    print("Второй по величине элемент:", result)

n1 = int(input("Выберите действие: 1 - Богдан, 2 - Дильмурод: "))

#Абдулазиз добавляет свой код

x = 39
y = 20

result_x, result_y = funk320FIO(x, y)

print(f"{x} -> {result_x}")
print(f"{y} -> {result_y}")
