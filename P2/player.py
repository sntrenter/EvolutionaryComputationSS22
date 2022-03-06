from random import random,sample
import numpy as np
class player:

    def __init__(self,size = 50,l = [],fitfunc = None,runFitOnInit = True):
        #TODO: need to implement getters and setters for fitness/mutation
        #self.l = l
        if l == []:
            self.l = np.random.choice([0, 1], size=(size,), p=[.5, .5])
        else:
            self.l = l
        self.fitfunc = fitfunc

        if runFitOnInit == True:
            self.fit = self.fitfunc(self.l)
            self.eval = True
        else:
            self.fit = -1
            self.eval = False

    def print(self):
        print("=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=")
        print("fit: ",self.fit)
        for i in self.l:
            print(i,end="")
        print()
        print("=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=")

    def reCalcFitness(self):
        self.fit =  self.fitfunc(self.l)




def returnPlayer(size = 50,fitfunc = None) -> player:
    p = player(size = size,fitfunc=fitfunc)
    return p


def CreatePopulation(popSize,lsize,fitfunc = None):
    pop = []
    for i in range(int(popSize)):
        pop.append(player(size=lsize,fitfunc=fitfunc))
    return pop

def SortPopulation(pop):
    for i in pop:
        if i.fit == None:
            i.reCalcFitness()
    return sorted(pop, key=lambda x: x.fit,reverse=True)

def Tournament(l,recombination,crossover,mutate,k = 2,g = False,G = False):
    if g or G:
        print("Tournament")
    p1 = SortPopulation(sample(l,k))[0] 
    p2 = SortPopulation(sample(l,k))[0]
    p1,p2 = recombination(p1,p2,crossover,mutate,g = g, G = G)
    if G:
        p1.print()
        p2.print()
    if g or G:
        print("End Tournament")
    return p1,p2

def MutatePlayer(p,g=False,G=False):
    if g or G:
        print("mutate")
    lSizeOverN = 1/len(p.l)
    for i in range(len(p.l)):
        ##print(i," ",p.l[i])
        num = random()
        if num < lSizeOverN:
            if G:
                print("random num",num)
            #print("flip bit")
            if p.l[i] == 1:
                if G:
                    print(i," ",p.l[i],"->",0)
                p.l[i] = 0
            else:
                if G:
                    print(i," ",p.l[i],"->",1)
                p.l[i] = 1
        else:
            if G:
                print(num)
                print(i," ",p.l[i])
    p.fit = p.reCalcFitness()
    #p.print()
    return p

def ElitismReplacement(l,numberToReplace,recombination,k,crossover = .6,mutate = 1.0,g = False,G = False):
    if g or G:
        print("start elitism replacement")
    if G:
        print("population:")
        for i in l:
            i.print()
    l = SortPopulation(l)

    if g or G:
        print("start creating offspring")
    newPlayers = []
    while len(newPlayers) < numberToReplace:
        np1,np2 = Tournament(l,recombination,crossover,mutate,k = k,g=g,G=G)
        newPlayers.append(np1)
        newPlayers.append(np2)
    if len(newPlayers) > numberToReplace: #if want to replace an odd number or something
        newPlayers.pop()
    if G:
        print("New players")
        for i in newPlayers:
            i.print()
    if g or G:
        print("removing the bottom " ,numberToReplace)
    del l[-numberToReplace:] #remove number to replace
    if g or G:
        print("original population remaining")
        for i in l:
            i.print()
    #print(l)
    #print(newPlayers)
    l.extend(newPlayers)

    
    if g or G:
        print("added offspring population... ")
        if G:
            print("full list:")
            for i in l:
                i.print()
    #print("test")
    #print(l)
    if g or G:
        print("returning from elitism replacement (returning sorted population")
    return SortPopulation(l)

