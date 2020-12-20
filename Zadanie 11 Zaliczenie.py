a1 = float(input("Podaj a1"))
a2 = float(input("Podaj a2"))
b1 = float(input("Podaj b1"))
b2 = float(input("Podaj b2"))
c1 = float(input("Podaj c1"))
c2 = float(input("Podaj c2"))
wx = float(input("Podaj wx"))
wy = float(input("Podaj wy"))
w = float(input("Podaj w"))
x = float(input("Podaj x"))
y = float(input("Podaj y"))

w = a1*b2 - b1*a2 #Wyznacznik glowny
wx = c1*b2 - b1*c2
wy = a1*c2 - c1*a1

m1 = 1
m2 = 1

if w!=0:
    m1 =  m1*wx/w
    print("x = ")
    print(m1)
    m2 = m2*wy/w
    print("y = ")
    print(m2)
    
else:
    if(wx==0 and wy==0):
        print("Uklad ma nieskonczenie wiele rozwiazan")
    else:
        print("Uklad sprzeczny")



