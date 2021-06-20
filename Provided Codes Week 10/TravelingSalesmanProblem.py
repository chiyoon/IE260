from GeneticAlgorithmProblem import *
import random
import math
import time
import csv

class TravelingSalesmanProblem(GeneticAlgorithmProblem):
    
    genes = []
    dicLocations = {}
    gui = ''
    best = ''
    time = 0
    
    def __init__(self, data_mode,csvfile,numCities, height, width, time):
        self.time = time
        if data_mode == 'Random':
            for itr in range(numCities):
                x = random.uniform(0, width)
                y = random.uniform(0, height)
                coordinate = [x, y]
                self.dicLocations[itr] = coordinate
        elif data_mode == 'Load':
            with open(csvfile, 'r') as my_csv:
                contents = list(csv.reader(my_csv, delimiter=","))
                for itr in range(len(contents)):
                    x , y= contents[itr][0],contents[itr][1]
                    self.dicLocations[itr] = [float(x),float(y)]
    def registerGUI(self, gui):
        self.gui = gui

    def performEvolution(self, numIterations, numOffsprings, numPopulation, mutationFactor):
        if self.gui != '':
            self.gui.start()

        startTime = time.time()
        population = self.createInitialPopulation(numPopulation, len(self.dicLocations.keys()))
        while True:
            currentTime = time.time()
            if (currentTime - startTime) >= self.time:
                break
            offsprings = {}
            for itr in range(numOffsprings):
                # Put a correct method name and an argument
                # HInt: You need a parent to create an offspring
                p1, p2 = self.selectParents(population)

                # After selecting a parent pair, you need to create
                # an offspring. How to do that?
                # Hint: You need to exchange the genotypes from parents
                offsprings[itr] = self.crossover(p1, p2)
                factor = int(mutationFactor * len(self.dicLocations.keys()))

                # You need to add a little bit of chagnes in the
                # genotype to see a potential random evolution
                # this does not need information from either population
                # or parent
                self.mutation(offsprings[itr], factor)

                # After creating an offspring set, what do you have to
                # perform?
                # HINT: You need to put the offspring in the population
            population = self.createInitialPopulation(population, offsprings)

            # which method do you need to use the best solution? and
            # from where?
            mostFittest = self.findBestSolution(population)
            self.best = mostFittest
            print(self.calculateTotalDistance(self.best))
            if self.gui != '':
                self.gui.update()

        endTime = time.time()
        return self.best.getGenotype(), self.fitness(self.best), self.calculateTotalDistance(self.best), (endTime - startTime)

    def fitness(self, instance):
        genotype = instance.getGenotype()
        currentCity = 0
        distance = 0.0
        for itr in range(len(genotype)-1):
            nextCity = genotype[currentCity]
            distance = distance + self.calculateDistance(self.dicLocations[currentCity], self.dicLocations[nextCity])
            currentCity = nextCity
        utility = 10000.0 / distance
        return utility
    
    def calculateTotalDistance(self, instance):
        # This genotype is created based upon a position based encoding
		# Fill in the following blanks to complete this method
        genotype = instance.getGenotype()
        currentCity = 0
        distance = 0.0
        for itr in range(len(genotype)-1):
            nextCity = genotype[currentCity]
            current = self.dicLocations[currentCity]
            next = self.dicLocations[nextCity]
            distance = distance + self.calculateDistance(current,nextCity)
            currentCity = nextCity
        return distance
    
    def calculateDistance(self, coordinate1, coordinate2):
        # how to calculate the distance between two cities?
		# how to calculate the squre and the square root?
        distance = math.sqrt( math.pow(coordinate1[0]-coordinate2[0], 2) + math.pow(coordinate1[1]-coordinate2[1], 2) )
        return distance

    def getPotentialGenes(self):
        return self.dicLocations.keys()

    def createInitialPopulation(self, numPopulation, numCities):
        population = []
        for itr in range(numPopulation):
            genotype = list(range(numCities))
            while self.isInfeasible(genotype) == False:
                random.shuffle(genotype)
            instance = GeneticAlgorithmInstance()
            instance.setGenotype(genotype)
            population.append( instance )
        return population
        
    def isInfeasible(self, genotype):
        currentCity = 0
        visitedCity = {}
        for itr in range(len(genotype)):
            visitedCity[currentCity] = 1
            currentCity = genotype[currentCity]
            
        if len(visitedCity.keys()) == len(genotype): 
            return True
        else:
            return False
        
    def findBestSolution(self, population):
        idxMaximum = -1
        max = -99999
        for itr in range(len(population)):
            if max < self.fitness(population[itr]):
                max = self.fitness(population[itr])
                idxMaximum = itr
        return population[idxMaximum]
    
    def selectParents(self, population):
        rankFitness = {}
        originalFitness = {}
        maxUtility = -999999
        minUtility = 999999
        for itr in range(len(population)):
            originalFitness[itr] = self.fitness( population[itr] )
            if maxUtility < originalFitness[itr]:
                maxUtility = originalFitness[itr]
            if minUtility > originalFitness[itr]:
                minUtility = originalFitness[itr]
        for itr1 in range(len(population)):
            for itr2 in range(itr1+1,len(population)):
                if originalFitness[itr1] < originalFitness[itr2]:
                    originalFitness[itr1], originalFitness[itr2] = originalFitness[itr2], originalFitness[itr1]
                    population[itr1], population[itr2] = population[itr2], population[itr1]
        size = float(len(population))
        total = 0.0
        for itr in range(len(population)):
            rankFitness[itr] = ( maxUtility + (float(itr) - 1.0)* (maxUtility - minUtility)) / ( size - 1 )
            total = total + rankFitness[itr]
        
        idx1 = -1
        idx2 = -1
        while idx1 == idx2:
            dart = random.uniform(0, total)
            sum = 0.0
            for itr in range(len(population)):
                sum = sum + rankFitness[itr]
                if dart <= sum:
                    idx1 = itr
                    break
            dart = random.uniform(0, total)
            sum = 0.0
            for itr in range(len(population)):
                sum = sum + rankFitness[itr]
                if dart <= sum:
                    idx2 = itr
                    break
        return population[idx1], population[idx2]
            
    def crossoverParents(self, instance1, instance2):
        genotype1 = instance1.getGenotype()
        genotype2 = instance2.getGenotype()
        newInstance = GeneticAlgorithmInstance()
        
        dicNeighbor = {}
        for itr in range(len(genotype1)):
            neighbor = {}
            neighbor1 = self.getNeighborCity(instance1, itr)
            neighbor2 = self.getNeighborCity(instance2, itr)
            neighbor[neighbor1[0]] = 1
            neighbor[neighbor1[1]] = 1
            neighbor[neighbor2[0]] = 1
            neighbor[neighbor2[1]] = 1
            dicNeighbor[itr] = neighbor.keys()
        
        currentCity = 0
        visitedCity = {}
        path = {}
        for itr in range(len(genotype1)):
            visitedCity[currentCity] = 1
            nextCity = self.getMinimumNeighborNotVisitedCity(list(visitedCity.keys()), dicNeighbor)
            if nextCity == -1:
                nextCity = 0
            path[currentCity] = nextCity
            currentCity = nextCity
            
        newInstance.setGenotype(path)
        
        return newInstance       
    
    def getMinimumNeighborNotVisitedCity(self, lstVisitedCity, dicNeighbor):
        cities = list(dicNeighbor.keys())
        for itr in range(len(lstVisitedCity)):
            cities.remove(lstVisitedCity[itr])
        minimum = 999
        candidates = []
        for itr in range(len(cities)):
            location = cities[itr]
            if len(dicNeighbor[location]) <= minimum:
                minimum = len(dicNeighbor[location])
                candidates.append(location)
        random.shuffle(candidates)
        if len(candidates) == 0:
            return -1
        return candidates[0]
        
    def getNeighborCity(self, instance, currentCity):
        
        genotype = instance.getGenotype()
        ret1 = -1
        ret2 = -1
        for itr in range(len(genotype)):
            if genotype[itr] == currentCity:
                ret1 = itr
                break
        ret2 = genotype[currentCity]
        neighbor = [ret1, ret2]
        return neighbor
    
    def mutation(self, instance, factor):
        genotype = instance.getGenotype()
        mutationDone = False
        while mutationDone == True:
            for itr in range(factor):
                idxSwap1 = random.randint(0, len(genotype))
                idxSwap2 = random.randint(0, len(genotype))
                genotype[idxSwap1], genotype[idxSwap2] = genotype[idxSwap2], genotype[idxSwap1]
            if self.isInfeasible(genotype) == True:
                mutationDone = False
            else:
                mutationDone = True
        instance.setGenotype(genotype)
         
    def substitutePopulation(self, population, children):
        for itr1 in range(len(population)):
            for itr2 in range(itr1+1,len(population)):
                if self.fitness(population[itr1]) < self.fitness(population[itr2]):
                    population[itr1], population[itr2] = population[itr2], population[itr1]
        for itr in range(len(children)):
            population[len(population)-len(children)+itr] = children[itr]
        return population
