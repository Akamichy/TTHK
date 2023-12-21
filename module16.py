def summa3(arv1: float, arv2: float, arv3:float)->float:
    """

    Tagastab kolme arvu summa

    :param float arv1: Esimene arv
    :param float arv2: Teine arv
    :param float arv3: Kolmas arv
    :rtype float

    """
    summa = arv1 + arv2 + arv3
    return summa

#Простейшие арифметические операции

#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, 
#которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; 
#/ — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(arv1: float, arv2: float, arv3: str) -> float:
    if arv3 == "+":
        return arv1 + arv2
    elif arv3 == "-":
        return arv1 - arv2
    elif arv3 == "*":
        return arv1 * arv2
    elif arv3 == "/":
        if arv2 == 0 and arv3 == "/":
            return ("NaN")
    else:
        return float('NaN')

conc = arithmetic(5, 3, "+")
print(conc)

def is_year_leap(arv1:int) -> bool:
    if arv1 % 4 == 0:
        return True
    else:
        return False

def square(arv1:float) -> float:
    a1 = arv1 * 4
    a2 = arv1 ** 2
    a3 = (arv1 ** 2 + arv1 ** 2)**0.5
    return(a1,a2,a3)

def season(arv1:int) -> str:
    talv = [12, 1, 2]
    kevad = [3,4,5]
    suvi = [6,7,8]
    sygis = [9,10,11]
    
    if arv1 in talv:
        return "talv"
    elif arv1 in kevad:
        return "kevad"
    elif arv1 in suvi:
        return "suvi"
    elif arv1 in sygis:
        return "sygis"

def bank(a:float, years:int) -> float:
    for i in range(years):
        a = a * 1.1
    return a

def is_prime(arv1:int) -> bool:
     if arv1 < 2:
        return False
     for i in range(2, int(arv1 ** 0.5) + 1):
        if arv1 % i == 0:
            return False
     return True

from datetime import datetime

def is_valid_date(kuup, kuu, aasta) -> bool:
    try:
        datetime(aasta=aasta, kuu=kuu, kuup=kuup)
        return True
    except ValueError:
        return False

    
