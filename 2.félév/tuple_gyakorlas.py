import random

százalékok = [random.randint(0, 100) for i in range(30)]

# 1. feladat, a százalékos eredmények mellé, tároljuk az osztályzatot is
eredmények = [] # (százalék, osztályzat)

for item in százalékok:
    if item >= 89:
        eredmények.append((item, 5))
    elif item >= 75:
        eredmények.append((item, 4))
    elif item >= 60:
        eredmények.append((item, 3))
    elif item >= 40:
        eredmények.append((item, 2))
    else:
        eredmények.append((item, 1))
        
print(eredmények)

# 2. a, feladat: Határozzuk meg az százalékos eredmények átlagát
# 2. b, feladat: Határozzuk meg az osztályzatok átlagot 
százalék_összeg = 0
osztályzat_összeg = 0
for item in eredmények: # példa: item = (43, 2)
    százalék_összeg += item[0]
    osztályzat_összeg += item[1]
    
print(f"A dolgozatok átlag eredménye: {round(százalék_összeg / len(eredmények), 2)}%")
print(f"Az osztályzatok átlaga: {round(osztályzat_összeg / len(eredmények), 2)}")

# 3. feladat: Számoljuk meg, hogy melyik osztályzatból hány darab született
számláló_lista = ["buffer", 0, 0, 0, 0, 0] # 1-es indexen az 1-eseket számolom

for item in eredmények:
    számláló_lista[item[1]] += 1

print(számláló_lista)
for i in range(1, 6):
    print(f"{i} darabszáma: {számláló_lista[i]}")

# 4. feladat: Írjuk ki, a legjobb a legrosszabb eredményt
min_index = 0
max_index = 0
for i in range(len(eredmények)):
    if eredmények[i][0] > eredmények[max_index][0]:
        max_index = i
    if eredmények[i][0] < eredmények[min_index][0]:
        min_index = i

print(f"A legjobb eredmény: {eredmények[max_index]}")
print(f"A legrosszabb eredmény: {eredmények[min_index]}")

# Kitekintés a max/min függvényekre

lista = [(random.randint(0,100),random.randint(0,100),random.randint(0,100)) for i in range(50)]
print(lista)

def sum_tuple(tup):
    return tup[0] + tup[1] + tup[2]

def polynom_tuple(tup):
    return tup[0]**(11/10) + tup[1] - tup[2]

print(max(lista, key=sum_tuple))
print(max(lista, key=polynom_tuple))
print(max(lista))
        