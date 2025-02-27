"""
print("Hello World!")

fruit = "Banana"
print("The fruit is: " + fruit)
darab = 5
#print("We have this many: " + darab) # HIBA! szöveget számmal nem tudunk összeadni!
print("We have this many: " + str(darab))

pet_name = "Zsömle"
pet_age = 11
pet_species = "Dog"

print("My pet is called " + pet_name + " he is " + str(pet_age) + " years old and he is a " + pet_species + ".")
print(f"My pet is called {pet_name} he is {pet_age} years old and he is a {pet_species}.")
print("My pet is called", pet_name, "he is", pet_age, "years old and he is a", pet_species, ".")
"""
# alt + Q -> \
tárgy_1 = input("Mondj egy tárgyat:\n")
tárgy_2 = input("Mondj egy tárgyat:\n")
tulajdonság = input("Mondj egy tulajdonságot:\n")
zene = input("Mondj egy zenét:\n")
híresség = input("Mondj egy híres embert:\n")
érzés = input("Mondj egy érzést:\n")
ige = input("Mondj egy igét:\n")
helyszín = input("Mondj egy helyszínt:\n")
kaja = input("Mondj egy ételt:\n")
személy = input("Mondd egy személynek a nevét:\n")

print(f"""

Most értem haza a buliból ahol {személy}-el voltam.
{tulajdonság} pizzát ettünk {helyszín}-ben! Mindenki kiválaszthatta
a neki tetsző feltéteket. Az én pizzámra {tárgy_1}-t és {tárgy_2}-t raktam.
Nagyon finomra sikeredett! A szélét még meg is töltötték {kaja}-val!
Nagyon {érzés} érzés volt! És ha ez nem lenne elég még {híresség} is ott volt
és énekelte a {zene}-t! Annyira izgatott lettem, hogy felkeltem
a székemből és elkezdtem {ige}-ni.
""")
"""

num = 5
szöveg = "cica"
férfi = True
állat = False

if férfi:
    print("ez egy férfi") #kiírva
if állat:
    print("ez egy állat") # ez nem lett kirva
if num:
    print("a num igaz") #kiírva ha nem 0 a num értéke, akkor igaz lesz
if szöveg:
    print("a szöveg igaz") #kiírva ha a szöveg nem egy üres string, akkor igaz lesz

if állat:
    print("ez egy állat")
else:
    print("Ez nem egy állat")

#feladat: olvassunk be két számot és döntsük el, hogy melyik a nagyobb

első = int(input("Add meg az első számot:\n"))
második = int(input("Add meg a második számot:\n"))

if első == második:
    print("A két szám egyenlő!")
elif első > második:
    print("Az első szám a nagyobb!")
else:
    print("A második szám a nagyobb!")

eredmény = int(input("Add meg, hogy hány százalékos lett a dolgozat:\n"))
# 90-100: 5
# 75- 89: 4
# 60- 74: 3
# 45- 59: 2
#  0- 45: 1
if eredmény >= 90:
    print("5-ös")
elif eredmény >= 75:
    print("4-es")
elif eredmény >= 60:
    print("3-as")
elif eredmény >= 45:
    print("2-es")
else:
    print("1-es")
"""
