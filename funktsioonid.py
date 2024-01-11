def Lisamine(i:list, p:list, k:int):
    """
    """
    for _ in range (k):
        nimi = input("Введите имя: ")
        palk = int(input(f'Введите зарплату для {nimi}: '))
        i.append(nimi)
        p.append(palk)

    return i, p