#!/usr/bin/env python
#Sam Trenter
from ast import Global
import sys
import re
import numpy as np
from player import MutatePlayer, player, returnPlayer, CreatePopulation, SortPopulation, Tournament, ElitismReplacement
import random
from Recombination import uniformCrossover, RECOMBINATION_LIST
from Fitness import FITNESS_LIST
from Generational import Generational
from Bisection import Bisection
from DiversityPreservation import DiversityPreservation




def getValueFromSettings(l, s):
    for i in l:
        if i.startswith(s):
            #print(s + ":" + i.split(" ")[1])
            return float(i.split(" ")[1])


randSeed = 123
populationSizeN = 100
stringSizen = 20
probApplyCrossover = 1
probApplyMutation = 1.0
selectionMethod = 0
tournamentSizek = 2
fitnessFunction = 2
crossoverOperator = 0
h = False
g = False
G = False
runmode = 2
bisectionTimeout = 1000
# add below to settingsfile
pauseAtBeginning = False #this just shows you all variables at beginning
graphing = True
w = 25 #int(stringSizen * 1)
replacementAmount=populationSizeN / 1


if len(sys.argv) != 1:
    for i in sys.argv:
        if re.search(r"^[\w,\s-]+\.[A-Za-z]{3}$", i):
            print("attempting to parse varialbes from " + i)
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
            runmode = int(getValueFromSettings(
                paramlist, "runmode"))
            bisectionTimeout = int(getValueFromSettings(
                paramlist, "bisectionTimeout"))
        if i == "-h":
            h = True
        if i == "-g":
            g = True
        if i == "-G":
            G = True
        if i == "-p":
            pauseAtBeginning = True

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
print("Recombination funtion: " +
      RECOMBINATION_LIST[crossoverOperator].__name__)
print("runmode: " + str(runmode))
print("bisectionTimeout: " + str(bisectionTimeout))
print("w: " + str(w))

def main():
    if pauseAtBeginning:
        input("press any key to continue...")
    if h:
        helpInfo()
    if g:
        print("minor logging mode enabled")
    if G:
        print("advanced logging enabled")

    #a = returnPlayer(5,fitfunc=FITNESS_LIST[fitnessFunction])
    #b = returnPlayer(5,fitfunc=FITNESS_LIST[fitnessFunction])
    # a.print()
    # b.print()
    # print()
    # print()
    # print()
    #b.l = [0,1,1,1,1]
    # b.print()
    # b.reCalcFitness()
    # b.print()

    if(runmode == 0):
        print("Running Generational Mode...")
        Generational(populationSizeN, stringSizen, FITNESS_LIST[fitnessFunction], RECOMBINATION_LIST[
                     crossoverOperator], tournamentSizek, probApplyCrossover, probApplyMutation, g, G)

    if(runmode == 1):
        print("Running in Bisection Mode...")
        Bisection(populationSizeN, stringSizen, FITNESS_LIST[fitnessFunction], RECOMBINATION_LIST[crossoverOperator],
                  tournamentSizek, probApplyCrossover, probApplyMutation, g, G, bisectionTimeout=bisectionTimeout,graph = graphing)

    if(runmode == 2):
        print("Running in diversity preservation mode...")
        DiversityPreservation(populationSizeN, stringSizen, FITNESS_LIST[fitnessFunction], RECOMBINATION_LIST[
                     crossoverOperator], tournamentSizek, probApplyCrossover, probApplyMutation, g, G,graphing=graphing,w=w,replacementAmount=replacementAmount)


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
