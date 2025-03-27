board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board():
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- " * 12)
        output = ""
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                output += " | " #alt gr + w -> |
            output += str(board[i][j]) + " "
        print(output)
        
        
print_board()