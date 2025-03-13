import random

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

# 2. feladat: Adjuk meg, hogy hány negatív szám van a mátrixban
    

    