import random
puzzles = ["finding nemo", "lion king", "frozen", "despicable me", "incredibles"]
puzzle = puzzles[random.randrange(0, len(puzzles))]
my_solution = ""
for char in puzzle:
    if char == " ":
        my_solution += " "
    else:
        my_solution += "*"
life = 10
correct_letters = []
wrong_letters = []
while life > 0 and my_solution != puzzle: # Amíg tart a játék
    print(my_solution)
    char = input("Tippelj egy betűt!\n").lower() # alt gr + Q -> \
    if len(char) == 1: # Egy betűt írtunk be
        found = False
        for i in range(len(puzzle)): # i = 0, 1, 2, 3, 4, ..., puzzle hossza - 1
            if char == puzzle[i]:
                found = True
                #my_solution[i] = char HIBA string elemét nem tudjuk átírni
                lista = list(my_solution) # "asd" -> ['a', 's', 'd'] -> "['a', 's', 'd']"
                lista[i] = char
                my_solution = "".join(lista)
        if found:
            correct_letters.append(char)
        else:
            wrong_letters.append(char)
            life -= 1
            print(f"Sajnos ez a betű nem szerepel a feladványban, még {life} életed maradt.")
        print("Kitalált betűk:", correct_letters)
        print("Rossz betűk:", wrong_letters)
    else:               # Ekkor a játékos tippelt a megoldásra
        if char == puzzle:
            print("Eltaláltad!")
            my_solution = char
        else:
            life -= 1
            print(f"Nem ez a megoldás! Még {life} életed maradt!")

#Ezen a ponton kiléptem a ciklusból -> vagy az élet fogyott el, vagy kitaláltuk
if life > 0:
    print("Gratulálok!")
else:
    print("Talán legközelebb...")

print("Megoldás:", puzzle)



