from proekt640AxmedovDilmurod import funk640DILMUROD
from funcKosyanenko import funk640BOGDAN
from proektQobilov import funkQobilov

y = int(input("Введите число y: "))
funk640DILMUROD(y)



x = int(input("Enter your x"))
funk640BOGDAN(x)

# Кобилов
num = int(input("Введите число num для возведения в квадрат: "))
result = funkQobilov(num)
print("Квадрат числа", num, "равен", result)

###

from funk_kuchkarova import tg_x

x = float(input("Введите угол: "))

result = tg_x(x)

print("tg(", x, ") =", result)