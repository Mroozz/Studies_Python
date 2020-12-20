import os
import matplotlib.pyplot as plt
from cmath import sqrt
r=[]
l=[]
print("Wartosci dla funkcji kwadratowej: ")
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
delta = b * b - 4 * a * c
if delta > 0:
    print("Funkcja ma 2 miejsca zerowe")
    fun = "Funkcja ma 2 miejsca zerowe"
    x = (-b - sqrt(delta)) / 2 * a
    xx = (-b + sqrt(delta)) / 2 * a
    print(x.real, xx.real)
    p = - b / (2*a)
    q = - delta / (4*a)
    print("W = ",p,q)
elif delta == 0:
    print("Funkcja ma 1 miejsce zerowe")
    fun = "Funkcja ma 1 miejsca zerowe"
    x = - b / (2*a)
    print(x.real)
    p = - b / (2*a)
    print("W = ",p,"0")
else:
    print("Funkcja nie ma miejsc zerowych")
    fun = "Funkcja nie ma miejsc zerowych"
    x = (-b - sqrt(delta)) / 2 * a
    xx = (-b + sqrt(delta)) / 2 * a
    print(x.real, xx.real)
    p = - b / (2*a)
    q = - delta / (4*a)
    print("W = ",p,q)
print("Delta = ",delta)
os.system("pause")
for n in range (-15,15,1):
        m=a*(n**2)+b*n+c
        r.append(n)
        l.append(m)
plt.figure().add_subplot(1,1,1).plot(r,l)
plt.axhline(y=0, color="#cccccc")
plt.axvline(x=0, color="#cccccc")
text = fun, x.real, xx.real
plt.text(-15,220,text, fontsize=8,
        verticalalignment='top')
plt.show()