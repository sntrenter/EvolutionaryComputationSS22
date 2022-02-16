#!/usr/bin/env python
from ast import Global
import sys
import re
import numpy as np
from player import player,returnPlayer,CreatePopulation,SortPopulation,Tournament,ElitismReplacement
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

def printGeneration(population):
    population = SortPopulation(population)
    #print("len: ",len(population))
    print("Most Fit")
    population[0].print()
    print("least fit")
    population[-1].print()
    allfit = 0
    for i in population:
        allfit += i.fit
    print("avg fit: ",allfit/len(population))

def main():
    generation = 0
    population = CreatePopulation(populationSizeN,stringSizen)
    population = SortPopulation(population)

    while generation < 30:
        print("############################################################")
        print("Generation: ", generation)
        generation += 1
        printGeneration(population)
        population = ElitismReplacement(population,49,uniformCrossover,tournamentSizek)
        print("############################################################")



    print("end")



main()
