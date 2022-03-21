import random
import sys
from player import player,MutatePlayer
from Fitness import oneMax


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
#They do need all those things
def onePointCrossover(p1,p2,probApplyCrossover = .6,mutate = 1.0,g = False,G = False):
    ###DELETE
    #g,G = True,True
    #probApplyCrossover = 1
    ###
    if g or G:
        print("one point crossover")
    num = random.random()
    if num < probApplyCrossover:
        if g or G:
            print("crossover")
        #apply crossover
        #print("len")
        mid = random.randint(0,len(p1.l))
        #print(mid)
        #print(len(p1.l))

        #l1 = p1.l[:mid] + p2.l[mid:]
        l1 = [*p1.l[:mid],*p2.l[mid:]]
        #print(l1)
        #l2 = p2.l[:mid] + p1.l[mid:]
        l2 = [*p2.l[:mid],*p1.l[mid:]]
        #print(l2)

        mutnum = random.random()
        if mutnum < mutate:
            return MutatePlayer(player(l = l1,fitfunc=p1.fitfunc),g,G),MutatePlayer(player(l = l2,fitfunc=p1.fitfunc),g,G)
        else:
            return player(l = l1,fitfunc=p1.fitfunc),player(l = l2,fitfunc=p1.fitfunc)
    else:
        if g or G:
            print("no crossover")
        return p1,p2



def twoPointCrossover(p1,p2,probApplyCrossover = .6,mutate = 1.0,g = False,G = False):
    ###DELETE
    #g,G = True,True
    #probApplyCrossover = 1
    #mutate = 0
    ###
    if g or G:
        print("one point crossover")
    num = random.random()
    if num < probApplyCrossover:
        if g or G:
            print("crossover")
        #apply crossover
        #print("len")
        midlist = sorted([random.randint(0,len(p1.l)),random.randint(0,len(p1.l))])
        #print(midlist)
        mid1,mid2 = midlist[0],midlist[1]
        #l1 = p1.l[:mid1] + p2.l[mid1:mid2] + p1.l[mid2:]
        l1 = [*p1.l[:mid1],*p2.l[mid1:mid2],*p1.l[mid2:]]
        #print(l1)
        #l2 = p2.l[:mid1] + p1.l[mid1:mid2] + p2.l[mid2:]
        l2 = [*p2.l[:mid1],*p1.l[mid1:mid2],*p2.l[mid2:]]
        #print(l2)

        mutnum = random.random()
        if mutnum < mutate:
            return MutatePlayer(player(l = l1,fitfunc=p1.fitfunc),g,G),MutatePlayer(player(l = l2,fitfunc=p1.fitfunc),g,G)
        else:
            return player(l = l1,fitfunc=p1.fitfunc),player(l = l2,fitfunc=p1.fitfunc)
    else:
        if g or G:
            print("no crossover")
        return p1,p2


#p1 = player(20,l=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],fitfunc=oneMax,runFitOnInit=True)
#p2 = player(20,l=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],fitfunc=oneMax,runFitOnInit=True)
#p1.print()
#p2.print()
#p3,p4 = twoPointCrossover(p1,p2)
#p3.print()
#p4.print()


RECOMBINATION_LIST = [uniformCrossover,onePointCrossover,twoPointCrossover]