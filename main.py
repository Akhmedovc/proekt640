import proekt640BogdanK
import proekt640DILMUROD

from funk320QJK import funk320QJK

from proekt640BogdanK import funk640

#добавил новый скрипт Богдана
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