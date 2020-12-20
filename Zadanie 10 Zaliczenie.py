import numpy as np 

R = int(input("Wpisz liczbe rzedow: ")) 
C = int(input("Wpisz liczbe kolumn: ")) 

w1 = list(map(int, input("Wpisz wartosci dla macierzy A ,kazdy po spacji :").split())) 
w2 = list(map(int, input("Wpisz wartosci dla macierzy B ,kazdy po spacji :").split())) 

m1 = np.array(w1).reshape(R, C) 
print(m1) 

m2 = np.array(w2).reshape(R, C) 
print(m2) 

c = []
c = m1+m2
print("Suma elementow wynosi :")
print(c)

d=[]
d = m1*m2
print("Iloczyn elementow wynosi: ")
print(d)