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
        


# ciklusvezérlő kulcsszavak (break, continue)

# ciklusok else ága

