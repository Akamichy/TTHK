from funktsioonid import *

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ['A', 'B', 'C', 'D', 'E']

print(palgad)
print(inimesed)

lisand = input("Желаете ли вы добавить еще человек/зарплат? (Да/Нет): ").lower()

while lisand == "да":
    k = int(input("Введите количество человек: "))
    inimesed, palgad = Lisamine(inimesed, palgad, k)
    for i in range(len(palgad)):
        print(inimesed[i], 'получает', palgad[i])

    lisand = input("Желаете ли вы добавить еще человек/зарплат? (Да/Нет): ").lower()

while True:
    print("""
    1. Удалить человека и его зарплату
    2. Чья зарплата самая большая
    3. Чья зарплата самая маленькая
    4. Упорядоченный список зарплат по возрастанию
    5. Вывод на экран людей с одинаковыми зарплатами 
    6. Поиск зарплаты по имени
    7. Кто получает меньше/больше, чем n-ное число
    8. Топ самых бедных и богатых людей
    9. Средняя зарплата человека из списка
    10. Вывод зарплат после вычета подоходного налога
    0. Выход
    """)
    def spisok():
        print("Список зарплат и людей:")
        for i, (nimi, palk) in enumerate(zip(inimesed, palgad), start=1):
            print(f"{i}.{nimi} получает {palk}")
        print("0 - выход")



    choice = input("Выберите номер операции: ")

    if choice == "1":
        print("Список зарплат и людей:")
        for i, (nimi, palk) in enumerate(zip(inimesed, palgad), start=1):
            print(f"{i}.{nimi} получает {palk}")
        print("0 - выход")

        remove = int(input("Напишите номер человека, которого хотите удалить из списка: "))

        if 0 < remove <= len(inimesed):
            inimesed.pop(remove - 1)
            palgad.pop(remove - 1)
        elif remove == 0:
            pass
        else:
            print("Некорректный номер человека. Пожалуйста, введите правильный номер.")

            pass
    elif choice == "2":
        index = palgad.index(max(palgad))
        print(f'Самая высокая зарплата на данный момент у {str(inimesed[index])} в размере {palgad[index]} евро.')

        pass
    elif choice == "3":
        index = palgad.index(min(palgad))
        print(f'Самая маленькая зарплата на данный момент у {str(inimesed[index])} в размере {palgad[index]} евро.')
        pass
    elif choice == "4":
        sorted_indices = sorted(range(len(palgad)), key=lambda k: palgad[k])

        print("Список зарплат и людей (в порядке возрастания зарплат):")
        for i, index in enumerate(sorted_indices, start=1):
            nimi = inimesed[index]
            palk = palgad[index]
            print(f"{i}.{nimi} получает {palk}")
        pass
    elif choice == "5":
        permalist = []
        for i in range(len(palgad)):
            for j in range(i + 1, len(palgad)):
                if palgad[i] == palgad[j] and inimesed[i] != inimesed[j]:
                    if inimesed[i] not in permalist and inimesed[j] not in permalist:
                        permalist.append(inimesed[i])
                        permalist.append(inimesed[j])

                        print(f'{inimesed[i]} с зарплатой {palgad[i]}')
                        print(f'{inimesed[j]} с зарплатой {palgad[j]}')
        pass
    elif choice == "6":
        element = (input("Введите имя, чью зарплату хотите узнать: "))
        position = inimesed.index(element)
        print(f'{inimesed[position]} получает зарплату в размере {palgad[position]} евро.')
        pass
    elif choice == "7":
        suurus = int(input("Введите сумму: "))
        for i in range(len(palgad)):
            if palgad[i] > suurus:
                print(f'{inimesed[i]} получает больше указанной суммы на {palgad[i] - suurus} евро ({palgad[i]})')
            elif palgad[i] < suurus:
                print(f'{inimesed[i]} получает меньше указаной суммы на {suurus - palgad[i]} евро ({palgad[i]})')
        pass
    elif choice == "8":
        permalist2 = []
        permalist2 = palgad.copy()
        top = int(input("Топ скольки самых богатых людей вам показать?: "))
        for i in range(min(top, len(permalist2))):
            maxx = max(permalist2)
            index = permalist2.index(maxx)
            print(f'{inimesed[index]} в размере {maxx} евро')
            permalist2[index] = float('-inf')
        pass
    elif choice == "9":
        
        pass
    elif choice == "10":
        spisok()
        num11 = int(input("Пожалуйста, введите индекс человека, которого хотите проверить"))
        if num11 == 0:
            continue
        
        palg = palgad[num11]
        if palg > 1200 and palg < 2100:
            tulumaksuvaba = 654 - 0.72667 * (palgad[num11] - 1200)
        elif palg < 1200:
            tulumaksuvaba = 654
        elif palg > 2100:
            tulumaksuvaba = 0

        tulumaks = ((palg - tulumaksuvaba) * 0.2)
        vabapalk = palg - tulumaks
        print(vabapalk)
        pass
    elif choice == "0":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, введите правильный номер операции.")
