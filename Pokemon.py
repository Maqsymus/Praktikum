#!/usr/bin/python
import pandas as pd

# Aufgabe 2: Lade Daten.
pokemon_df = pd.read_csv("Pokemon.csv")

# Aufgabe 3: Waehle Spalte mit Namen und sortiere
def aufgabe3(df):
    r = df['Name'].sort_values()
    print(r)
#aufgabe3(pokemon_df)

#Aufgabe 4
def aufgabe4(df):
    re = df[['Speed','Defense','Attack']].max()
    print(re)
#aufgabe4(pokemon_df)

#Aufgabe 5
def aufgabe5(df):
    res = df[df['Legendary']==True]
    print(res)
#aufgabe5(pokemon_df)

#Aufgabe 6
def aufgabe6(df):
    resu = df[df['Type 2']==None]
    z = df['Type 2'].count()
    print(z)
#aufgabe6(pokemon_df)

#Aufgabe 7
def aufgabe7(df):
    grps = df.groupby(["Generation"])
    result = grps.size()
    print(result)
#aufgabe7(pokemon_df)

#Aufgabe 8
def aufgabe8(df):
    typ = df.groupby(["Type 1","Type 2"])
    result = typ.size()
    print(result)
#aufgabe8(pokemon_df)

#Aufgabe 9
def aufgabe9(df):
    wert = df.groupby(["Type 1","Type 2"])["Total"].max()
    print(wert)
#aufgabe9(pokemon_df)

#Aufgabe 10
def aufgabe10(df):
    grps = df.groupby(["Generation"])
    result = grps.size()
    result = result.plot()
    fig = result.get_figure()
    fig.savefig("result.png")
    #aufgabe10(pokemon_df)

#Aufgabe 11
def aufgabe11(df):
    result = df[df["Attack"]>100].count()
    print(result)
#aufgabe11(pokemon_df)

#Aufgabe 12
def aufgabe12(df):
    result = df[df['Legendary']==True]
    result = result[result['Type 1']=='Water'].count()
    print(result)
#aufgabe12(pokemon_df)

#Aufgabe 13
def aufgabe13(df):
    result = df[df["Type 1"]=="Flying"]
    result = result[result["Defense"]<100].count()
    print(result)
#aufgabe13(pokemon_df)

#Aufgabe 14
def aufgabe14(df):
    result = df.groupby(["Type 1"]).size()
    result = result.plot()
    fig = result.get_figure()
    fig.savefig("Types.png")
#aufgabe14(pokemon_df)

#Aufgabe 14 v2
def aufgabe14v2(df):
    #result = df.groupby(["Attack"]).size()
    result = df["Attack"]
    #result = pd.DataFrame(result.values(), index=result.keys(), columns=['Attack Points'])
    #result = result.plot(kind="hist")
    result = result.hist(bins=30)
    fig = result.get_figure()
    fig.savefig("Attack.png")
aufgabe14v2(pokemon_df)
