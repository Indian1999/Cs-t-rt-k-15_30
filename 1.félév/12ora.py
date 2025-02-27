import random
lista = []
for i in range(20):
    lista.append(random.randint(-10, 10))
print(lista)
# 15:55
# 1. feladat: Számoljuk meg a páros, páratlan, poz, neg, nulla számokat egy listában
paros = 0
ptlan = 0
poz = 0
neg = 0
nulla = 0
for num in lista:
    if num % 2 == 0:
        paros += 1
    else:
        ptlan += 1
    if num > 0:
        poz += 1
    elif num < 0:
        neg += 1
    else:
        nulla += 1
print(f"Páros: {paros}\nPáratlan: {ptlan}\nPozitív: {poz}\nNegatív: {neg}\nNulla: {nulla}")
    
# 16:00
# 2. feladat: A legnagyobb különbséget kell megkeresni két szám között (max-min)
maxi = lista[0]
mini = lista[0]
for item in lista:
    if item > maxi:
        maxi = item
    if item < mini:
        mini = item

print(f"Minimum: {mini}, Maximum: {maxi}, A kettő különbsége: {maxi-mini}")
# 16:10
# 3. feladat: Töröljük a duplikációkat a listából (minden elem csak 1-szer szerepelhet)
print(lista)
egyedi_lista = []
for i in range(len(lista)):
    if lista[i] not in egyedi_lista:
        egyedi_lista.append(lista[i])
lista = egyedi_lista[:]
print(lista)

# 16:20
# 4. feladat: Találjuk meg, a második legnagyobb számot a listában
seged_lista = lista[:]
seged_lista.remove(max(seged_lista))
masodik_legnagyobb = max(seged_lista)
print("A második legnagyobb szám:", masodik_legnagyobb)

# 16:30
# 5. feladat: Rendezzük a listát
for i in range(len(lista)):
    for j in range(len(lista) -i - 1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)
# 6. feladat: Az extend függvény
lista = []
lista2 = [1,3,4,5]
lista3 = [9, 2, 8, True]
lista.extend(lista2)
lista.extend(lista3)
print(lista)
# 7. feladat: Válogassuk ki az inteket egy vegyes listából
lista = [3, "alma", True, 4.12, 8, 9, False, [1,2,3], "cica", 12, 9.4]
int_lista = []
for item in lista:
    if type(item) == int:
        int_lista.append(item)
print(int_lista)
# 8. feladat: Találjuk meg két lista közös elemeit
lista1 = []
for i in range(20):
    lista1.append(random.randint(-20,20))

lista2 = [random.randint(-20,20) for i in range(20)]
print(lista1)
print(lista2)
közös_lista = []
for item in lista1:
    if (item in lista2) and (item not in közös_lista):
        közös_lista.append(item)

print(közös_lista)
# 9. feladat: Egy lista elemeiből készítsünk számot
# pl.: [23, 14, 2, 91] -> 2314291
lista = [23, 14, 2, 91]
num_string = ""
for item in lista:
    num_string += str(item)
num = int(num_string)
print(num)