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