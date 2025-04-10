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