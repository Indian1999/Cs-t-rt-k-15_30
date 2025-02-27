import math
import random 
"""
# 1. feladat: Számoljuk ki egy kúp térfogatát
# V = (r^2 * pi) * magasság / 3
#r = float(input("radius: "))
#magasság = float(input("magasság: "))
#térfogat = r ** 2 * math.pi * magasság / 3
#print("A kúp térfogata:", round(térfogat, 2), térfogat)

# 2. feladat: Adott két változó, cseréljük meg az értéküket
# a = 25 b = 10
a = 10
b = 25

# 1. megoldás:
temp = a
a = b
b = temp
# 2. megoldás:
a, b = b, a

print(a, b)

# 3. feladat: Van egy listánk, bontsuk fel 2 új listára, az egyikben a páros, a másikban
# a páratlan számok legyenek (szétválogatás tétele)

lista = [23, 12, 11, 0, 6, 3, 12, 14, 25, 22, 23, 20, 1, 92, 9, 7, 4, 6, 23]
paros = [elem for elem in lista if elem % 2 == 0]
paratlan = [elem for elem in lista if elem % 2 != 0]
paros.sort()
paratlan.sort()
print("Párosok:", paros)
print("Páratlanok:", paratlan)
paros = []
paratlan = []
for item in lista:
    if item % 2 == 0:
        paros.append(item)
    else:
        paratlan.append(item)
paros.sort()
paratlan.sort()
print(paros)
print(paratlan)


# 4. feladat:
gyümölcsök = ["eper", "körte", "alma", "dinnye", "mandarin", "narancs", "banán"]
kamra = [10, 8, 7, 2, 12, 15, 5]

# a, Melyik gyümölcsből van a legtöbb?
maxi = 0
for i in range(len(gyümölcsök)):
    if kamra[i] > kamra[maxi]:
        maxi = i
print(gyümölcsök[maxi], kamra[maxi])
# b, Összesen hány darab gyümölcsünk van?
összeg = 0
for item in kamra:
    összeg += item
print("Összesen", összeg, "db gyümölcs van.")
# c, Írjuk ki, hogy milyen gyümölcsöket kell venni (akkor kell venni, ha kevesebb,
# mint 6 db van már csak egy adott gyümölcsből
print("Ezeket kell venni a boltban:")
for i in range(len(kamra)):
    if kamra[i] < 6:
        print(gyümölcsök[i])

# Színözön játék
puzzle = []
while len(puzzle) != 4:
    num = random.randint(1, 9)  # 0
    if str(num) not in puzzle:       # 0 not in ["0", "6"] -> True
        puzzle.append(str(num)) # "0"
puzzle = "".join(puzzle)
#print(puzzle)
tips = 0
gameOn = True

while gameOn:
    tip = input("Adj meg egy négygjegyű számot!\n") #7812
    jo_helyen = 0
    rossz_helyen = 0
    for i in range(len(tip)):
        if tip[i] == puzzle[i]:
            jo_helyen += 1
        elif tip[i] in puzzle:
            rossz_helyen += 1
    tips += 1
    if tip == puzzle:
        gameOn = False
    else:
        print(f"{jo_helyen} db szám van megfelelő helyen.")
        print(f"{rossz_helyen} db szám van benne a puzzle-ben, de rossz helyen van.")


print(f"Szép volt! A megoldás: {puzzle}. {tips} lépésből találtad ki!")
"""

# 1. feladat: Határozzuk meg az első x egész szám összegét:
# 10: 1+ 2 + 3 + 4 + 5 + ... + 9 + 10 = 55
n = 10
összeg = 0
for i in range(1, n + 1):
    összeg += i
print(f"Az első {n} pozitív egész szám összege: {összeg}")

# 2. feladat: Határozzuk meg a magánhangzók számát egy szövegben!
szöveg = "The nice banana had a delicious human for lunch." # -> 17 magánhanzó
magánhangzók = "aeiouáéíőúűóüö"
számláló = 0
for char in szöveg:
    if char in magánhangzók:
        számláló += 1
print(f"Ebben a szövegben {számláló} db magánhanzó van")
