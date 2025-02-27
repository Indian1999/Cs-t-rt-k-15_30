nevek = ["András", "Béla", "Cecil", "Dominik", "Elemér", "Ferenc"]
print(nevek)
print(type(nevek))
print("A lista hossza:", len(nevek))

#A listákat 0-tól indexeljük
print(nevek[0]) #András
print(nevek[4]) #Elemér
print(nevek[5]) #Ferenc
print(nevek[-2]) # Hátulról a 2. elem (Elemér)
print(nevek[-4]) # Cecil

index = int(input("Adj meg egy indexet!\n"))
if index < len(nevek) and index >= -len(nevek):
    print(nevek[index])
else:
    print("Nincs ilyen index!")

#Írjuk ki a lista összes elemét!

print("####################")
i = 0
while i < len(nevek):
    print(nevek[i])
    i += 1
print("####################")
print("# For ciklussal: #")

for i in range(len(nevek)): # i = 0, 1, 2, 3, 4, 5
    print(nevek[i])

print("####################")
print("# For ciklussal 2: #")

for név in nevek: # név = András, Béla, Cecil, Dominik, Elemér, Ferenc
    print(név)
print("####################")

#Hozzunk létre egy listát ami a számokat tartalmazza 1-től 50-ig

számok = []
for i in range(1, 51): #i = 1, 2, 3, ..., 50
    számok.append(i)
print(számok)

#Hozzunk létre két új listát ami a páros és páratlan számokat tarlmazza 1-től 20-ig

paros_lista = []
ptlan_lista = []
for i in range(1, 21):
    if i % 2 == 0:
        paros_lista.append(i)
    else:
        ptlan_lista.append(i)

print(paros_lista)
print(ptlan_lista)

# Cseréljünk meg két elemet egy listában!
print("Elemek megcserélése, ebben a listában:", paros_lista)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

temp = paros_lista[3] #8
paros_lista[3] = paros_lista[4] # [2, 4, 6, 10, 10, 12, 14, 16, 18, 20]
paros_lista[4] = temp           # [2, 4, 6, 10, 8, 12, 14, 16, 18, 20]

print(paros_lista)

paros_lista[5], paros_lista[8] = paros_lista[8], paros_lista[5]
print(paros_lista)

# az insert(index, érték) függvény
paros_lista.insert(4, 50)
#a 4. indexre behelyzi az 50-et, minden ami ettől a ponttól volt, eggyel hátrébb kerül
print(paros_lista)
paros_lista.insert(0, 0)
paros_lista.insert(9438, 100)
print(paros_lista)

# lista.pop(index) - törli az adott indexen lévő elemet

paros_lista.pop(10) # A 10. elemet kiszedi a listából
print(paros_lista)

# lista.remove(érték) - törli a listából az adott értékű elemet

paros_lista.remove(20) # A 20-as értéket kiveszi a listából
print(paros_lista)

#Feladat: Határozzuk meg a páros lista elemeinek az összegét!

összeg = 0
for item in paros_lista:
    összeg += item
print("A páros lista elemeinek az összege:", összeg)

# Feladat: Határozzuk meg, hogy hányszor szerepel egy adott elem a listában!

lista = [1,0,1,2,2,1,0,1,2,2,1,0,1,2,0,1,2,1,0,2,2,2,1,1,1,0,1,1,0,1,2]
print(lista)
keresendo = int(input("Adj meg egy számot a listából!\n"))
számláló = 0
for item in lista:
    if item == keresendo:
        számláló += 1

print(f"A(z) {keresendo} érték {számláló} alkalommal szerepel a listában!")