#yield függvények (generátor függvények)
# yield visszaad egy értéket, de nem állítja le a függvényt
def generate_series():
    yield 5
    yield 8
    yield "kiscica"
    yield "palacsinta"
    yield [1,2,3]
    yield 3.14
    yield 0
    yield 18
    
for item in generate_series():
    print(item, end=" ")
print()

# A range függvény is egy ilyen generátor függvény
for i in range(5):
    print(i, end = " ")
print()

def myRange(num):
    i = 0
    while i < num:
        yield i
        i += 1

for i in myRange(5):
    print(i, end=" ")
print()

def squared_numbers(num = None):
    if num == None:
        i = 1
        while True:
            yield i**2
            i += 1
    else:
        i = 1
        while i <= num:
            yield i**2
            i += 1
            
for i in squared_numbers(20):
    print(i, end=" ")
print()
            
for i in squared_numbers():
    print(i, end=" ")
    if i > 10000:
        break # Hogyha ezt kiadjuk egy cikluson belól, akkor leáll a ciklus
print()

# Készítsünk egy generátor függvényt, ami a prímszámokat sorolja fel

def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime

def generate_primes(num):
    primes = []
    i = 2
    while len(primes) < num:
        if is_prime(i):
            primes.append(i)
            yield i
        i += 1
            
for i in generate_primes(30):
    print(i, end= " ")
print()
        
# 1. feladat: Írjunk egy függvényt ami felsorolja a számokat 1-től 100-ig, amik 7-tel oszthatóak
def generate_div_sevens():
    for i in range(1, 101):
        if i % 7 == 0:
            yield i

for i in generate_div_sevens():
    print(i, end= " ")
print()
# 2. feladat: Írjunk egy függvényt, ami a-tól b-ig felsorolja az m-mel osztható számokat
def divisors_from_to(a, b, m):
    for i in range(a, b):
        if i % m == 0:
            yield i

for i in divisors_from_to(3422, 4523, 73):
    print(i, end= " ")
print()

# 3. feladat: Írjunk egy függvényt ami felsorolja az alábbi sorozat elemeit:
# a(n) = n*2 + 3

def generate_an(num):
    n = 1
    for i in range(1, num+1):
        yield i *2 + 3
        
for i in generate_an(15):
    print(i, end= " ")
print()

# 4. feladat: Írjunk egy függvényt ami felsorolja a fibonacci sorozat elemeit:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 

def fib_generator():
    a = 1
    b = 1
    while True:
        yield a
        c = a + b
        a = b
        b = c

for i in fib_generator():
    print(i, end=" ")
    if i > 2000:
        break
print()
# ciklusvezérlő kulcsszavak (break, continue)
for i in range(10):
    if i % 3 == 0:
        continue   # A következő ciklus iterációra ugrik (minden ami utána jönne, kihagyja)
    print(i, end = " ")
print()

num = 49
divisor = 2
prime = True
while prime:
    if num == divisor:
        break
    if num % divisor != 0:
        divisor += 1
        continue
    prime = False

print(prime)

# ciklusok else ága (Python exclusive)

for i in range(5):
    print(i, end = " ")
else:
    print("Ez itt a for ciklus else ága")
    
    
logic_value = False
while logic_value:
    print("szia")
else:
    print("Ez itt a while ciklus else ága")
    
# Az else ág akkor fut le, hogyha természetes módon léptünk ki a ciklusból
# azaz, abban az esetben, ha breakkel lépünk ki, nem fog lefutni

for i in range(10):
    if i == 5:
        break
else:
    print("Ez az else ág nem fog lefutni")
    

# 5 db #
i = 1
while i < 10: # 1, 2, 4, 8, else
    print("#", end="")
    i *= 2
else:
    print("#", end="")
print()

# 7 db #
i = 0
while i < 20: # 0, 1, 2, 3, 4, 5, 6
    if i == 7:
        break
    print("#", end = "")
    i += 1
else:
    print("#", end="")
print()

def fakt(num):
    result = 1
    run = True
    while run:
        if type(num) != int or num < 0:
            break
        result *= num
        if num == 1:
            run = False
        num -= 1
    else:
        return result
    
print(fakt("kiscica"))
print(fakt(-5))
print(fakt(3.14))
print(fakt(6))
