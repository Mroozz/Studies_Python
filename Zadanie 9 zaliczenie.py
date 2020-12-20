
macierz = [] 
print("Napisz 9 wartosci macierzy:") 

for i in range(3):		 
	a =[] 
	for j in range(3):
		a.append(int(input())) 
	macierz.append(a) 

for i in range(3): 
	for j in range(3): 
		print(macierz[i][j], end = " ") 
	print() 

a=1
for i in range (3):
    for j in range(3):
        if macierz[i][j]%3==0 or macierz[i][j]%4==0:
            a *= macierz[i][j]
            print("Wynik iloczynu dla warunku zadania to: ")
            print(a)
