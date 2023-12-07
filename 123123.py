import math 
print("Ruudu karakteristikud")
a=int(input('Sisesta ruudu kulje pikkus => '))
S=float(a**2)
print("Ruudu pindala", S)
P=float(4*a)
print("Ruudu umbermoot", P)
di=(2*(a**2))**0.5
print("Ruudu diagonaal", round(di,2))
print()
print("Ristkuliku karakteristikud")
b=int(input("Sisesta ristkuliku 1. kulje pikkus => "))
c=int(input("Sisesta ristkuliku 2. kulje pikkus => "))
S=b*c
print('Ristkuliku pindala', S)
P=2*(b+c)
print("Ristkuliku umbermoot", P)
di=(b**2+c**2)**0.5
print("Ristkuliku diagonaal", round(di, 1))
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => '))
d=2*r
print("Ringi labimoot", d)
S = math.pi*(r**2)
print("Ringi pindala", round(S,2))
C= math.pi * r * 2
print("Ringjoone pikkus", round(C, 2))
