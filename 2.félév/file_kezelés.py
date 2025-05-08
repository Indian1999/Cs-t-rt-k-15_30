"""
f = open("input.txt", "r", encoding="utf-8")

print(f.read(50))
print(f.read(10))
f.seek(0)
print(f.read(20))
print(f.read(2000)) # EOF-ig olvas 
# EOF = End Of File

f.seek(0)
szöveg = f.read()
print(szöveg.count(" "))
print(szöveg.count("\n"))
sorok = szöveg.split("\n")
print(sorok)

f.close()

#############################################################

f = open("input.txt", "r", encoding = "utf-8")

sorok = []
for line in f:
    sorok.append(line)
print(sorok)

f.close()

#############################################################

f = open("input.txt", "r", encoding = "utf-8")

sorok = f.readlines()
print(sorok)

f.close()

#############################################################
#                       Fájlba írás                         #
#############################################################

f = open("output.txt", "w", encoding = "utf-8")

f.write("Szia!\n")
f.write("Hello!")

f.close()

# A w mód, az mindig létrehoz egy új fájlt, ha volt már ilyen nevű, akkor törli a tartalmát

f = open("output.txt", "w", encoding = "utf-8")

f.write("Hello there!\n")
f.write("General Kenobi!")

f.close()

# Az a mód (append), nem törli a fájlnak a tartalmát, hanem a végéről elkezdhetünk új tartalmat belerakni
f = open("output.txt", "a", encoding = "utf-8")

f.write("\nMay the 4th be with you!")

f.close()
#################################################################
f = open("input.txt", "a", encoding = "utf-8")

f.write("\nCsudijó mese volt ez!")

f.close()

#################################################################

f = open("input.txt", "a+", encoding="utf-8")

print(f.read(20)) # A végéről indul, úgyhogy nem olvas be semmit
f.write("Szia!")

f.close()

#################################################################
f = open("input.txt", "r+", encoding="utf-8")

print(f.read(20)) 
f.write("Szia!")

f.close()
"""
###############################################################

nevek = ["András", "Péter", "Béla", "Cecil", "Hugó", "Dóra", "Ábel", "Domonkos"]
életkorok = [18, 12, 9, 13, 30, 21, 17, 15]
osztályzatok = [3, 5, 4, 2, 1, 2, 4, 3]
sport = ["Foci", "Tenisz", "Kosárlabda", "Foci", "Golf", "Floorball", "Röplabda", "Foci"]

# Mentsük el ezeket az adatokat egy csv fájlba!
# csv = comma seperated value (Vesszővel elválasztott értékek)

f = open("osztaly.csv", "w", encoding="utf-8")

for i in range(len(nevek)):
    f.write(f"{nevek[i]};{életkorok[i]};{osztályzatok[i]};{sport[i]}\n")

f.close()

# Feladat: Olvassuk be az autok.csv fájl tartalmát, és mentsük el az 
# adatokat egy megfelelő adatszerkezetben

f = open("autok.csv", "r", encoding="utf-8")
rendszámok = []
gyártók = []
lóerők = []
# string.strip() - eltünteti a whitespaceket (szóköz, enter), a string elejéről
# és végéreől
# string.split(";") - ; -ők mentén feldarabolja a stringet egy listába
for line in f:
    sor = line.strip().split(";")  # ['VRO-121', 'Peugeot', '1450']
    rendszámok.append(sor[0])
    gyártók.append(sor[1])
    lóerők.append(sor[2])

f.close()
print(rendszámok)
print(gyártók)
print(lóerők)

# konteksztus manager

with open("osztaly.csv", "r", encoding="utf-8") as f:
    print(f.read(20))

f.read(30)