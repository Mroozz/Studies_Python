print("Podaj 7 liczb calkowitych")

tab = []
for ele in range (0, 7):
	ele = int(input())
	tab.append(ele)
print("Twoj wybor liczb: ")
print(tab)

wynik = 0
for ele in tab:
	if (ele<0 and ele%4==2):
		wynik += ele ** 2
		
print (wynik)
