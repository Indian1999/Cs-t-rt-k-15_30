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

print(MyPackage.is_palindrome(szöveg))
print(MyPackage.is_palindrome(szöveg, False))

import datetime

# datetime modul datetime osztályának a now() függvényét hívjuk
print(datetime.datetime.now()) 
print(datetime.date.today())
print(datetime.date.today() - datetime.timedelta(days=200000))

print(datetime.date.today() - datetime.date(year=1, month=1, day=1))