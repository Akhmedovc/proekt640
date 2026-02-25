import proekt640BogdanK
import proekt640DILMUROD

n1 = int(input("Выберите действие: 1 - Богдан, 2 - Дильмурод: "))

if n1 == 1:
    proekt640BogdanK.funk640()
elif n1 == 2:
    proekt640DILMUROD.funk640DILMUROD()
else:
    print("Неверный выбор! Введите 1 или 2.")