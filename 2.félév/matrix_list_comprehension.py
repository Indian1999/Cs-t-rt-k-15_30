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
    

    