def Lisamine(i:list, p:list, k:int):
    """
    """
    for _ in range (k):
        nimi = input("Введите имя: ")
        palk = int(input(f'Введите зарплату для {nimi}: '))
        i.append(nimi)
        p.append(palk)

    return i, p

def venesona():
    newrus = input("Верное написание слова: ")
    return newrus

def eestisona():
    newest = input("Sona ilma vigadeta: ")
    return newest