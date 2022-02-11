from random import random,sample
import numpy as np
class player:

    def __init__(self,size = 50,l = []):
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
    for i in range(popSize):
        pop.append(player(size=lsize))
    return pop

def SortPopulation(pop):
    return sorted(pop, key=lambda x: x.fit,reverse=True)

def Tournament(l,recombination,k = 2):
    #TODO: print samples to make debugging easier
    p1 = SortPopulation(sample(l,k))[0] 
    p2 = SortPopulation(sample(l,k))[0]
    p1,p2 = recombination(p1,p2)
    return p1,p2

