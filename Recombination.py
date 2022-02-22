import random
import sys
from player import player,MutatePlayer
#
#def getValueFromSettings(l, s):
#    for i in l:
#        if i.startswith(s):
#            return float(i.split(" ")[1])
#if len(sys.argv) != 1:
#    for i in sys.argv:
#        if re.search(r"^[\w,\s-]+\.[A-Za-z]{3}$", i):
#            with open(i) as f:
#                paramlist = list(f)
#            randSeed = getValueFromSettings(paramlist, "randSeed")
#            populationSizeN = getValueFromSettings(
#                paramlist, "populationSizeN")
#            stringSizen = getValueFromSettings(paramlist, "stringSizen")
#            probApplyCrossover = getValueFromSettings(
#                paramlist, "probApplyCrossover")
#            probApplyMutation = getValueFromSettings(
#                paramlist, "probApplyMutation")
#            selectionMethod = getValueFromSettings(
#                paramlist, "selectionMethod")
#            tournamentSizek = getValueFromSettings(
#                paramlist, "tournamentSizek")
#            fitnessFunction = getValueFromSettings(
#                paramlist, "fitnessFunction")
#        if i == "-h":
#            h = True
#            print("TODO:help")
#        if i == "-g":
#            g = True
#        if i == "-G":
#            G = True
#else:
#    randSeed = 123
#    populationSizeN = 100
#    stringSizen = 50
#    probApplyCrossover = 0.6
#    probApplyMutation = 1.0
#    selectionMethod = 0
#    tournamentSizek = 2
#    fitnessFunction = 0
#    h = False
#    g = False
#    G = False


def uniformCrossover(p1,p2,probApplyCrossover = .6,mutate = 1.0,g = False,G = False):
    if g or G:
        print("recombination")
    num = random.random()
    if num < probApplyCrossover:
        if g or G:
            print("crossover")
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
        #TODO:add MutatePlayer, might be able to just make it use lists 
        mutnum = random.random()
        if mutnum < mutate:
            return MutatePlayer(player(l = l1)),MutatePlayer(player(l = l2))
        else:
            return player(l = l1),player(l = l2)
    else:
        #print("no crossover")
        return p1,p2



RECOMBINATION_LIST = [uniformCrossover]