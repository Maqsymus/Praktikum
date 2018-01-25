#!/usr/bin/python
#importieren von packages
import random
r = random.randrange(1,21)
gewonnen = False
#Schleife/Loop
while not gewonnen:
    g = int(input("rate mal\n"))
    if r < g:
        print("zu gross")
    elif r > g:
        print("zu klein")
    elif r == g:
        gewonnen = True
        print("du hast gewonnen!")
