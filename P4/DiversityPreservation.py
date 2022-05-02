from player import CreatePopulation, SortPopulation, ElitismReplacementDiversityPreservation
import matplotlib.pyplot as plt


def DiversityPreservation(populationSizeN, stringSizen, fitnessFunction, crossoverOperator, tournamentSizek, probApplyCrossover, probApplyMutation, g, G, graphing=False,w=None,replacementAmount=None):
    if w == None:
        w = int(stringSizen*.10)
    if replacementAmount == None:
        raise "you didn't define something right"
    lowfit = []
    avgfit = []
    highfit = []
    top25 = []
    bottom25 = []

    foundMax = False
    generation = 0
    population = CreatePopulation(
        populationSizeN, stringSizen, fitfunc=fitnessFunction)
    population = SortPopulation(population)
    
    print("###############################")
    while population[0].fit != stringSizen:  # generation < 1 and
        if generation == 1000:
            print("Could not converge! BREAKING")
            break;
        print("Generation: ", generation)
        generation += 1
        if (generation + 1) % 10 == 0:
            printGeneration(population)
        #graphing stuff
        fit = 0
        for i in population:
            fit += i.fit
        avgfit.append(fit/len(population)) 
        highfit.append(population[0].fit)
        lowfit.append(population[-1].fit)
        t25 = 0
        b25 = 0
        for i in population[:int(len(population)*.25)]:
            t25 += i.fit
        for i in range(int(len(population)*.25)):#population[:int(len(population)*.25):-1]:
            b25 += population[-1*i].fit
        top25.append(t25/int(len(population)*.25))
        bottom25.append(b25/int(len(population)*.25))

        #next generation
        population = ElitismReplacementDiversityPreservation(
            population, replacementAmount, crossoverOperator, tournamentSizek, crossover=probApplyCrossover, mutate=probApplyMutation, g=g, G=G, w=w)
        #print("###############################")
    fit = 0
    for i in population:
        fit += i.fit
    avgfit.append(fit/len(population)) 
    highfit.append(population[0].fit)
    lowfit.append(population[-1].fit)
    t25 = 0
    b25 = 0
    for i in population[:int(len(population)*.25)]:
        t25 += i.fit
    for i in range(int(len(population)*.25)):#population[:int(len(population)*.25):-1]:
        b25 += population[-1*i].fit
    top25.append(t25/int(len(population)*.25))
    bottom25.append(b25/int(len(population)*.25))
    print("best individual at end of simulation")
    population[0].print()
    print()
    print()
    print()
    if graphing:
        plt.plot(lowfit)
        plt.plot(avgfit)
        plt.plot(highfit)
        plt.plot(top25)
        plt.plot(bottom25)
        plt.legend(['lowest fitness', 'average fitness','highest fitness','top 25%','bottom 25%'], loc='lower right')
        plt.show()


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
