#!/usr/bin/env python
from ast import Global
import sys
import re
import numpy as np
from player import player,returnPlayer,CreatePopulation,SortPopulation,Tournament
import random
from Recombination import uniformCrossover,RECOMBINATION_LIST

#randSeed 
#populationSizeN  
#stringSizen  
#probApplyCrossover 
#probApplyMutation 
#selectionMethod  
#tournamentSizek  
#fitnessFunction  
def getValueFromSettings(l, s):
    for i in l:
        if i.startswith(s):
            return float(i.split(" ")[1])
if len(sys.argv) != 1:
    for i in sys.argv:
        if re.search(r"^[\w,\s-]+\.[A-Za-z]{3}$", i):
            with open(i) as f:
                paramlist = list(f)
            randSeed = getValueFromSettings(paramlist, "randSeed")
            populationSizeN = getValueFromSettings(
                paramlist, "populationSizeN")
            stringSizen = getValueFromSettings(paramlist, "stringSizen")
            probApplyCrossover = getValueFromSettings(
                paramlist, "probApplyCrossover")
            probApplyMutation = getValueFromSettings(
                paramlist, "probApplyMutation")
            selectionMethod = getValueFromSettings(
                paramlist, "selectionMethod")
            tournamentSizek = getValueFromSettings(
                paramlist, "tournamentSizek")
            fitnessFunction = getValueFromSettings(
                paramlist, "fitnessFunction")
        if i == "-h":
            h = True
            print("TODO:help")
        if i == "-g":
            g = True
        if i == "-G":
            G = True
else:
    randSeed = 123
    populationSizeN = 100
    stringSizen = 50
    probApplyCrossover = 0.6
    probApplyMutation = 1.0
    selectionMethod = 0
    tournamentSizek = 2
    fitnessFunction = 0
    h = False
    g = False
    G = False

def main():

    b = returnPlayer()
    #b.print()

    c = returnPlayer()
    #c.print()
    
    #d,f = uniformCrossover(b,c)
    d,f = RECOMBINATION_LIST[0](b,c)
    #d.print()
    #f.print()

    #print("#######################################")
    #l = CreatePopulation(50,50)
    #for i in l:
    #    i.print()
    #print(len(l))
    #print("#######################################")
    #print("#######################################")
    #print("#######################################")
    #lsort = SortPopulation(l)
    #for i in lsort:
    #    i.print()
    #l = [b,c,d,f]
    l = [returnPlayer(),returnPlayer()]#,returnPlayer(),returnPlayer()]
    for i in l:
        i.print()
        print(i)
    print("#######################################") 
    s1 = Tournament(l,uniformCrossover,tournamentSizek)
    for i in s1:
        print(i.print())
        print(i)

    
    print("end")



main()
