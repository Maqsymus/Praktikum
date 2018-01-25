#!/usr/bin/python
liste = range(1,101)
#Liste definieren
#algorythmus
for Zahl in liste:
    if Zahl%3==0 and Zahl%5==0:
        print("FizzBuzz")
    elif Zahl%3==0:
        print("Fizz")
    elif Zahl%20==0:
        print("lol")
    elif Zahl%5==0:
        print("Buzz")
    else:
        print(Zahl)
