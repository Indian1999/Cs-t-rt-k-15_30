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