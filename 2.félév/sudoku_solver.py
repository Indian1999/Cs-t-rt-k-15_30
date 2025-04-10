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
        
def find_empty():
    """
    Visszaadja a legelső üres cella sor-oszlop indexét
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j) # 2 elemeű tuple, a sor és oszlop indexekkel.
       
def is_valid(num: int, pos: tuple) -> bool:
    """
    Megnézi, hogy amennyiben a num-ot beírnánk az adott pozícióra, akkor valid marad-e a tábla. True vagy False értékkel tér vissza.
    """ 
    #Sor ellenőrzése:
    for j in range(9):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    #Oszlop ellenőrzése:
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #A kis négyzet ellenőrzése:
    box_x = pos[1] // 3 * 3
    box_y = pos[0] // 3 * 3
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve():
    empty = find_empty()
    if empty == None:
        return True
    else:
        row, col = empty
    for num in range(1, 10):
        if is_valid(num, empty):
            board[empty[0]][empty[1]] = num
            if solve():
                return True
            board[empty[0]][empty[1]] = 0
    return False

# A játékos kiválaszthat egy cellát, és arra a cellára beírhat egy számot
# (bónusz) Ez megy egészen addig, amíg készen nem lesz a sudoku (Ehez egy új függvény is kéne)
# A játékosnak ajánljuk fel minden lépésnél, hogy szabad-e a gazda, ilyenkor a szg. kitölti a sudokut

def completed():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return False
    if not is_valid(board[0][0], (0,0)):
        return False
    return True

gameOn = True
while gameOn:
    print_board()
    bemenet = input("Adj meg 3 számot! (sor, oszlop, szám), ha szabad a gazda: solve\n")
    if bemenet == "solve":
        solve()
        gameOn = False
    else:
        bemenet_split = bemenet.split(" ") # ["2", "3", "1"]
        sor = int(bemenet_split[0]) - 1
        oszlop = int(bemenet_split[1]) - 1
        num = int(bemenet_split[2])
        board[sor][oszlop] = num
        if completed():
            gameOn = False
            print("Szép volt!")
        
print_board()
        