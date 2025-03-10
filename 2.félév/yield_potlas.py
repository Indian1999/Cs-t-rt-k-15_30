# yield függvények (generátor függvények)
# returnhöz hasonló, ugyanúgy visszaad egy értéket, viszont ez nem állítja meg a függvény futását

def listElements():
    yield 5
    yield 19
    yield True
    yield "kiscica"
    yield [1,2,3]
    yield 3.14
    yield "kiskutya"
    
def myRange(num):
    i = 0
    while i < num:
        yield i
        i += 1 

for item in listElements():
    print(item)
    
for i in range(5):
    print(i, end= " ")
print()

for i in myRange(5):
    print(i, end= " ")
print()

def squares(n):
    i = 1
    while i <= n:
        yield i*i
        i += 1
        
for i in squares(20):
    print(i, end= " ")
print()

def f(x):
    return x**2 - 2*x + 1

def g(x):
    return 2**x

def infinite_func(func):
    i = 0
    while True:
        yield func(i)
        i += 1
        
import time
for i in infinite_func(lambda x: x**3 + 2*x**2 + 3*x - 50):
    print(i)
    time.sleep(0.5)
    if i > 500:
        break # Ha kilép az aktuális ciklusból

