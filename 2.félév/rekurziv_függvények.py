# A rekurzív függvény, egy olyan függvény ami önmagát hívja meg

# Faktoriális:
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1
# 0! = 1

def fakt(n):
    if n == 1 or n == 0:
        return 1            # Nem hívja meg önmagát a függvény (degnerált eset)
    return n * fakt(n-1)    # Figyeljünk arra, hogy fgv. el tudjon jutni egy degenerált esethez

print(fakt(5))
print(fakt(1))
print(fakt(10))
print(fakt(0))

# Írjunk egy függvény az "a" rekurzív sorozat n. elemének kiszámítására
# a(n) = 5 + a(n-1)
# a(1) = -10
# a(4) = 5 + a(3) = 5 + 0 = 5
# a(3) = 5 + a(2) = 5 + -5 = 0
# a(2) = 5 + a(1) = 5 + -10 = -5
# a(1) = -10

def a(n):
    if n == 1:
        return -10
    return 5 + a(n-1)

print(a(10))
print(a(3))
print(a(5))
print(a(1))

# fibonacii:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#fib(n) = fib(n-1) + fib(n-2)
#fib(1) = fib(2) = 1

from functools import cache
from sys import setrecursionlimit

setrecursionlimit(5000)

@cache
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(1200))

# Írjunk rekurzív függvényt ami a b sorozat n. elemét adja meg!
# b(n) = b(n-1) * 2 + 3
# b(1) = 1
# 1, 5, 13, 29, 61, ...

@cache
def b(n):    
    if n == 1:        
        return 1    
    return b(n - 1) * 2 + 3

# Írjunk egy függvényt ami a c sorozat n. elemét adja meg!
# c(n) = 5 * c(n-1) - 2 * c(n-2)
# c(1) = 0
# c(2) = 1

@cache
def c(n):    
    if n == 1:       
        return 0
    if n == 2:
        return 1
    return 5* c(n - 1) - 2 * c(n-2)

print(c(5))
print(c(6))
print(c(7))

# Rekurzív függvénnyel készüntsünk egy összegzés tételét
import random
lista = [random.randint(-10,10) for i in range(1000)]

def rek_sum(lista):
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    return lista[0]  + rek_sum(lista[1:])

print(f"rek_sum(lista) = {rek_sum(lista)},    sum(lista) = {sum(lista)}")

# Írjunk egy rekurzív, hatányozó függvényt
# power(3, 5) = 3 * power(3, 4)
# power(x, 0) = 1
# power(x, 1) = x
def power(a, b):
    if a == 0 and b == 0:
        return "ERROR"
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * power(a, b-1)

print(power(2, 10))
print(power(10, 3))
print(power(3, 4))
print(power(0, 0))
