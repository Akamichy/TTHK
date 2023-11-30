import random

print("Привет! Давай проверим знания в математике!")
print("Выбери сложность: 1 - Просто, 2 - Средне, 3 - Сложно")

dif = int(input("Выбери уровень сложности (1-3): "))
while dif not in [1, 2, 3]:
    dif = int(input("Выбери уровень сложности (1-3): "))

op = input("Выбери операцию (+, -, *, /, **): ")
while op not in ['+', '-', '*', '/', '**']:
    op = input("Выбери операцию (+, -, *, /, **): ")

num_qs = int(input("Сколько примеров ты хочешь решить? "))
correct = 0

for _ in range(num_qs):
    num1 = random.randint(1, dif * 10)
    num2 = random.randint(1, dif * 10)
    correct_ans = None

    if op == '+':
        correct_ans = num1 + num2
    elif op == '-':
        correct_ans = num1 - num2
    elif op == '*':
        correct_ans = num1 * num2
    elif op == '/':
        divisor = random.randint(1, min(num1, num2))
        dividend = divisor * random.randint(1, max(num1, num2) // divisor)
        correct_ans = dividend // divisor
    elif op == '**':
        correct_ans = num1 ** num2

    question = f"{num1} {op} {num2}"
    user_ans = int(input(f"Сколько будет {question}? "))
    
    if user_ans == correct_ans:
        correct += 1
    else:
        print(f"Неправильно. Правильный ответ: {correct_ans}")

percentage = (correct / num_qs) * 100
print("Спасибо за участие!")
if percentage < 60:
    print("Оценка: 2")
elif percentage < 75:
    print("Оценка: 3")
elif percentage < 90:
    print("Оценка: 4")
else:
    print("Оценка: 5")
