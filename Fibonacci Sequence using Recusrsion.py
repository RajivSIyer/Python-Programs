import time

#Iterative Method

def fib_iter(n):

    a, b = 0, 1

    for i in range(n):
        #print(a)
        a, b = b, a+b

    return a

t1 = time.time()
fib_iter(10)
t2 = time.time()
print(t2-t1)

#Recursive Method

def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-2) + fib_rec(n-1)

t1 = time.time()
fib_rec(10)
t2 = time.time()
print(t2-t1)

#Memoisation/Dynamic Caching
n = 10
cache = [None]*(n+1)

def fib_mem(n):

    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_mem(n-2) + fib_mem(n-1)
    return cache[n]

t1 = time.time()
fib_mem(10)
t2 = time.time()
print(t2-t1)

print(fib_mem(10))

t1 = time.time()
fib_mem(10)
t2 = time.time()
print(t2-t1)