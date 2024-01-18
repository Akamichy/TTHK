#def Loe_failist(fail:str)->list:
#    jarjend = []
#    f = open(fail,'r', encoding = "utf-8-sig")
#    for rida in f:
#        jarjend.append(rida.strip())
#    f.close()
#    return jarjend

def Kirjuta_failisse(fail:str, jarjend:list):
    f = open(fail, 'w', encoding = "utf-8-sig")
    for item in jarjend:
        f.write(item+'\n')
    f.close()

#paevad = Loe_failist("TextFile1.txt")
#print(paevad)

list_=[]
for i in range(5):
    nimi=input(str(i+1)+ ".slovo ")
    list_.append(nimi)
Kirjuta_failisse("est.txt", list_)

#with open('Nimed.txt', 'r') as f:
#    print(f.read())

#from os import *
#if path.isfile("Nimed.txt"): 
#    remove("Nimed.txt")