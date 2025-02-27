import random

# 1. feladat: Két listát tegyünk ugyan olyanná
# (Hogyha egy listából hiányzik egy elem ami a másik listában benne van, akkor rakjuk bele)
lista1 = [random.randint(-10, 10) for i in range(10)]
lista2 = [random.randint(-10, 10) for i in range(10)]
print(lista1)
print(lista2)

for item in lista2:
    if item not in lista1:
        lista1.append(item)

for item in lista1:
    if item not in lista2:
        lista2.append(item)

lista1.sort() # Rendezi a listát
lista2.sort()
lista1 = list(set(lista1)) # Kiszedi a duplikációkat
lista2 = list(set(lista2))
print(lista1)
print(lista2)

# 2. feladat: Boltban kapható áruk
items = ["alma", "kenyér", "szalámi", "vaj", "ásó", "traktor", "fánk", "wc papír", "zokni", "sajt", "csoki"]
prices =[130,     540,      360,       860,   3500,  120000,    120,    1200,       500,     3200,   400]

# a, Írjuk ki azoknak a termékeknek a nevét, amik kevesebb, mint 800 Ft-ba kerülnek
for i in range(len(prices)):
    if prices[i] < 800:
        print(items[i])

# b, Mennyibe kerülne, ha minden 1000 Ft-nál olcsóbb terméket megvennénk?
összeg = 0
for item in prices:
    if item < 1000:
        összeg += item
print("Az 1000 Ft-nál olcsóbb termékek árának az összege:", összeg)

# c, Írjuk ki azokat a termékeket és az árukat, amik 300Ft-nál drágábbak, de 2000 Ft-nál olcsóbbak
for i in range(len(prices)):
    if prices[i] > 300 and prices[i] < 2000:
        print(f"{items[i]} - {prices[i]} Ft")
        

# d, Mennyibe kerül 1 db ásó?
index = 0
for i in range(len(items)):
    if items[i] == "ásó":
        index = i
print(f"1 db ásó ára: {prices[index]} Ft")

# e, Mennyibe kerül 1 db vaj, 1 db fánk?
vaj_index = 0
fánk_index = 0
for i in range(len(items)):
    if items[i] == "vaj":
        vaj_index = i
    if items[i] == "fánk":
        fánk_index = i
print(f"1 db vaj ára: {prices[vaj_index]} Ft")
print(f"1 db fánk ára: {prices[fánk_index]} Ft")

items = ["alma", "kenyér", "szalámi", "vaj", "ásó", "traktor", "fánk", "wc papír", "zokni", "sajt", "csoki"]
prices =[130,     540,      360,       860,   3500,  120000,    120,    1200,       500,     3200,   400]

# 16:25
# f, Mennyit fizetünk a boltban, ha veszünk:
#       4 db szalámit
#       1 db vajat
#       2 db zoknit
#       1 db sajtot
#       3 db csokit
vaj_index = 0
szalámi_index = 0
zokni_index = 0
sajt_index = 0
csoki_index = 0
for i in range(len(items)):
    if items[i] == "vaj":
        vaj_index = i
    if items[i] == "szalámi":
        szalámi_index = i
    if items[i] == "zokni":
        zokni_index = i
    if items[i] == "sajt":
        sajt_index = i
    if items[i] == "csoki":
        csoki_index = i
végösszeg = 4 * prices[szalámi_index] + 1 * prices[vaj_index] + 2 * prices[zokni_index] + 1 * prices[sajt_index] + 3 * prices[csoki_index] 
print(f"Végösszeg = {végösszeg} Ft") # 7700 Ft

#16:35
# g, Átlagosan mennyibe kerül egy termék?
összeg = 0
for item in prices:
    összeg += item
print(f"Az összes termék árának az átlaga: { round(összeg / len(prices)) } Ft") #11892 Ft

#16:45
# h, Írjuk ki a legdrágább terméket és az árát is!
max_index = 0
for i in range(len(prices)):
    if prices[i] > prices[max_index]:
        max_index = i
print(f"A legdrágább termék: {items[max_index]} - {prices[max_index]} Ft")
# i, Írjuk ki a legolcsóbb terméket és az árát is!
min_index = 0
for i in range(len(prices)):
    if prices[i] < prices[min_index]:
        min_index = i
print(f"A legolcsóbb termék: {items[min_index]} - {prices[min_index]} Ft")

# 16:52
# j, Ha a traktort nem nézzük, mennyi a termékek átlagára?
összeg = 0
for i in range(len(prices)):
    if items[i] != "traktor":
        összeg += prices[i]

átlag = összeg / (len(prices) - 1)
print(f"A traktort nem számítva a termékek átlagára: { round(átlag) } Ft") #1081 Ft

# k, Írjuk ki azokat a termékeket és az árukat amik olcsóbbak a j feladatban kiszámolt értéknél
print("Ettől az átlagtól olcsóbb termékek")
for i in range(len(prices)):
    if prices[i] < átlag:
        print(f"{items[i]} - {prices[i]} Ft")

