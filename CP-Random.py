#!/usr/bin/python
#Random Zahl importieren
import random
#Range definieren
z = random.randrange(1,1001)
#Funktion definieren
def Collatz(z):
    eins = False
    zahl = z
    liste = []
#Loop
    while not eins:
        liste.append(zahl)
        if zahl==1:
            eins = True
        elif zahl%2==0:
            zahl =zahl/2
        elif zahl%2==1:
            zahl = zahl*3+1
    return liste
for x in range(0,10):
    z = random.randrange(1,101)
    liste = Collatz(z)
    print(liste)
