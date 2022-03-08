import random
import sys
from player import player,MutatePlayer



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
        mutnum = random.random()
        if mutnum < mutate:
            return MutatePlayer(player(l = l1,fitfunc=p1.fitfunc),g,G),MutatePlayer(player(l = l2,fitfunc=p1.fitfunc),g,G)
        else:
            return player(l = l1,fitfunc=p1.fitfunc),player(l = l2,fitfunc=p1.fitfunc)
    else:
        if g or G:
            print("no crossover")
        return p1,p2

#These don't seem to "need" things like mutations chances and prob apply crossover?
def onePointCrossover(p1,p2):
    pass



def twoPointCrossover(p1,p2):
    pass





RECOMBINATION_LIST = [uniformCrossover]