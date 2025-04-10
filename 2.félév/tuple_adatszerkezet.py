# A tuple szinte ugyan az mint a lista, a fő különbség, hogy a tuple az nem módosítható

myTuple = (5, 2, 3)
print("myTuple:", myTuple)
print("type(myTuple):", type(myTuple)) # <class 'tuple'>
print("myTuple[1]:", myTuple[1]) # 2

# A tuple adatszerkezet NEM módosítható
#myTuple[0] = 10
#Exception has occurred: TypeError
#'tuple' object does not support item assignment

# Ha egyszer létrehoztuk, akkor már nem lehet átírogatni

# Ez így működik, de fontos megérteni, hogy itt nem módosítjuk a tuple-t, 
# hanem újradefiniáljuk (Az eddigi értékét töröljük, és adunk neki egy teljesen újat)
myTuple = (10, 2, 3)
print(myTuple)

# Elemet sem tudunk hozzáadni/törölni
# myTuple.append(4) HIBA

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

one_element_tuple = (5)        
print(one_element_tuple)        # 5
print(type(one_element_tuple))  # <class 'int'>

# Amit várnánk: hogy létrejön egy 1 elemű tuple
# Ami történik, hogy integer lesz a változó tuple helyett
# Ez azért történik mert a (5) kifejezést aritmetikai kifejezésként értelmezi a python

# Ha egy 1 elemű tuple-re van szükségünk:
one_element_tuple = (5,)   # <--- VESSZŐ     
print(one_element_tuple)        # (5,)
print(type(one_element_tuple))  # <class 'tuple'>


# A típusok egy tuple objektumon belül szabadon keverhetők
myTuple = (5, "kiscica", True, 3, 3.67, True, (1,2,3), [5, 9, 1, 2], False)
print(myTuple)

# Tuple comprehension
myTuple = tuple(i for i in range(1, 10))
print(myTuple)

# Operátorok a tuple-re

# Két tuple akkor egyenlő, ha az elemeik rendre megegyeznek
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = (3,1,2)
tuple4 = (4,5,6)
print(tuple1 == tuple2) # False
print(tuple1 == tuple3) # False
print(tuple2 == tuple4) # True

print("tuple1 * 3 =", tuple1 * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
#print("tuple1 + 3 =", tuple1 + 3) # TYPE ERROR - int-et nem adhatok hozzá tuplehöz
print("tuple1 + tuple2 =", tuple1 + tuple2) # (1, 2, 3, 4, 5, 6)

def minimum(lista):
    min_index = 0
    for i in range(len(lista)):
        if lista[i] < lista[min_index]:
            min_index = i
    return (lista[min_index], min_index) # tuple

lista = [9, 2, 1, 6, -2, 6, -5, 6, 9, 1]

legkisebb = minimum(lista)
print(legkisebb) # (-5, 6)

min_value, min_index = minimum(lista)
print(min_value) # -5
print(min_index) # 6


import random
# 1. feladat: Szerepel-e a tuple-ben a 7-es szám?
myTuple = tuple(random.randint(1, 10) for i in range(5))
print(myTuple)
if 7 in myTuple:
    print("Szerpel benne 7-es.")
else:
    print("Nem szerepel benne 7-es.")

# 2. feladat: Határozzuk meg a tuple elemeinek összegét
összeg = 0
for item in myTuple:
    összeg += item
print("Az elemek összege:", összeg)

# 3. feladat: Töröljük a listából azokat az elemeket amik nem tuple-ök
lista = [5, (3, 2, 1), 4.13, ("asd", "fa"), "cica", True, None, (1, "egy almafa")]
new_lista = []
for i in range(len(lista)):
    if type(lista[i]) == tuple:
        new_lista.append(lista[i])
lista = new_lista.copy()
print(lista)

# 4. feladat: Határozzuk meg a tuple elemeinek az átlagát
myTuple = ((1,2,3), (43, 13), (9, 3, 8), (20, 40, 60))
print(myTuple)

összeg = 0
darab = 0
for i in range(len(myTuple)):
    for j in range(len(myTuple[i])):
        összeg += myTuple[i][j]
        darab += 1
        
print("Az elemek átlaga:", round(összeg / darab, 2))

# 5. feladat: Fordítsuk meg a tuple elemeit
myTuple = (5, 7, 8, 9, 3, 7) # -> (7, 3, 9, 8, 7, 5)

new_tuple = []
for i in range(len(myTuple)-1, -1, -1):
    new_tuple.append(myTuple[i])
new_tuple = tuple(new_tuple)
print(new_tuple)

new_tuple = new_tuple[::-1]
print(new_tuple)

# 6. feladat: Ugyan ennek a tuple-nek vágjuk le az első és utolsó elemét, 
# majd mentsük el egy új tuple-be (7, 8, 9, 3)

new_tuple = myTuple[1:-1]
print(new_tuple)

# 7. feladat: Határozzuk meg, hogy egy tuple-ben melyik indexen található 
# az első 2 jegyű szám
myTuple = (4, 8, 9, 123, 7, 12, 8) # -> 5. index
i = 0
while i < len(myTuple):
    if myTuple[i] >= 10 and myTuple[i] <= 99:
        break
    i += 1
if i == len(myTuple):
    print("Nincs benne kétjegyú szám.")
else:
    print(f"Az első kétjegyű szám a {i}. indexen található.")

# 8. feladat: Számoljuk ki vektorok műveletének eredményét
a = (3, 5)
b = (-1, 3)
c = (2, -1)
# Határozzuk meg az    a + 2b - 3c vektort
# (3,5) + 2 * (-1,3) - 3 * (2, -1) = (3,5) + (-2, 6) - (6, -3) = (-5, 14)

v = (a[0] + 2 * b[0] - 3 * c[0], a[1] + 2 * b[1] - 3 * c[1])
print(v)