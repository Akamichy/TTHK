'''Написать программу для проверки знаний по математике.

Предложить пользователю выбрать сложность заданий.
Например:
Tase 1, Tase 2, Tase 3
количество действий(+,-,/,*,**)
величину случайно генерируемых чисел.

В программе случайным образом "задаются" примеры, с учетом сложности провряемых знаний.
После введенного пользователем ответа, проверяется его правильностью.

Придумать условие выхода из цикла.(можно сначала указать количество примеров)

В конце работы программы, надо сообщить тестируемому оценку.
<60% - Hinne 2
60-75% - Hinne 3
75-90% - Hinne 4
>90% - Hinne 5
'''
from random import *
from math import *
import sys
correct_ans = 0
opl = ["+", "-", "*", "/", "**"]
print("Привет, я твой помощник к подготовке к экзамену по математике!")
print()
print("Всего на выбор дается 3 уровня слоэности, от них зависит то, с какими числами ты будешь работать!")
print()
print("Если захочешь выйти, то просто напиши 'ВЫХОД' после введения количества желаемых примеров.")
dif = (input("Выберите сложность заданий! 1 - Легко, 2 - Средне, 3 - Тяжело: "))

while dif not in ["1", "2", "3"]:
    dif = (input("Выберите сложность заданий! 1 - Легко, 2 - Средне, 3 - Тяжело: "))
    if dif == "ВЫХОД":
        sys.exit()
qs = str(input("Сколько примеров ты хочешь решить?: "))
if qs == 'ВЫХОД':
    sys.exit()

qs = int(qs)
dif = int(dif)

for i in range(int(qs)):
    correct = None
    opn = randint(0, 4)
    op = opl[opn]
    num1 = randint(1, dif * 10)
    num2 = randint(1, dif * 10)
    num3 = randint(1, dif*10)
    num4 = randint(1, 4)
    if op == "+":
        correct = num1 + num2
        print(f'{num1} {op} {num2}')
    elif op == "-":
        correct = num1 - num2
        print(f'{num1} {op} {num2}')
    elif op == "/":
        if num1 > num2:
            correct = round(num1 / num2, 2)
            print(f'{num1} {op} {num2}')
        else:
            correct = round(num2 / num1, 2)
            print(f'{num2} {op} {num1}')
    elif op == "*":
        correct = num1 * num2
        print(f'{num1} {op} {num2}')
    elif op == "**":
        correct = num3**num4
        print(f'{num3}^{num4}')

    v = float(input("Введите ваш ответ(округлите до сотых, максимум 2 цифры после запятой): "))
    if v == "ВЫХОД":
        print("Всего хорошего!")
        sys.exit()
    elif v == correct:
        correct_ans += 1
        print("Верно")
    else:
        print(f'Неверно, правильный ответ {correct}')

percentage = (correct_ans / qs) * 100
for i in range(5):
    print( )
print("Спасибо за участие!")
if percentage < 60:
    print("Оценка: 2")
elif percentage < 75:
    print("Оценка: 3")
elif percentage < 90:
    print("Оценка: 4")
else:
    print("Оценка: 5")


