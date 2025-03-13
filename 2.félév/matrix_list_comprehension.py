import random
import matplotlib.pyplot as plt
import numpy as np

def generate_2d_matrix(n:int, m:int) -> list[list[int]]:
    """
    This function returns an n x m matrix filled with zeros.
    Args:
        n (int): Defines the amount of rows the matrix will have (n > 0)
        m (int): Defines the amount of columns the matrix will have (m > 0)
    """
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        matrix.append(row)
    return matrix

matrix = generate_2d_matrix(3,8)
for row in matrix:
    print(row)
    
    
matrix = [[random.randint(-20, 100) for j in range(8)] for i in range(5)] 
for row in matrix:
    print(row)
    
összeg = 0
for i in range(len(matrix)): # sorok számáig megy
    for j in range(len(matrix[i])): # oszlopok számáig
        összeg += matrix[i][j]
print("A mátrix elemeinek az összege:", összeg)

# 1. feladat: Írjuk ki a legkisebb számot a mátrixban
minimum = matrix[0][0]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < minimum:
            minimum = matrix[i][j]
print("A legkisebb szám a mátrixban:", minimum)

# 2. feladat: Adjuk meg, hogy hány negatív szám van a mátrixban
neg_counter = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            neg_counter += 1
print("A negatív számok darabszáma:", neg_counter)
    
# List comprehension

lista = [0 for i in range(10)]
print(lista)
lista = [i for i in range(10)]
print(lista)
lista = [i**2 -4*i + 2 for i in range(10)]
print(lista)
lista = [[] for i in range(10)]
print(lista)
lista = [[j*i for j in range(3)] for i in range(3)]
print(lista)

dice_matrix = [[i + j for j in range(1,7)] for i in range(1, 7)]
for row in dice_matrix:
    print(row)
    
# 4 dobókockával dobunk egyszerre
# Mennyi a valószínűsége, hogy a dobás eredménye 7?

four_dice = [[[[i+j+k+l for l in range(1,7)] for k in range(1,7)] for j in range(1,7)] for i in range(1,7)]

counter= 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                if four_dice[i][j][k][l] == 7:
                    counter += 1
összes = 6**4
#Valószínűség = kedvező/összes
# Kedvező: a dobások összege: 7
print(f"A 7-es dobásának valószínűsége 4 dobókockával: {round(counter/összes, 4) * 100}%")     

x = np.array([i for i in range(4, 25)])
y = []
for num in x:
    counter= 0
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    if four_dice[i][j][k][l] == num:
                        counter += 1
    összes = 6**4  
    y.append(counter/összes)
y = np.array(y)
y = 100 * y
plt.bar(x, y)
plt.xlabel("4 dobás összege")
plt.ylabel("Százalék")
plt.xlim([3.5, 24.5])
plt.xticks(x)
plt.grid()
plt.show()

    