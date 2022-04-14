from player import CreatePopulation,SortPopulation,ElitismReplacement



def DiversityPreservation(populationSizeN,stringSizen,fitnessFunction,crossoverOperator,tournamentSizek,probApplyCrossover,probApplyMutation,g,G,graphing = False):
    avgfit = []
    foundMax = False
    generation = 0
    population = CreatePopulation(populationSizeN, stringSizen,fitfunc=fitnessFunction)
    population = SortPopulation(population)
    
    while population[0].fit != stringSizen:  # generation < 1 and
        print("###############################")
        print("Generation: ", generation)
        generation += 1
        printGeneration(population)
        #fit = 0
        #for i in population:
        #    fit += i.fit
        #avgfit.append(fit/len(population)) This would cause it to end early when not needed
        #if not failsafe(avgfit):           Will implement when needed :) 
        #    break
        population = ElitismReplacement(
            population, len(population) - 1, crossoverOperator, tournamentSizek,crossover=probApplyCrossover, mutate=probApplyMutation, g=g, G=G)
        print("###############################")
    print("best individual at end of simulation")
    population[0].print()
    print()
    print()
    print()


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