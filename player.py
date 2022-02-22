from random import random,sample
import numpy as np
class player:

    def __init__(self,size = 50,l = []):
        #TODO: need to implement getters and setters for fitness/mutation
        #self.l = l
        if l == []:
            self.l = np.random.choice([0, 1], size=(size,), p=[.5, .5])
        else:
            self.l = l
        self.fit = sum(self.l)#will need to change this later
        self.eval = True#we eval every time

    def print(self):
        print("=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=")
        print("fit: ",self.fit)
        for i in self.l:
            print(i,end="")
        print()
        print("=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=")

    def hello(self):
        print("hello worl")




def returnPlayer(size = 50) -> player:
    p = player(size = size)
    return p


def CreatePopulation(popSize,lsize):
    pop = []
    for i in range(int(popSize)):
        pop.append(player(size=lsize))
    return pop

def SortPopulation(pop):
    return sorted(pop, key=lambda x: x.fit,reverse=True)

def Tournament(l,recombination,mutate,k = 2,g = False,G = False):
    #TODO: print samples to make debugging easier
    p1 = SortPopulation(sample(l,k))[0] 
    p2 = SortPopulation(sample(l,k))[0]
    p1,p2 = recombination(p1,p2,mutate,g = g, G = G)
    return p1,p2

def MutatePlayer(p: player):
    #print("mutate")
    lSizeOverN = 1/len(p.l)
    for i in range(len(p.l)):
        ##print(i," ",p.l[i])
        num = random()
        if num < lSizeOverN:
            #print(num)
            #print("flip bit")
            if p.l[i] == 1:
                #print(i," ",p.l[i],"->",0)
                p.l[i] = 0
            else:
                #print(i," ",p.l[i],"->",1)
                p.l[i] = 1
        else:
            pass
            #print(i," ",p.l[i])
    p.fit = sum(p.l)
    #p.print()
    return p

def ElitismReplacement(l,numberToReplace,recombination,k,mutate = 1.0,g = False,G = False):
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
        np1,np2 = Tournament(l,recombination,mutate,k = k)
        newPlayers.append(np1)
        newPlayers.append(np2)
    if len(newPlayers) > numberToReplace: #if want to replace an odd number or something
        newPlayers.pop()

    #for i in newPlayers:
    #    i.print()
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

