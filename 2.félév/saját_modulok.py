#from MyPackage import functions
#from MyPackage import *   Mindent behúzunk a MyPackage
from random import randint

import MyPackage
MyPackage.print_rectangle(5,10)

lista = MyPackage.names[:10]
print(lista)

print("Az 5 egység sugarú kör területe:", MyPackage.pi * 5**2)
