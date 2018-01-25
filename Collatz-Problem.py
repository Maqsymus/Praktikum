#!/usr/bin/python
eins = False
z = int(input("pick a number which is bigger than 1\n"))
zahl = z
liste = []
#Loop/Schleife
while not eins:
    liste.append(zahl)
    print(zahl)
#Bedingungen
    if zahl==1:
        eins = True
        print("Die Zahl ist nun eins")
    elif zahl%2==0:
        zahl =zahl/2
    elif zahl%2==1:
        zahl = zahl*3+1
print(liste)
