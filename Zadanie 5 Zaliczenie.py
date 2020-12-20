print("Wprowadz 6 liczb calkowitych: ")
 
tab = []
for i in range(0, 6):
   ele = int(input())
   tab.append(ele)
 
print(tab)
wynik = 1
for ele in tab:
    if (ele>0 and ele%3==0) :
        wynik *= ele
 
print ("Oto iloczyn liczb spelniajacych warunek zadania: ")
print(wynik)