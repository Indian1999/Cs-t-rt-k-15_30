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

