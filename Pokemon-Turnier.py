#!/usr/bin/python
#Plug-Ins importieren
import time
import sys
import random as rd
import pandas as pd
import matplotlib.pyplot as plt
#Pokemon importieren und einrichten
class Pokemon:
    def __init__(self, name, speed, attack, defense):
        self.name = name;
        self.speed = speed;
        self.attack = attack;
        self.defense = defense;
def create_pokemon(row):
    n = row["Name"]
    s = row["Speed"]
    a = row["Attack"]
    d = row["Defense"]
    object_pokemon = Pokemon(n,s,a,d)
    turnier_pokemons.append(object_pokemon)
#Benutzerdefinierte Werte abholet
#Turnier-Intro
def intro(teilnehmer, spieleranzahl):
    #print("-----------------------------------------------------Pokemon Turnier!-----------------------------------------------------")
    #time.sleep(1)
    #print("--------------------------------------------------------"+str(spieleranzahl)+" Spieler--------------------------------------------------------")
    #time.sleep(1)
    #print("------------------------------------------------Hier kommen die Teilnehmer------------------------------------------------")
    #time.sleep(1)
    index = 0
    while index < len(teilnehmer):
        teilnehmer_buffer = []
        object_pokemon = teilnehmer[index]
        teilnehmer_buffer.append(object_pokemon)
        object_pokemon2 = teilnehmer[index+1]
        teilnehmer_buffer.append(object_pokemon2)
        object_pokemon3 = teilnehmer[index+2]
        object_pokemon4 = teilnehmer[index+3]
        teilnehmer_buffer.append(object_pokemon4)
        object_pokemon5 = teilnehmer[index+4]
        teilnehmer_buffer.append(object_pokemon5)
        object_pokemon6 = teilnehmer[index+5]
        teilnehmer_buffer.append(object_pokemon6)
        object_pokemon7 = teilnehmer[index+6]
        teilnehmer_buffer.append(object_pokemon7)
        object_pokemon8 = teilnehmer[index+7]
        teilnehmer_buffer.append(object_pokemon8)
        laenge = sum([len(pokemon.name) for pokemon in teilnehmer_buffer])

        for pokemon in teilnehmer_buffer:
            #sys.stdout.write(pokemon.name)
            sys.stdout.flush()
            #time.sleep(0.025)
            for x in range(0,5):
                #sys.stdout.write("-")
                sys.stdout.flush()
                #time.sleep(0.025)
        rest = 122-laenge-40

        for x in range(0,rest):
            #sys.stdout.write("-")
            sys.stdout.flush()
            #time.sleep(0.025)

        #sys.stdout.write("\n")
        for x in range(0,122):
        ##    sys.stdout.write("-")
            sys.stdout.flush()
            #time.sleep(0.005)

        #sys.stdout.write('\n')
        index = index + 8
#Turnier-fights 1
def fight(pokemon1, pokemon2):
    #sleep_time = 0.005
    if pokemon1.speed >= pokemon2.speed:
        first_pokemon = pokemon1
        second_pokemon = pokemon2
        ##print(first_pokemon.name+" kaempft gegen "+second_pokemon.name+".")
        #time.sleep(sleep_time)
        #print(first_pokemon.name+" beginnt den Kampf!")
        #time.sleep(sleep_time)
        #time.sleep(sleep_time)
    elif pokemon1.speed < pokemon2.speed:
        first_pokemon = pokemon2
        second_pokemon = pokemon1
        #print(first_pokemon.name+" kaempft gegen "+second_pokemon.name+".")
        #time.sleep(sleep_time)
        #print(first_pokemon.name+" beginnt den Kampf!")
        #time.sleep(sleep_time)

        #time.sleep(sleep_time)
    first_pokemon_defense = first_pokemon.defense
    second_pokemon_defense = second_pokemon.defense

    winner = ""
    while winner == "":
        #print(first_pokemon.name+" Attackiert mit "+str(first_pokemon.attack)+" Angriffspunkten "+second_pokemon.name+" mit "+str(second_pokemon_defense)+" Abwehrpunkten!")
        #time.sleep(sleep_time)
        #print(second_pokemon.name+" Attackiert mit "+str(second_pokemon.attack)+" Angriffspunkten "+first_pokemon.name+" mit "+str(first_pokemon_defense)+" Abwehrpunkten!")
        #time.sleep(sleep_time)
        second_pokemon_defense = second_pokemon_defense - first_pokemon.attack
        first_pokemon_defense = first_pokemon_defense - second_pokemon.attack
        if second_pokemon_defense < 1:
            winner = first_pokemon
        elif first_pokemon_defense < 1:
            winner = second_pokemon
    #print(winner.name+" hat gewonnen!")
    #time.sleep(sleep_time)
    #print("--------------------------------------------------------------------------------------------------------------------------")
    #time.sleep(sleep_time)
    return winner

def turnier(teilnehmer,x):
    intro(teilnehmer,x)
    turnier_teilnehmer_pokemons = teilnehmer

    while len(turnier_teilnehmer_pokemons) > 1:
        turnier_buffer = []
        index = 0
        while index < len(turnier_teilnehmer_pokemons):
            object_pokemon = turnier_teilnehmer_pokemons[index]
            object_pokemon2 = turnier_teilnehmer_pokemons[index+1]
            winner = fight(object_pokemon, object_pokemon2)
            turnier_buffer.append(winner)
            index = index+2
        turnier_teilnehmer_pokemons = turnier_buffer

    gewinner = turnier_teilnehmer_pokemons[0]
    #print("Der Gewinner des Turnieres ist "+gewinner.name)
    return winner



pokemon_df = pd.read_csv("Pokemon.csv", encoding='utf-8')


turnier_dictionary = {}
turnier_gewinner = []
for x in range (0,10000):
    turnier_pokemons = []
    sample_size = 512
    pokemon_sample = pokemon_df.sample(sample_size)
    pokemon_sample.apply(create_pokemon, axis=1)
    pokemon_sample.append(turnier_pokemons)
    turnier_gewinner = []
    winner = turnier(turnier_pokemons,len(turnier_pokemons))
    turnier_gewinner.append(winner.name)
    if winner.name not in turnier_dictionary:
        turnier_dictionary[winner.name] = 1
    elif winner.name in turnier_dictionary:
        turnier_dictionary[winner.name] = turnier_dictionary[winner.name] + 1
for keys,values in turnier_dictionary.items():
    print(keys)
    print(values)
