#!/usr/bin/env python
from ast import Global
import sys
import re
import numpy as np
from player import MutatePlayer, player, returnPlayer, CreatePopulation, SortPopulation, Tournament, ElitismReplacement
import random
from Recombination import uniformCrossover, RECOMBINATION_LIST
from Fitness import FITNESS_LIST

def getValueFromSettings(l, s):
    for i in l:
        if i.startswith(s):
            #print(s + ":" + i.split(" ")[1])
            return float(i.split(" ")[1])


randSeed = 123
populationSizeN = 200
stringSizen = 50
probApplyCrossover = 0.6
probApplyMutation = 1.0
selectionMethod = 0
tournamentSizek = 2
fitnessFunction = 0
crossoverOperator = 0
h = False
g = False
G = False


if len(sys.argv) != 1:
    for i in sys.argv:
        if re.search(r"^[\w,\s-]+\.[A-Za-z]{3}$", i):
            print("attempting to parse varialbes from "+ i)
            with open(i) as f:
                paramlist = list(f)
            randSeed = int(getValueFromSettings(paramlist, "randSeed"))
            populationSizeN = int(getValueFromSettings(
                paramlist, "populationSizeN"))
            stringSizen = int(getValueFromSettings(paramlist, "stringSizen"))
            probApplyCrossover = float(getValueFromSettings(
                paramlist, "probApplyCrossover"))
            probApplyMutation = float(getValueFromSettings(
                paramlist, "probApplyMutation"))
            selectionMethod = int(getValueFromSettings(
                paramlist, "selectionMethod"))
            tournamentSizek = int(getValueFromSettings(
                paramlist, "tournamentSizek"))
            fitnessFunction = int(getValueFromSettings(
                paramlist, "fitnessFunction"))
            crossoverOperator = int(getValueFromSettings(
                paramlist, "crossoverOperator"))
        if i == "-h":
            h = True
        if i == "-g":
            g = True
        if i == "-G":
            G = True

try:
    randSeed
    populationSizeN
    stringSizen
    probApplyCrossover
    probApplyMutation
    selectionMethod
    tournamentSizek
    fitnessFunction
    crossoverOperator
    h
    g
    G
except NameError:
    print("It seems that something wasn't defined properly")
    exit()


print("randSeed: " + str(randSeed))
print("populationSizeN: " + str(populationSizeN))
print("stringSizen: " + str(stringSizen))
print("probApplyCrossover: " + str(probApplyCrossover))
print("probApplyMutation: " + str(probApplyMutation))
print("selectionMethod: " + str(selectionMethod))
print("tournamentSizek: " + str(tournamentSizek))
print("fitnessFunction: " + str(fitnessFunction))
print("crossoverOperator: " + str(crossoverOperator))
print("h: " + str(h))
print("g: " + str(g))
print("G: " + str(G))
print("Fitness funtion: " + FITNESS_LIST[fitnessFunction].__name__)
print("Recombination funtion: " + RECOMBINATION_LIST[crossoverOperator].__name__)


def main():

    if h:
        helpInfo()
    if g:
        print("minor logging mode enabled")
    if G:
        print("advanced logging enabled")

    #a = returnPlayer(5,fitfunc=FITNESS_LIST[fitnessFunction])
    #b = returnPlayer(5,fitfunc=FITNESS_LIST[fitnessFunction])
    #a.print()
    #b.print()
    #print()
    #print()
    #print()
    #b.l = [0,1,1,1,1]
    #b.print()
    #b.reCalcFitness()
    #b.print()

    
    #avgfit = []
    generation = 0
    population = CreatePopulation(populationSizeN, stringSizen,fitfunc=FITNESS_LIST[fitnessFunction])
    population = SortPopulation(population)
    
    while population[0].fit != stringSizen:  # generation < 1 and
        print("############################################################")
        print("Generation: ", generation)
        generation += 1
        printGeneration(population)
        fit = 0
        for i in population:
            fit += i.fit
        #avgfit.append(fit/len(population)) This would cause it to end early when not needed
        #if not failsafe(avgfit):           Will implement when needed :) 
        #    break
        population = ElitismReplacement(
            population, len(population) - 1, uniformCrossover, tournamentSizek,crossover=probApplyCrossover, mutate=probApplyMutation, g=g, G=G)
        print("############################################################")
    print("best individual at end of simulation")
    population[0].print()
    print()
    print()
    print()
    

    print("end")


def helpInfo():
    print("help...")
    print("written in python 3.8.10 but should work in most 3+ version")
    print("the generations will stop when the top player has reached a fitness of stringSizen")
    print("can use command line args but also supports the use of a manually setting variables")
    print("you may manually set the variables near the top of the script if desired")
    print("setting file will override any preset variables")
    print("the script should exit if a variable is not set properly")
    print("EXITING...")
    exit()


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
    print("avg fit: ", allfit/len(population))

def failsafe(avgfit):
    if len(avgfit) <= 2:
        return True
    if len(avgfit) > 2 and avgfit[-1] > avgfit[-2]:
        return True
    print("breaking due to avgfit")
    return False
# test()
main()
