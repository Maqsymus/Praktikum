#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from datetime import datetime





df = pd.read_csv('experiment.csv')
df['time'] = df['time']
df['time'] = pd.to_datetime(df['time'])
#print df
#format='%Y-%m-%d %H:%M:%S.%f
#exit()


df = df.set_index("time")

ax = df.plot(figsize=(20, 15))




#h = ax.legend(loc='center left', bbox_to_anchor=(0.85, 0.5), fontsize=11)
#x = df['time']
#ds = [datetime.strptime(y, "%Y-%m-%d %H:%M:%S.%f") for y in x]
#xi = [i for i in range(0, len(x))]
#plt.ylim(0.8,1.4)
#ax.set_xticklabels(df['time'], rotation=0)
#plt.plot(x, marker='o', linestyle='--', color='r', label='Square')
#plt.xlabel('x')
#plt.xticks(ds, x)
h = ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=14)
plt.title('Krypto-Waehrungen 2018/01/22')
fig = ax.get_figure()
fig.savefig('y.png')
