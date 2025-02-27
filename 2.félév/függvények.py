# Függvények
# () - zárójelek a nevük után
# Ha meghívunk egy függvényt, akkor a függvényben definiált kód lefut

#Függvény definiálás:
def say_hi():
    print("#######")
    print("# HI! #")
    print("#######")
    print()

say_hi()

#Függvény paraméterek: (zárójelbe írt rész)
def say_hi_to(name):
    print(f"Hi {name}!")

say_hi_to("Ádam")
say_hi_to("András")
say_hi_to("Béla")

def say_time_hi_to(name, time):
    if time == 1:
        print(f"Jó reggelt {name}!")
    elif time == 2:
        print(f"Jó napot {name}!")
    elif time == 3:
        print(f"Jó estét {name}!")
    else:
        print(f"Szia {name}!")

say_time_hi_to("András", 1)
say_time_hi_to("Béla", 2)
say_time_hi_to("Cecil", 3)
say_time_hi_to("Dénes", 4)

# Függvények visszatérési értékkel
def linear_func(x):
    return 2*x - 3

print(linear_func(3))
print(linear_func(4))
print(linear_func(5))

def add(a, b):
    return a + b

print(add(3,8))

# Derékszögű háromszög-e? Ha bármely két oldalának négyzetösszege, egyenlő a harmadik oldal négyzetével
# 2**4 = 2 a 4. hatványon (2*2*2*2)
def is_right_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    return False
    
print(is_right_triangle(3,4,5))
print(is_right_triangle(6,4,3))
#Ha nincs visszatérési érték akkor None-t ad vissza
# Ha egy függvény returnhöz ér, akkor abbahagyja a futását
def func():
    print("Szia!")
    return 1
    print("Hello!") # Ez már nem fog lefutni, mert a returnnél megáll a függvény

func()

#prím szám - csak 1-el és önmagával osztható (Az 1 az nem prím)
def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num): #i = 2, 3, 4, ...., num - 1
        if num % i == 0:
            return False
    return True

print(isPrime(0))
print(isPrime(1))
print(isPrime(2))
print(isPrime(4))
print(isPrime(7))
print(isPrime(63))

# A függvény definíciókor zárójelbe írt értékeket paramétereknek nevezzük
# A függvény hívásakor zárójelbe írt értékeket argumentumoknak nevezzük

def param(ez_a_fgv_paramétere): #Paraméter
    print(ez_a_fgv_paramétere)

param("Ez a függvény argumentuma") # argumentum (argument)

#Kulcsszavas paraméterek:
def is_right_triangle2(befogo1, befogo2, atfogo):
    if befogo1**2 + befogo2**2 == atfogo**2:
        return True
    return False

print(is_right_triangle2(atfogo=10, befogo2=6, befogo1=8))
print(is_right_triangle2(8,6,10))

print("alma", "banán", "citrom", sep=", ", end="\n" + "#"*20 + "\n")

#A változók látótere (hatóköre)
#A függvényeken belül létrehozott változók csak a függvényen belül léteznek
def func_num():
    x = 10
    print(x)

x = 20
print(x)    #20
func_num()  #10
print(x)    #20

# 1. feladat: Írjunk egy függvényt ami eldönti egy paraméterben megkapott számról, hogy páros vagy páratlan
# A függvény egy logikai értéket (bool) adjon vissza
def isEven(num):
    return num % 2 == 0

print("isEven()")
print(isEven(3))
print(isEven(8))
# 2. feladat: Írjunk egy függvényt ami egy paraméterben megkapott listáról eldönti és visszaadja
# a listában található elemek összegét
def sumList(lista):
    összeg = 0
    for item in lista:
        összeg += item
    return összeg

print("sumList()")
print(sumList([1,2,3,4,5]))
# 3. feladat: Írjunk egy függvényt ami egy paraméterben megkapott stringről meghatározza, hogy hány magánhangzó
# van benne. Ezt az érték adja vissza

def countVowels(word):
    counter = 0
    vowels = "aeiouéáőúűóüöAEIOUÉÁŐÚŰÓÜÖ"
    for char in word:
        if char in vowels:
            counter += 1
    return counter

print("countVowels()")
print(countVowels("Indul a görög aludni"))
# 4. feladat: Írjunk egy függvényt ami egy paraméterben megkapott Celsius hőfokot átvált Fahrenheit-re.
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# 5. feladat: Írjunk egy függvényt ami egy paraméterben megkapott Fahrenheit hőfokot átvált Celsius-ra.
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(f"50 C° = {celsius_to_fahrenheit(50)} F°") # alt gr + 5 (kétszer kell megnyomni az 5-t)
print(f"100 C° = {celsius_to_fahrenheit(100)} F°")
print(f"32 F° = {fahrenheit_to_celsius(32)} C°")
print(f"100 F° = {round(fahrenheit_to_celsius(100),1)} C°")
print(f"0 F° = {round(fahrenheit_to_celsius(0),1)} C°")

