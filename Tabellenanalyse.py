#!/usr/bin/python
import random as rndm
import pandas as pd

# user input
x = raw_input("Waehle, wie viele Nummern generiert werden sollen. ")
x = int(x)
y = raw_input("Waehle die maximale Nummerngroesse. ")
y = int(y)

#z = raw_input("Sollen die Zahlen absteigend oder aufsteigend sortiert werden? Fuer absteigend tippe ab, fuer aufsteigend tippe auf")
sortiert = []
# zufallszahl generator
def nummern_ausgabe(x,y):

    random_nummern = []
    for x in range(0,x):
        random_nummern.append(rndm.randrange(0,y))
    return random_nummern

my_list = nummern_ausgabe(x,y)
#print(my_list)
d = len(my_list)

# sortierung
#if z =="ab":
    #while len(my_list) > 0:
        #maximum = max(my_list)
        #ind = my_list.index(maximum)
        #sortiert.append(maximum)
        #my_list.pop(ind)
#elif z == "auf":
        #while len(my_list) > 0:
            #minimum = min(my_list)
            #ind = my_list.index(minimum)
            #sortiert.append(minimum)
            #my_list.pop(ind)
#print(sortiert)

#Sortierung 2
def sortieren(my_list,d):
    loesung = []

    while len(loesung) < d:
        sorted_list = []
        while len(my_list) > 1:
            zahl1 = my_list[0]
            zahl2 = my_list[1]
            if zahl1 > zahl2:
                sorted_list.append(my_list[0])
                my_list.pop(0)
            elif zahl1 < zahl2:
                sorted_list.append(my_list[1])
                my_list.pop(1)
            elif zahl1 == zahl2:
                sorted_list.append(my_list[0])
                my_list.pop(0)
        loesung.append(my_list[0])
        my_list = sorted_list

    print(loesung)
sortieren(my_list,d)
