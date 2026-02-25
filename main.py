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
    funk640DILMUROD()
elif request == 2:
    funk640BOGDAN()
elif request == 3:
    funk320QJK()
elif request == 4:
    funk640ABDULAZIZ()
elif request == 5:
    funk640Sarvina()
else:
    print("Неверный номер функции.")