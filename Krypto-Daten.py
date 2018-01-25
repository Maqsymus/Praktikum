#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv("experiment.csv")

liste_w = ["BTC","BCH","DGB","DASH","ETC","ETH","LTC","XMR","NXT","ZEC"]
liste_f = ["USD","EUR"]

for f in liste_f:
    for w in liste_w:
        rma = df[w+' in '+f].max()
        rma1 = str(rma)
        print(rma1+" ist der hoechsten gemessene Wert bei "+w+" in "+f)
        rmi = df[w+' in '+f].min()
        rmi1 = str(rmi)
        print(rmi1+" ist der niedrigste gemessene Wert bei "+w+" in "+f)
        sol = ((rma-rmi)/rma)*100
        sol1 = str(sol)
        print(sol1+"% ist der prozentuale Unterschied zwischen dem hoechsten und dem niedrigsten gemessenen Wert bei "+w+" in "+f)

for w in liste_w:
    rma = df[w+' in EUR'].max()
    rmi = df[w+' in EUR'].min()
    sole = ((rma-rmi)/rma)*100
    rma = df[w+' in USD'].max()
    rmi = df[w+' in USD'].min()
    solu = ((rma-rmi)/rma)*100
    if sole > solu:
        print("Bei der Krypto-Währung "+w+" ist es sicherer mit US-Dollars zu traden, da bei ihnen der Kurs geringer schwankt als bei Euros.")
    if solu > sole:
        print("Bei der Krypto-Währung "+w+" ist es sicherer mit Euros zu traden, da bei ihnender Kurs geringer schwankt als bei US-Dollars.")
