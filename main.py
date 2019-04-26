#!/usr/bin/python3

# IMPORT VARIUS UTILITY
import os, platform, random, time, string

# IMPORT ANSWERS ARRAY
from answers import *

# SETTINGS
NAME = "Minerva"
VERSION = "0.0.1"
AUTHOR = "Andrea"
DESC = "Script per la lettura a freddo sviluppato da %s" % AUTHOR


# TITLE AND DESCRIPTION OF THE PROJECT
def intro():
    print("#" * len(DESC))
    print("%s, v. %s\n%s" % (NAME, VERSION, DESC))
    print("#" * len(DESC))


# CLEAN THE OUTPUT
def check_platform():
    os.system('cls' if os.name=='nt' else 'clear') 


# GET RANDOM STRING FROM ARRAY
def cold_read(a, b, c, d):
    print("%s\n%s\n%s\n%s" % (random.choice(a), random.choice(b), random.choice(c), random.choice(d)))


# COLD READER FUNCTION
def minerva(val):
    age = 0
    while True:
        try:
            userInput = int(input("Quanti anni hai %s? " % val))       
        except ValueError:
            print("Inserisci un intero!")
            continue
        else:
            break 
    print(" ")
    desc = input("\nTi farò un test, dopodichè calcolerò una lettura del tuo passato presente e futuro.\nDurante il test premi invio per procedere [premi invio]")
    q1 = input("Pensa ad un numero.. ")
    q2 = input("Raddoppialo.. ")
    q3 = input("Aggiungi 6.. ")
    q4 = input("Dividi per 2.. ")
    q5 = input("Sottrai il numero pensato.. ")
    q6 = input("Hai ottenuto 3.")
    q7 = input("Premi invio e procedi con la lettura a freddo")
    time.sleep(1)
    print(" ")
    cold_read(generic_past, feel_past, health_past, job_past)
    cold_read(generic_pres, feel_pres, health_pres, job_pres)
    cold_read(generic_fut, feel_fut, health_fut, job_fut)


# START THE PROGRAM
userInput = 0

while True:
    try:
        check_platform()
        intro()
        userInput = int(input("[1]Inizia la lettura\t[2]Esci\n\nInserisci un valore: "))      
    except ValueError:
        print("Input invalido!")
        continue
    else:
        if userInput == 1:
            while True:
                try:
                    name = input("Come ti chiami? ")
                    assert  any([char not in string.ascii_letters for char in name]) is False
                except AssertionError:
                    print("Il tuo nome deve contenere caratteri validi!")
                else:
                    break
            minerva(name)
            input("\n[Premi invio per uscire]")
            break
        elif userInput == 2:
            break
        
        
