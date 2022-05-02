from Fitness import oneMax,trapFour
import numpy as np
import random
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #for testing, ignore
    randSeed = 123
    populationSizeN = 10000
    stringSizen = 40
    probApplyCrossover = 1
    probApplyMutation = 1.0
    selectionMethod = 0
    tournamentSizek = 2
    fitnessFunction = 0
    crossoverOperator = 0
    h = False
    g = False
    G = False
    runmode = 4
    bisectionTimeout = 500
    # add below to settingsfile
    pauseAtBeginning = False #this just shows you all variables at beginning
    graphing = True
    w = 25 #int(stringSizen * 1)
    replacementAmount=populationSizeN 


#Generational(populationSizeN, stringSizen, FITNESS_LIST[fitnessFunction], RECOMBINATION_LIST[crossoverOperator], tournamentSizek, probApplyCrossover, probApplyMutation, g, G)
def CompactGA(populationSizeN, stringSizen,fitnessFunction,graphing):

    gen = 0
    popArray = np.full(shape=stringSizen,fill_value=.5)
    graphArray = []

    #loop here
    while mostlyConverged(popArray):#sum(popArray) != stringSizen: #gen < 10000 and 
        print(gen)
        print(int(sum(popArray)))

        graphArray.append(popArray.copy())

        oldar = popArray.copy()
        gen += 1
        #print(popArray)
        p1 = createList(popArray)
        #print(p1)
        #print(fitnessFunction(p1))
        p2 = createList(popArray)
        #print(p2)
        #print(fitnessFunction(p2))

        if fitnessFunction(p1) >= fitnessFunction(p2):
            #print("p1 greater or equal")
            for i in range(len(popArray)):
                if p1[i] == 1:
                    popArray[i] += 1/populationSizeN
                else:
                    popArray[i] -= 1/populationSizeN
        else:
            #print("p2 greater")
            for i in range(len(popArray)):
                if p2[i] == 1:
                    popArray[i] += 1/populationSizeN
                else:
                    popArray[i] -= 1/populationSizeN
        for i in range(len(popArray)):
            if popArray[i] > 1:
                popArray[i] = 1
            if popArray[i] < 0:
                popArray[i] = 0
        #print(oldar)
        print("old array:",sum(oldar))
        #print(popArray)
        print("new array:",sum(popArray))

        print("||||||||||||||||||||||||||")
    #graph
    if graphing:
        plt.imshow(graphArray)
        plt.show()
    print(oldar)
    print("old array:",sum(oldar))
    print(popArray)
    print("new array:",sum(popArray))




def createList(popArray):
    newArray = []
    for i in popArray:
        if random.random() > i:
            newArray.append(0)
        else:
            newArray.append(1)
    return newArray


def mostlyConverged(array):
    for i in array:
        if i < .01 or i > .99:
            continue
        else:
            return True

    return False


if __name__ == "__main__":
    #for testing, ignore
    print(createList([.9,0]))
    print(createList([.9,0]))
    print(createList([0,1]))
    print(createList([0,1]))


    CompactGA(populationSizeN=populationSizeN,stringSizen=stringSizen,fitnessFunction=oneMax,graphing=graphing)
    print("EOF")