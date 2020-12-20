tab = []
n = 0
for i in range(0, 10):
    i = int(input())
    tab.append(i)
print (tab)
czujka = True
warunek = tab[1]-tab[0]
for i in range(1, tab[9]):
    if i+1<10 and tab[i+1]-tab[i]!=warunek:
        print("Ten ciag nie jest arytmetyczny")
        czujka = False
        break
 
if czujka == True:
    print("Ten ciag jest arytmetyczny")