print("Hello World!")
print(input("Írj ide valamit: "))
szöveg = "kutya" #szöveg nevű változó, cica értékkel
print(szöveg)
szöveg = input("Add meg a szöveg értékét!\n") # \n = enter  alt gr + Q -> \
print("A szöveg hossza:", szöveg.__len__())
print(szöveg.split(" "))
print(szöveg.split('a'))

név = "John Doe"            # szöveg (string (str))
életkor = 28                # egész szám (integer (int))
munka = "Programozó"        # szöveg (string (str))
állampolgárság = "Brit"     # szöveg (string (str))
magasság = 180              # egész szám (integer (int))
súly = 75.6                 # nem egész szám (float) lebegőpontos szám
férfi = True                # logikai érték (boolean (bool)) igaz/hamis

print(type(név))        # <class 'str'> (string)
print(type(életkor))    # <class 'int'>
print(type(súly))       # <class 'float'>
print(type(férfi))      # <class 'bool'>

print("Név: " + név)
print("Életkor: " + str(életkor))
print("Életkor: " + str(súly))
