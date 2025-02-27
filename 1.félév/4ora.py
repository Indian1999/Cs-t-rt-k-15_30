print("Hello World")
#input() # Beolvasás, mindig stringet ad vissza

név = "Kis Pista" # string
print(type(név))
print(type(5))

#Alap típusok:
#string     -   szöveg
#int        -   egész szám
#float      -   nem egész szám
#bool       -   logikai érték

if név == "Kis Pista":
    print("Szia Pista!")
else:
    print("Ki te vagy?")

#Operátorok:
#Aritmetikai operátorok (+, -, *, /, %, //, **)
print(4 + 9)    # 13
print(15 - 3)   # 12
print(3 * 5)    # 15
print(12 / 3)   # 4.0 (float érték) osztás eredménye mindig float lesz
print(9 / 4)    # 2.25
print(9 % 4)    # 1 megnézi hogy mennyi az osztási maradék (int)
print(9 // 4)   # 2 megadja, hogy hány egészszer van meg benne (int)
print(2 ** 10)  # 2^10 = 2*2*2*2*2*2*2*2*2*2 = 1024

#Értékadó operátorok (=, +=, -=, *=, /=, //=, %=, **=)
num = 8 #Létrehoz egy num nevű változót és az értékét 8-ra állítja
print(num) # 8
num += 7 #num változó értékéhez hozzáad 7-et
print(num) # 15
num -= 3
print(num) # 12
num *= 2
print(num) # 24
num /= 2
print(num) # 12.0 (innentől a num az egy float lesz)
num //= 5
print(num) # 2.0
num **= 10
print(num) #1024.0
num %= 100
print(num) #24.0

#Összehasonlító operátork (>, <, >=, <=, ==, !=)
#Az eredményük igaz vagy hamis (True/False)

print(5 > 3)  #True
print(9 <= 5) #False
print(9 == 8) #False
print(4*5 == 20) #True
print(5 != 9) #True

#Logikai operátorok (and, or, not)
barna_szemű = True
magas = False
print(barna_szemű and magas) #False      (js-ben &&)
print(barna_szemű or magas)  #True       (js-ben ||)
print(not magas) #True                   (js-ben ! )

#Az in operátor
print("a" in "almafa") # (True) Megnézi, hogy az a betű benne-e van az almafa szóban
print("cica" in "almafa") #False
print("cica" in "cicakaparófa") #True

#Feladat:
# Olvassunk be 3 egész számot és döntsük el, hogy melyik a legnagyobb
# alt gr + Q -> \
# \n az entert jelenti
a = int(input("Add meg az 1. számot:" + "\n"))
b = int(input("Add meg a 2. számot:\n"))
c = int(input("Add meg a 3. számot:\n"))

if a >= b and a >= c:
    print("A legnagyobb szám: " + str(a))
elif b >= a and b >= c:
    print("A legnagyobb szám: " + str(b))
else:
    print("A legnagyobb szám: " + str(c))

szöveg = "cica"
print(szöveg.capitalize())
print(szöveg.upper())
mondat = "a cica nagyon szereti a marhahúst"
print(mondat.title())



