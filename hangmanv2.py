#!/usr/bin/python
#importieren
import os
import sys
import pandas as pd
import time as tm
#Wort aufteilen

wortketten = pd.read_csv("sinnlose_wortketten.csv")
sample_size = 1
wort1 = wortketten.sample(sample_size).values[0][0]

ind = 0
versuche = 12
geraten = []
leerzeichen_liste = []
buchstaben_liste = list(wort1.lower())
#print(buchstaben_liste)
laenge = len(buchstaben_liste)
for o in range(laenge):
    leerzeichen_liste.append("_")

#Spielintro

print("-" * 20 + "Welcome to hangman!" + "-" * 20)
tm.sleep(0.5)
print("-" * 20 + "Think or die!" + "-" * 20)
tm.sleep(0.5)
print("-" * 20 + "You have only 12 trys" + "-" * 20)
#Spiel

print(leerzeichen_liste)
while versuche > 0 and len(geraten) < laenge:
    buchstabe = raw_input("Select a letter please. ")
    buchstabe = buchstabe.lower()
    if buchstabe in buchstaben_liste and buchstabe not in geraten:
        a = []
        a = (list(i for i in range(len(buchstaben_liste)) if buchstaben_liste[i] == buchstabe))
        ind = 0
        while ind < len(a):
            b = a[ind]
            #print("b: " + str(b))
            #exit()
            geraten.append(buchstabe)
            leerzeichen_liste.pop(b)
            leerzeichen_liste.insert(b, buchstabe)
            ind = ind +1
        print("you are right")
        print(leerzeichen_liste)

    elif buchstabe not in buchstaben_liste:
        if versuche == 12:
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" ")
        if versuche == 11:
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 10:
            print(" |/")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 9:
            print("________")
            print(" |/")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 8:
            print("________")
            print(" |/    |")
            print(" |     |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 7:
            print("________")
            print(" |/    |")
            print(" |     |")
            print(" |     0")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 6:
            print("________")
            print(" |/    |")
            print(" |     |")
            print(" |     0")
            print(" |     |")
            print(" |")
            print(" |")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 5:
            print("________")
            print(" |/    |")
            print(" |     |")
            print(" |     0")
            print(" |    \|")
            print(" |")
            print(" |")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 4:
            print("________")
            print(" |/    |")
            print(" |     |")
            print(" |     0")
            print(" |    \|/")
            print(" |     ")
            print(" |")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 3:
            print("________")
            print(" |/    |")
            print(" |     |")
            print(" |     0")
            print(" |    \|/")
            print(" |     |")
            print(" |     ")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 2:
            print("________")
            print(" |/    |")
            print(" |     |")
            print(" |     0")
            print(" |    \|/")
            print(" |     |")
            print(" |    /")
            print(" |")
            print("/|\\")
            print(" ")
        if versuche == 1:
            print("________")
            print(" |/    |")
            print(" |     |")
            print(" |     0")
            print(" |    \|/")
            print(" |     |")
            print(" |    / \\")
            print(" |")
            print("/|\\")
            print(" ")





























































        versuche = versuche - 1

        print("Wrong Letter! Try again. You have "+str(versuche)+" left")

if versuche == 0:
    print("you lost the game!")
if len(geraten) == laenge:
    print ("you won the game!")
