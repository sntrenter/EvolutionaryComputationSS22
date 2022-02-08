#!/usr/bin/env python
from ast import Global
import sys
import re
import numpy as np
from player import player
import random

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
    b.print()

    c = returnPlayer()
    c.print()
    
    d,f = recombination(b,c)
    d.print()
    f.print()
    print("end")




#Recombination: 
#Our recombination operator is uniform crossover that will take in two parents and produce 
#two new children to put in the offspring population. This results in mixing the bits 
#uniformly from the two parent strings to produce two new children. Note that this 
#operation is applied with a percentage chance from the settings file. If it is determined not 
#to apply recombination, the two children are identical to the parents. Ensure that offspring 
#data structures are set so their fitness will be calculated later if they are changed from the 
#parents.

def recombination(p1: player,p2: player) -> player:
    num = random.random()
    if num < probApplyCrossover:
        #apply crossover
        l1 = []
        l2 = []
        for i in range(len(p1.l)):
            num = random.random()
            if num < .5:
                l1.append(p1.l[i])
                l2.append(p2.l[i])
            else:
                l2.append(p1.l[i])
                l1.append(p2.l[i])
        return player(l1),player(l2)
    else:
        return p1,p2
    



def returnPlayer(size = 50) -> player:
    p = player(np.random.choice([0, 1], size=(size,), p=[.5, .5]))
    return p

def getValueFromSettings(l, s):
    for i in l:
        if i.startswith(s):
            return float(i.split(" ")[1])


main()
