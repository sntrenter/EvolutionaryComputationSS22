import matplotlib.pyplot as plt
from player import CreatePopulation,SortPopulation,ElitismReplacement,ElitismReplacementDiversityPreservation
from Generational import printGeneration
from Fitness import oneMax,trapFour
from Recombination import uniformCrossover,onePointCrossover,twoPointCrossover

Generation_timeout = 300

#TODO: optimize to keep track of max successful run to stop backtracking
def BisectionRTR(populationSizeN,stringSizen,fitnessFunction,crossoverOperator,tournamentSizek,probApplyCrossover,probApplyMutation,g,G,bisectionTimeout=Generation_timeout,graphing = False,w=None,replacementAmount = None):
    if w == None or replacementAmount == None:
        raise "w not defined"
    
    lowerBound = 1
    upperBound = populationSizeN
    num = upperBound
    l = []
    u = []
    n = []
    
    while True:
        if upperBound == 1:
            print("upper bound converged to 1, very small poplulation sufficient")
            break
        cur_run = runPop(upperBound,stringSizen,fitnessFunction,crossoverOperator,tournamentSizek,probApplyCrossover,probApplyMutation,g,G,bisectionTimeout,w=w,replacementAmount = replacementAmount)
        #print(cur_run)
        if float(upperBound/lowerBound) <= 1.05:
            print("Upper and lower bound close, breaking",num,str(upperBound/lowerBound))
            if graphing:
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



def runPop(populationSizeN,stringSizen,fitnessFunction,crossoverOperator,tournamentSizek,probApplyCrossover,probApplyMutation,g,G,timeout,w=None,replacementAmount = None):
    generation = 0
    population = CreatePopulation(populationSizeN, stringSizen,fitfunc=fitnessFunction)
    population = SortPopulation(population)
    
    #print("###############################")
    while population[0].fit != stringSizen and generation < timeout:  # generation < 1 and
        #print("Generation: ", generation)
        generation += 1
        population = ElitismReplacementDiversityPreservation(
            population, replacementAmount, crossoverOperator, tournamentSizek,crossover=probApplyCrossover, mutate=probApplyMutation, g=g, G=G,w=w)
        #print("###############################")
    #print("best individual at end of simulation")
    #population[0].print()
    #print("Generation Found: ",generation)
    if population[0].fit == stringSizen:
        return True
    else:
        return False

#randSeed = 123
#populationSizeN = 10
#stringSizen = 24
#probApplyCrossover = 0.6
#probApplyMutation = 1.0
#selectionMethod = 0
#tournamentSizek = 2
#fitnessFunction = 0
#crossoverOperator = 0
#h = False
#g = False
#G = False

#Bisection(populationSizeN,stringSizen,oneMax,uniformCrossover,tournamentSizek,probApplyCrossover,probApplyMutation,g,G)
#input()
#Bisection(populationSizeN,stringSizen,oneMax,onePointCrossover,tournamentSizek,probApplyCrossover,probApplyMutation,g,G)
#input()
#Bisection(populationSizeN,stringSizen,oneMax,twoPointCrossover,tournamentSizek,probApplyCrossover,probApplyMutation,g,G)
#input()

#Bisection(populationSizeN,stringSizen,trapFour,uniformCrossover,tournamentSizek,probApplyCrossover,probApplyMutation,g,G)
#input()
#Bisection(populationSizeN,stringSizen,trapFour,onePointCrossover,tournamentSizek,probApplyCrossover,probApplyMutation,g,G)
#input()
#Bisection(populationSizeN,stringSizen,trapFour,twoPointCrossover,tournamentSizek,probApplyCrossover,probApplyMutation,g,G)
#input()
