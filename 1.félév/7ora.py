#for ciklus:
for i in range(5): # i = 0, 1, 2, 3, 4
    print(i)
print()
for i in range(3, 8):  #i = 3, 4, 5, 6, 7
    print(i)
print()
for i in range(9, 27, 3): #i = 9, 12, 15, 18, 21, 24
    print(i)
print()

for char in "Logirobi": # char = L, o, g, i, r, o, b, i
    print(char)

print()
lista = [5, "alma", True, 3.14, 8, "banán"]
for item in lista: # item = 5, alma, True, 3.14, 8, banán
    print(item)


lista = [3, 9, 1, 8, 1, 12, 0, 6, 4, 8]
print(lista[3]) # 8
print(lista[2:7]) # [1, 8, 1, 12, 0] A 7. index már nincs benne!
print(lista[:7])  # [3, 9, 1, 8, 1, 12, 0] A lista elejétől a 7-ik
print(lista[5:])  # [12, 0, 6, 4, 8] Az 5. indextől a végéig
print(lista[:])   # [3, 9, 1, 8, 1, 12, 0, 6, 4, 8] AZ elejétől a végéig
# feladat: Olvassunk be egy számot, és írjuk ki a szorzótábláját!
# alt gr + Q -> \
num = 7 #int(input("Adj meg egy egész számot!\n"))
for i in range(1, 11):
    print(f"{i} * {num} = {i*num}")

# feladat: Egy adott szöveg kódolása/dekódolás
# a páratlan sorszámú betűket előre tesszük, a párosakat hátra
# Szeretem a cicákat
# Seee  iáazrtmacckt

#Egy adott string kódolása:
szöveg = "Szeretem a cicákat"
kódolt_szöveg = ""
for i in range(0, len(szöveg), 2): # i = 0, 2, 4, 6, 8, ...
    kódolt_szöveg += szöveg[i]

for i in range(1, len(szöveg), 2): # i = 1, 3, 5, 7, 9, ...
    kódolt_szöveg += szöveg[i]

print(kódolt_szöveg)

#Egy adott string dekódolása:
kódolt_szöveg = "Seee  iáazrtmacckt"
dekódolt_szöveg = ""
első_fele = kódolt_szöveg[:(len(kódolt_szöveg)+1)//2] # Az elejétől a feléig
második_fele = kódolt_szöveg[(len(kódolt_szöveg)+1)//2:] #A felétől a végig
for i in range((len(kódolt_szöveg) + 1) // 2):
    dekódolt_szöveg += első_fele[i]
    if i < len(második_fele):
        dekódolt_szöveg += második_fele[i]

print(dekódolt_szöveg)


#Listák generálása:
#Generáljunk egy listát amiben a számok 0-tól 49-ig szerepelnek
lista = []
for i in range(50):
    lista.append(i)
print(lista)

#Generáljunk egy listát amiben a számok 9-től 19-ig mennek
lista = []
for i in range(9, 20):
    lista.append(i)
print(lista)

#Generáljunk egy listát amiben a számok 7-től -20-ig szerepelnek
lista = []
for i in range(7, -21, -1):
    lista.append(i)
print(lista)

#List comprehension
lista = [0 for i in range(5)] # [0,0,0,0,0]
print(lista)
lista = [i for i in range(5)] # [0,1,2,3,4]
print(lista)
lista = [i*i + 3*i - 7 for i in range(-10, 11)]
print(lista)

#x^2 - 2x + 1
lista = [i**2 - 2*i + 1 for i in range(-10, 11)]
print(lista)

# Feladat: Olvassunk be egy nevet és döntsük el, hogy szerepel-e egy listában

nevek = ["Anna", "Béla", "Cecil", "Dávid", "Elemér", "Ferenc"]
print(nevek)
név = input("Adj meg egy nevet és megnézem, hogy szerepel-e a listában!\n")
találat = False
for i in range(len(nevek)):
    if név.lower() == nevek[i].lower():
        találat = True

if találat:
    print("Szerepel a listában")
else:
    print("Nem szerepel a listában")

"""
if név in nevek:
    print("Szerepel a listában")
else:
    print("Nem szerepel a listában")
"""











