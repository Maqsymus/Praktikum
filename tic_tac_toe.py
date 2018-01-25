#!/usr/bin/python3
import random
winner = []
liste_a = ["_","|","_","|","_"]
liste_b = ["_","|","_","|","_"]
liste_c = ["_","|","_","|","_"]
liste_d = [0,1,2,3,4,5,6,7,8]
while len(liste_d) > 0:
    print(liste_a)
    print(liste_b)
    print(liste_c)
    eingabe = raw_input("Wo möchtest du setzen? 1,2 und 3 markieren die Spalten, a,b und c die Zeilen.
