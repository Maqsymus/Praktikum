#!/usr/bin/python3
# -*- coding: utf-8 -*-
#importieren
import urllib.request as ul
import json
import gzip
import shutil
#input sammeln
print("Aktuelle Werte von diversen Krypto-Währungen.")
eingabe = input("Von welcher Währung möchtest du den aktuellen Wert wissen? Bitcoin = BTC, Ethereum = ETH, Z-Cash = ZEC, DigitalCash = DASH  ")
eingabe2 = input("Möchtest du den Wert in US-Dollar oder Euro dargestellt bekommen? Euro = EUR, US-Dollar = USD  ")
#einzelne Währungen ausgeben
if eingabe == "ETH":
    crypto_waehrung = ul.urlretrieve("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR")
    waehrung = open(crypto_waehrung[0]).read()
    waehrung2 = json.loads(waehrung)
    if eingabe2 == "EUR":
        waehrung2['EUR']
        print(waehrung2['EUR'])
    elif eingabe2 == "USD":
        waehrung2['USD']
        print(waehrung2['USD'])

elif eingabe == "BTC":
    crypto_waehrung = ul.urlretrieve("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    waehrung = open(crypto_waehrung[0]).read()
    waehrung2 = json.loads(waehrung)
    if eingabe2 == "EUR":
        waehrung2['EUR']
        print(waehrung2['EUR'])
    elif eingabe2 == "USD":
        waehrung2['USD']
        print(waehrung2['USD'])

elif eingabe == "ZEC":
    crypto_waehrung = ul.urlretrieve("https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=USD,EUR")
    waehrung = open(crypto_waehrung[0]).read()
    waehrung2 = json.loads(waehrung)
    if eingabe2 == "EUR":
        waehrung2['EUR']
        print(waehrung2['EUR'])
    elif eingabe2 == "USD":
        waehrung2['USD']
        print(waehrung2['USD'])

elif eingabe == "DASH":
    crypto_waehrung = ul.urlretrieve("https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=USD,EUR")
    waehrung = open(crypto_waehrung[0]).read()
    waehrung2 = json.loads(waehrung)
    if eingabe2 == "EUR":
        waehrung2['EUR']
        print(waehrung2['EUR'])
    elif eingabe2 == "USD":
        waehrung2['USD']
        print(waehrung2['USD'])
