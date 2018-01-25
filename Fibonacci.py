#!/usr/bin/python

def fib_n(zahl):
    a = 1
    b = 1
    if zahl < 3:
        return a
    for x in range(zahl-2):
        c = b
        b = a+b
        a = c
    return b
g = int(input("rate mal\n"))
k = fib_n(g)
print(k)
