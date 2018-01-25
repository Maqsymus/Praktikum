#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, urllib2, json
import time as tm
from datetime import datetime

liste_w = ["BTC","BCH","DGB","DASH","ETC","ETH","LTC","XMR","NXT","ZEC"]
liste_f = ["USD","EUR"]

while True:
    try:
        liste_e = []
        liste_d = []
        timer = str(datetime.now())
        for w in liste_w:
            for f in liste_f:
                link = "https://min-api.cryptocompare.com/data/price?fsym="+w+"&tsyms="+f
                crypto_waehrung = urllib2.urlopen(link)
                waehrung = crypto_waehrung.read()
                waehrung2 = json.loads(waehrung)
                waehrung2 = waehrung2[f]
                liste_d.append(waehrung2)

        fd = open('experiment.csv','a')
        fd.write(timer+",")
        g = ','.join(str(i) for i in liste_d) + "\n"
        fd.write(g)
        fd.close()

        tm.sleep(60)
    except Exception as e:
        print(e)
        print("Unexpected error:", sys.exc_info()[0])
