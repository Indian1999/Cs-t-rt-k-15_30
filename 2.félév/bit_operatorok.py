# 2-es számrendszer (Egy számjegy 2 különböző érték lehet 0, 1)
# 10010111011011

# Hétköznapokban 10-es számrendszert használunk (19, 32, 334, stb.)
# egy számjegy 10 különöző értéket vehet fel (0-9)

binary = bin(54) 
print(binary)           # 0b110110 - a 0b jelzi, hogy 2-es számrendszer
print(type(binary))     # <class 'str'>
# Gyakran kellhet, hogy 0b nélkül jelenítsük meg a számot
print(binary[2:])       # 110110

binary = input("Adj meg egy 2-es számrendszer-beli számot!\n")
decimal = int(binary, 2)
print(decimal)

# 16-os számrendszer
# A számjegyek helyén szerepelhetnek betűk is
# 16 különböző értéke lehet egy számjegynek (0-9, A-F)
# A: 10, B: 11, C:12, D:13, E: 14, F: 15

#Hol használjuk a 16-os számrendszert?
# IPv6 címeknél
# RGB (színek) #FF1020 (piros)
# MAC címeknél # 9F-2C-4C-48-6A-44 (szg. fizikai címe)
# 9F - 1001 1111
# Memóriacímzés: 0x0000022D0A49FE10

class Valami():
    pass

valami = Valami()
print(valami)

# Miért szeretjük? mert 2 hatvány a 16
# 2-es és 16 os számrendszer között, könnyű az átváltás
# 11100011 -> E3


hexa = input("Adj meg egy 16-os számrendszer-beli számot!\n")
decimal = int(hexa, 16)
print(decimal)

# Hearthstone-ban ha egy minion élete 2 147 483 648 fölé megy, akkor meghal
# Ennek az az oka, hogy a minion élete egy 32 bites integer



