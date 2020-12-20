tab = []
n = 0
for i in range(0, 10):
    i += n+1
    tab.append(i)
print (tab)

parzyste = 0
for i in tab:
    if(i%2==0):
        parzyste += i

print("To jest suma liczb parzystych: ")
print(parzyste)

nieparzyste = 0
for i in tab:
    if not(i%2==0):
        nieparzyste += i

print("A to nieparzystych ...")
print(nieparzyste)
        