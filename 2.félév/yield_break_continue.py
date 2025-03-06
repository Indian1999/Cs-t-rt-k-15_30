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
# ciklusvezérlő kulcsszavak (break, continue)

# ciklusok else ága

