"""ulesanne 1"""
name = input()
print(f'Tere, {name}')

"""ulesanne 2"""

print(3+8/(4-2)*4)
print((3+8)/(4-2)*4)
print(3+(8/4)-(2*4))
print(3+8/4-2*4)

import math

"""ulesanne 2.1"""
r = 3
a = r*2
s = a**2
p = a*4
s2 = math.pi*(r**2)
c = 2*math.pi*r
print(f'Ruudu pindala on {s}, ruudu umbermoot on {p}, ringi pindala on {s2}, ringi umbermoot {c}')

"""ulesanne 2.2"""
count1 = 0
earth = 6378
mars = 3389
print("1.Earth")
print("2.Mars")
print("3.Raadiuse kasitsi sisestamine")
planet = int(input('Palun valige mis planeet te valisite: '))

if planet == 1:
    munt = int(input("Palun siseta mis munt te valisite: "))
    if munt == 2:
        count1 = (math.pi * 2 * earth) / 0.0002575
    elif munt == 1:
        count1 = (math.pi * 2 * earth) / 0.0002325
elif planet == 2:
    munt = int(input("Palun siseta mis munt te valisite: "))
    if munt == 2:
        count1 = (math.pi * 2 * mars) / 0.0002575
    elif munt == 1:
        count1 = (math.pi * 2 * mars) / 0.0002325
elif planet == 3:
    muntr = float(input("Mundi labimoot: "))
    planetr = float(input("Planeedi raadius: "))
    count1 = (math.pi * 2 * planetr) / (muntr/100000)
print(count1)

"""ulesanne 3"""
print("kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll killkoll kill-koll")

"""ulesanne 4"""
print("Rong see soitis tsuhh tsuhh tsuhh,")
print("piilupart oli rongijuht.")
print("Rattad tegid rat tat taa,")
print("rat tat taa ja tat tat taa.")
print("Aga seal rongi peal,")
print("kas sa tead, kes olid seal?")

"""ulesanne 5"""

a = float(input("A: "))
b = float(input("B: "))
s = a*b
p = 2*(a*b)

print(f'Ristkuliku pindala on {s}, umbermoot on {p}')

"""ulesanne 6"""

km = int(input("Kilomeetrite arv: "))
li = int(input("Liitrite arv: "))
km2 = km/100
arv = km / li
print(f'Keskmine kutusekulu 100km kohta on {arv}')

"""ulesanne 7"""
k = 29.9
kpm = k / 60
mins = int(input("Kui kaua soidab (minutiga)"))
kaugele = kpm * mins
print(f'Soidab umbes {kaugele} kilomeetrit.')

