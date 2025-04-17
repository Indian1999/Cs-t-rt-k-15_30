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
        