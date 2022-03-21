import matplotlib.pyplot as plt
from player import CreatePopulation,SortPopulation,ElitismReplacement
from Generational import printGeneration
from Fitness import oneMax,trapFour
from Recombination import uniformCrossover,onePointCrossover,twoPointCrossover

Generation_timeout = 500


def Bisection(populationSizeN,stringSizen,fitnessFunction,crossoverOperator,tournamentSizek,probApplyCrossover,probApplyMutation,g,G):
    lowerBound = 1
    upperBound = populationSizeN
    num = upperBound
    l = []
    u = []
    n = []
    
    while True:
        cur_run = runPop(upperBound,stringSizen,fitnessFunction,crossoverOperator,tournamentSizek,probApplyCrossover,probApplyMutation,g,G)
        #print(cur_run)
        if float(upperBound/lowerBound) <= 1.05:
            print("Upper and lower bound close, breaking",num,str(upperBound/lowerBound))
            plt.plot(l)
            plt.plot(u)
            plt.plot(n)
            plt.show()
            break;    
        elif cur_run == False:
            print("Max not Found!",num,str(upperBound/lowerBound))
            lowerBound = upperBound
            upperBound *= 2
            num = upperBound
            l.append(lowerBound)
            u.append(upperBound)
            n.append(num)  

        elif cur_run == True:
            print("Found Max!",num,str(upperBound/lowerBound))
            #lowerbound = same
            #over = True
            upperBound = int((upperBound + lowerBound)/2)
            num = upperBound        
            l.append(lowerBound)
            u.append(upperBound)
            n.append(num)
    print("for String size: ", stringSizen)
    print("Problem solved when population size is ",upperBound)
    #print(runPop(populationSizeN,stringSizen,fitnessFunction,crossoverOperator,tournamentSizek,probApplyCrossover,probApplyMutation,g,G))



def runPop(populationSizeN,stringSizen,fitnessFunction,crossoverOperator,tournamentSizek,probApplyCrossover,probApplyMutation,g,G):
    generation = 0
    population = CreatePopulation(populationSizeN, stringSizen,fitfunc=fitnessFunction)
    population = SortPopulation(population)
    
    #print("###############################")
    while population[0].fit != stringSizen and generation < Generation_timeout:  # generation < 1 and
        #print("Generation: ", generation)
        generation += 1
        population = ElitismReplacement(
            population, len(population) - 1, crossoverOperator, tournamentSizek,crossover=probApplyCrossover, mutate=probApplyMutation, g=g, G=G)
        #print("###############################")
    #print("best individual at end of simulation")
    #population[0].print()
    print("Generation Found: ",generation)
    if population[0].fit == stringSizen:
        return True
    else:
        return False

randSeed = 123
populationSizeN = 10
stringSizen = 24
probApplyCrossover = 0.6
probApplyMutation = 1.0
selectionMethod = 0
tournamentSizek = 2
fitnessFunction = 0
crossoverOperator = 0
h = False
g = False
G = False

Bisection(populationSizeN,stringSizen,trapFour,twoPointCrossover,tournamentSizek,probApplyCrossover,probApplyMutation,g,G)