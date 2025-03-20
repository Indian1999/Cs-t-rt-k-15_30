#from MyPackage import functions
#from MyPackage import *   Mindent behúzunk a MyPackage
from random import randint

import MyPackage
MyPackage.print_rectangle(5,10)

lista = MyPackage.names[:10]
print(lista)

print("Az 5 egység sugarú kör területe:", MyPackage.pi * 5**2)

# Döntsük el egy szövegről, hogy palindróm-e

szöveg = "In+dul,? a ,gö:rög- aludni."
uj_szöveg = ""
for char in szöveg:
    if char not in MyPackage.special_chars:
        uj_szöveg += char
szöveg = uj_szöveg.lower().replace(" ", "")
print(szöveg)

print(MyPackage.is_palindrome(szöveg))