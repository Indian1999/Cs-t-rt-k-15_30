import random
#Mai óra tartalma az elől tesztelős ciklusok (while)

num = 1
while num <= 5:
    print(num)
    num += 1

#Számoljuk meg egy szám számjegyeinek a számát

num = 592862347
számláló = 0
while num != 0:
    num //= 10
    számláló += 1
print("Számjegyek száma:", számláló)

#feladat:
# Bizonyos elemig írjuk ki a fibonacci számokat
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ....

counter = 10
num1 = 0
num2 = 1
print("A fibonacci sorozat:")
while counter > 0:
    print(num1)
    summa = num1 + num2
    num1 = num2
    num2 = summa
    counter -= 1

# Írjuk ki a prím számokat 1-100-ig
# Prímszám: csak 1-gyel és önmagával osztható (Az 1 az nem prím szám)
num = 2
while num <= 100:
    isPrime = True
    osztó = 2
    while osztó < num:
        if num % osztó == 0:
            isPrime = False
        osztó += 1
    if isPrime:
        print(num)
    num += 1

#Gondoltam egy számra játék:
"""
num = random.randint(1, 100) # 1 és 100 között generál egy random számot!
guessCount = 0
guess = 0
while guessCount < 10 and guess != num:
    guess = int(input("Tippelj egy számot!\n")) #alt gr + Q -> \
    if guess > num:
        print("Ettől kisebbre gondoltam")
    elif guess < num:
        print("Ettől nagyobbra gondoltam")
    guessCount += 1
if guess == num:
    print("Szép volt! Eltaláltad!")
else:
    print("Ez most nem jött össze, a megoldás a " + str(num) + " volt.")
    """

for i in range(10): # i = 0, 1, 2, 3, ..., 8, 9
    print(i)

for i in range(10, 20): # i = 10, 11, 12, ..., 18, 19
    print(i)

for i in range(100, 9500, 1000): # 100, 1100, 2100, 3100, ..., 9100
    print(i)

lista = [5, 8, 1, 7, 9]
print(lista)
lista.append(11) # 11-et hozzáfűzi a lista végére
print(lista)
lista.pop(2)
print(lista)
print(lista[3])
lista.remove(9) # A 9-es számot törli a listából
print(lista)

összeg = 0
for i in range(len(lista)):
    összeg += lista[i]
print(összeg)

szorzat = 1
for i in lista: # i = lista[0], lista[1], lista[2], ... egészen a lista végéig
    szorzat *= i

print(szorzat)



