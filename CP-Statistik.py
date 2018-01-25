#!/usr/bin/python
#Packages importieren
import random
#Packages andere Namen geben
import pandas as pd
z = random.randrange(1,1001)
#Funktion definieren
def Collatz(z):
    eins = False
    zahl = z
    liste = []
    while not eins:
        liste.append(zahl)
        if zahl==1:
            eins = True
        elif zahl%2==0:
            zahl =zahl/2
        elif zahl%2==1:
            zahl = zahl*3+1
    return liste
dic = {}
#Laenge der Zahlen 1-1000000 bestimmen
for x in range(1,1000):
    liste = Collatz(x)
    laenge = len(liste)
    dic[x] = laenge
#print(dic)


df = pd.DataFrame(dic.values(), index=dic.keys(), columns=['CP'])
ergebnis = df.plot()
fig = ergebnis.get_figure()
fig.savefig("ergebnis.png")
