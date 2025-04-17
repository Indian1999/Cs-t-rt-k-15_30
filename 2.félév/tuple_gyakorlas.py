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


# 4. feladat: Írjuk ki, a legjobb a legrosszabb eredményt
        