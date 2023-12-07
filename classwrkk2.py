
s = input("Sisesta text: ")
s_list = list(s)
k = len(s_list)
if s.isdigit():
    for t in range(k):
        num=int(s_list[t])
        s_list.pop(t)
        s_list.insert(t,num)


    summa = 0
    for e in s_list:
       summa += e
    print("Summa: ", summa)
    
print(s_list)

e = input("Element: ") 

try:
    if e.isalpha():
        ind = s_list.index(e)
    elif e.isdigit():
        ind = s_list.index(int(e))
    print(f'Element {e} on {indeks} positsioonil')
except:
    print("Element puudub")
     