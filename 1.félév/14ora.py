# 1. feladat: Számoljuk ki, hogy valaki hány napos
today_string = "2025-01-09"
#birthday_string = input("Add meg a születési dátumodat (pl.: 1999-02-10)!\n")
birthday_string = "2025-01-01"
today = today_string.split("-") # ["2025", "01", "09"]
today = [int(item) for item in today]
birthday = birthday_string.split("-") # ["2025", "01", "09"]
birthday = [int(item) for item in birthday]

#365,24218967 SI nap (365 d 5 h 48 m 45 s) 
#Szökőév akkoor van:
# Ha 4-gyel osztható és 100-al nem osztható
# vagy pedig 400-al osztható


#[2015, 4, 12]
# év   hó  nap
days = 0

honapok = ["HONAP", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

#while today != birthday:
while days != 10000:
    if birthday[2] < honapok[birthday[1]]:
        birthday[2] += 1
    else: # Ha a hónap utolsó napja van
        if birthday[1] == 2 and birthday[2] == 28 and is_leap_year(birthday[0]):
            birthday[2] += 1
        elif birthday[1] != 12:
            birthday[2] = 1
            birthday[1] += 1
        else: # Ha december utolsó napja van
            birthday[0] += 1
            birthday[1] = 1
            birthday[2] = 1
    days += 1

print(birthday)
print(days)

# 2. feladat: Döntsük el két stringről, hogy anagrammák-e
# Hogy ha a két szó betűit összetudjuk keverni úgy hogy a másik szót megkapjuk, akkor a két szó
# egymás anagrammái
# pl.: étel - élet;   kelletlen  -  lelketlen;     nyelvész  -  szelvény
#word1 = input("Add meg az első szót!\n").lower()
#word2 = input("Add meg a második szót!\n").lower()

word1 = "malac"
word2 = "alma"
if len(word1) == len(word2):
    if sorted(word1) == sorted(word2):
        print("Ezek anagrammák")
    else:
        print("Ezek nem anagrammák")
else:
    print("Ezek nem anagrammák")

lista = [4, 1, 2, 4, 2]
print(lista.sort())
print(lista)

# 3. feladat: Hány autónak kell lassítania?
cars = [13, 43, 54, 34, 51, 53, 63, 49, 52, 58, 60, 63, 51, 77, 81, 88, 82, 90, 93, 100, 99]

számláló = 0
for i in range(len(cars)):
    lassabban = False
    for j in range(i + 1, len(cars)):
        if cars[j] < cars[i]:
            lassabban = True
            break
    if lassabban:
        számláló += 1

print(számláló, "autónak kell lassítania.")