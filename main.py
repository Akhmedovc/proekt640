from proekt640DILMUROD import funk640DILMUROD
print ('Akhmedov: Результат: ', funk640DILMUROD(5))

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