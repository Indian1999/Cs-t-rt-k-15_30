import random

#list comprehension
lista = [0 for i in range(10)]
print(lista)
lista = [1 for i in range(10)] + [2 for i in range(12)]
print(lista)
lista = [i for i in range(1, 11)]
print(lista)
lista = [i*i for i in range(1, 11)]
print(lista)

lista = [random.randint(-10, 10) for i in range(10)]
print(lista)

# Legyen egy listánk ami 73-mal osztható számokat tartalmazza 12340-től 13170-ig
lista = [i for i in range(12340, 13171) if i % 73 == 0]
print(lista)

# feladat: Számoljuk meg a páros, páratlan, negatív, pozitív, nulla számokat egy listában
lista = [random.randint(-50, 50) for i in range(20)]
paros = 0
ptlan = 0
poz = 0
neg = 0
nulla = 0
for szám in lista:
    if szám % 2 == 0:
        paros += 1
    else:
        ptlan += 1
    if szám > 0:
        poz += 1
    elif szám < 0:
        neg += 1
    else:
        nulla += 1
# \n - enter
# alt gr + Q -> \
print(lista)
print(f"Páros: {paros}\nPáratlan: {ptlan}\nPozitív: {poz}\nNegatív: {neg}\nNulla: {nulla}")



