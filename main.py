import proekt640BogdanK
import proekt640DILMUROD


#добавил новый скрипт Богдана
from proekt640BogdanK import funk640

funk640(3)

#Кобилов добавляет свой код
from funk320QJK import funk320QJK

user_input = input("Введите числа через пробел: ")

nums = [int(x) for x in user_input.split()]

result = funk320QJK(nums)

if result is None:
    print("Второго по величине элемента нет")
else:
    print("Второй по величине элемент:", result)

n1 = int(input("Выберите действие: 1 - Богдан, 2 - Дильмурод: "))

if n1 == 1:
    proekt640BogdanK.funk640()
elif n1 == 2:
    proekt640DILMUROD.funk640DILMUROD()
else:
    print("Неверный выбор! Введите 1 или 2.")

