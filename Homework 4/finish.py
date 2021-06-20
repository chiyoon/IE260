from GeneticAlgorithmProblem import *
import random
import math
import time
import csv
import matplotlib.pyplot as plt


class TravelingSalesmanProblem(GeneticAlgorithmProblem):
    genes = []
    dicLocations = {}
    gui = ''
    best = ''
    bestList = []
    time = 0

    def __init__(self, data_mode, csvfile, numCities, height, width, time):
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
                    x, y = contents[itr][0], contents[itr][1]
                    self.dicLocations[itr] = [float(x), float(y)]

    def registerGUI(self, gui):
        self.gui = gui

    def performEvolution(self, numIterations, numOffsprings, numPopulation, mutationFactor):
        if self.gui != '':
            self.gui.start()
        iterate = 0
        num = numOffsprings
        startTime = time.time()
        population = self.createInitialPopulation(numPopulation, len(self.dicLocations.keys()))
        # print("-----init------")
        # for i in range(len(population)):
        #     print(population[i].getGenotype())
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

                # Plan 1
                # offsprings[itr] = self.crossoverParents(p1, p2)

                # Plan 2
                # offsprings[itr] = self.crossoverParents1(p1, p2)

                # Plan 3
                # if time.time() - startTime <= 60:
                #     offsprings[itr] = self.crossoverParents(p1, p2)
                # else:
                #     offsprings[itr] = self.crossoverParents1(p1, p2)

                # Plan 4
                # offsprings[itr] = self.crossoverParents2(p1, p2)

                # Plan 5
                # if time.time() - startTime <= 60:
                #     offsprings[itr] = self.crossoverParents(p1, p2)
                # elif time.time() - startTime > 60 and time.time() - startTime <= 120:
                #     offsprings[itr] = self.crossoverParents2(p1, p2)
                # else:
                #     offsprings[itr] = self.crossoverParents1(p1, p2)

                # Plan 6
                # if time.time() - startTime <= 20:
                #     offsprings[itr] = self.crossoverParents(p1, p2)
                # elif time.time() - startTime > 20 and time.time() - startTime <= 60:
                #     offsprings[itr] = self.crossoverParents2(p1, p2)
                # else:
                #     offsprings[itr] = self.crossoverParents1(p1, p2)

                # Plan 7
                if time.time() - startTime <= 30:
                    offsprings[itr] = self.crossoverParents2(p1, p2)
                else:
                    offsprings[itr] = self.crossoverParents1(p1, p2)

                factor = int(mutationFactor * len(self.dicLocations.keys()))
                # You need to add a little bit of chagnes in the
                # genotype to see a potential random evolution
                # this does not need information from either population
                # or parent

                # self.mutation(offsprings[itr], factor)

                mutation = mutationFactor - float(iterate / 10000)
                if mutation <= 0.001:
                    mutation = 0.001
                self.mutation1(offsprings[itr], mutation)

                # After creating an offspring set, what do you have to
                # perform?
                # HINT: You need to put the offspring in the population

            # population = self.substitutePopulation(population, offsprings)

            popNum = int(float((-num / 180) * (time.time() - startTime)) + num)
            # print(popNum)
            if popNum <= 1:
                popNum = 1
            population = self.substitutePopulationNum(population, offsprings, popNum)

            # print(population[0].getGenotype())
            # which method do you need to use the best solution? and
            # from where?
            mostFittest = self.findBestSolution(population)
            self.best = mostFittest
            self.bestList.append((self.best, time.time() - startTime))
            # print("-----iter------")
            # print(popNum)
            # for i in range(len(population)):
            #     print(population[i].getGenotype())
            print(self.calculateTotalDistance(self.best))
            iterate = iterate + 1
            if self.gui != '':
                self.gui.update()
        endTime = time.time()
        if type(self.best.getGenotype()) == list:
            Dic = self.listIntoDic(self.best.getGenotype())
            self.best.setGenotype(Dic)
        print(iterate)
        return self.best.getGenotype(), self.fitness(self.best), self.calculateTotalDistance(self.best), (
                    endTime - startTime)

    def fitness(self, instance):
        genotype = instance.getGenotype()
        currentCity = 0
        distance = 0.0
        for itr in range(len(genotype) - 1):
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
        for itr in range(len(genotype) - 1):
            nextCity = genotype[currentCity]
            current = self.dicLocations[currentCity]
            next = self.dicLocations[nextCity]
            distance = distance + self.calculateDistance(current, next)
            currentCity = nextCity
        return distance

    def calculateDistance(self, coordinate1, coordinate2):
        # how to calculate the distance between two cities?
        # how to calculate the squre and the square root?
        distance = math.sqrt(
            math.pow(coordinate1[0] - coordinate2[0], 2) + math.pow(coordinate1[1] - coordinate2[1], 2))
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
            population.append(instance)
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
            originalFitness[itr] = self.fitness(population[itr])
            if maxUtility < originalFitness[itr]:
                maxUtility = originalFitness[itr]
            if minUtility > originalFitness[itr]:
                minUtility = originalFitness[itr]
        for itr1 in range(len(population)):
            for itr2 in range(itr1 + 1, len(population)):
                if originalFitness[itr1] < originalFitness[itr2]:
                    originalFitness[itr1], originalFitness[itr2] = originalFitness[itr2], originalFitness[itr1]
                    population[itr1], population[itr2] = population[itr2], population[itr1]
        size = float(len(population))
        total = 0.0
        for itr in range(len(population)):
            rankFitness[itr] = (maxUtility + (float(itr) - 1.0) * (maxUtility - minUtility)) / (size - 1)
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

    def crossoverParents1(self, instance1, instance2):
        genotype1 = instance1.getGenotype()
        genotype2 = instance2.getGenotype()
        # print(genotype1, genotype2)
        if type(genotype1) == list:
            genotype1 = self.listIntoDic(genotype1)
        if type(genotype2) == list:
            genotype2 = self.listIntoDic(genotype2)
        # print(genotype1, genotype2)
        pathGeno1 = self.dicIntoPath(genotype1)
        pathGeno2 = self.dicIntoPath(genotype2)
        lenpath1 = len(pathGeno1)
        lenpath2 = len(pathGeno2)
        # print(pathGeno1, pathGeno2)
        temp1 = [0] * lenpath1
        temp2 = [0] * lenpath2

        pathGeno1 = pathGeno1[1:len(pathGeno1) - 1]
        pathGeno2 = pathGeno2[1:len(pathGeno2) - 1]
        # print(pathGeno1, pathGeno2)

        newInstance = GeneticAlgorithmInstance()

        crossInd = random.randint(0, len(pathGeno1) - 1)

        leftList1 = pathGeno1[0:crossInd]
        rightList1 = pathGeno1[crossInd:]
        leftList2 = pathGeno2[0:crossInd]
        rightList2 = pathGeno2[crossInd:]

        # print(leftList1, rightList1, leftList2, rightList2)

        for i in range(len(rightList2)):
            if rightList2[i] in pathGeno1:
                common = rightList2[i]
                pathGeno1.remove(common)
        # print(pathGeno1)
        for i in range(len(rightList1)):
            if rightList1[i] in pathGeno2:
                common = rightList1[i]
                pathGeno2.remove(common)
        # print(pathGeno2)

        temp1[crossInd + 1:len(temp1) - 1] = rightList2
        # print(temp1)
        temp1[1:crossInd + 1] = pathGeno1
        # print(temp1)
        temp2[crossInd + 1:len(temp2) - 1] = rightList1
        # print(temp2)
        temp2[1:crossInd + 1] = pathGeno2
        # print(temp2)
        # print(temp1)
        # print(temp2)

        rand = random.randint(0, 1)
        if rand == 0:
            dic = self.pathIntoDic(temp1)
        else:
            dic = self.pathIntoDic(temp2)

        newInstance.setGenotype(dic)
        # print(newInstance.getGenotype())
        return newInstance

    def crossoverParents2(self, instance1, instance2):
        genotype1 = instance1.getGenotype()
        genotype2 = instance2.getGenotype()

        if type(genotype1) == list:
            genotype1 = self.listIntoDic(genotype1)
        if type(genotype2) == list:
            genotype2 = self.listIntoDic(genotype2)

        pathGeno1 = self.dicIntoPath(genotype1)
        pathGeno2 = self.dicIntoPath(genotype2)
        # print(pathGeno1, pathGeno2)

        lenpath1 = len(pathGeno1)
        lenpath2 = len(pathGeno2)

        temp1 = [0] * lenpath1
        temp2 = [0] * lenpath2

        pathGeno1 = pathGeno1[1:len(pathGeno1) - 1]
        pathGeno2 = pathGeno2[1:len(pathGeno2) - 1]
        # print(pathGeno1, pathGeno2)

        crossInd1 = -1
        crossInd2 = -1
        while crossInd1 == crossInd2:
            crossInd1 = random.randint(0, len(pathGeno1) - 1)
            crossInd2 = random.randint(0, len(pathGeno1) - 1)
        temp = [crossInd1, crossInd2]
        temp.sort()
        crossInd1 = temp[0]
        crossInd2 = temp[1]
        # print(crossInd1, crossInd2)

        swap1 = pathGeno1[crossInd1:crossInd2 + 1]
        swap2 = pathGeno2[crossInd1:crossInd2 + 1]
        # print(swap1, swap2)

        for i in range(len(swap2)):
            if swap2[i] in pathGeno1:
                common = swap2[i]
                pathGeno1.remove(common)
        # print(pathGeno1)

        for i in range(len(swap1)):
            if swap1[i] in pathGeno2:
                common = swap1[i]
                pathGeno2.remove(common)
        # print(pathGeno2)

        temp1[1:crossInd1 + 1] = pathGeno1[0:crossInd1]
        # print(temp1)
        temp1[crossInd1 + 1:crossInd2 + 2] = swap2
        # print(temp1)
        temp1[crossInd2 + 2:len(temp1) - 1] = pathGeno1[crossInd1:]
        # print(temp1, len(temp1))
        temp2[1:crossInd1 + 1] = pathGeno2[0:crossInd1]
        # print(temp2)
        temp2[crossInd1 + 1:crossInd2 + 2] = swap1
        # print(temp2)
        temp2[crossInd2 + 2:len(temp2) - 1] = pathGeno2[crossInd1:]
        # print(temp2, len(temp2))

        rand = random.randint(0, 1)
        if rand == 0:
            # if len(temp1) != 21:
            #     print('-------------------------------')
            # print(temp1)
            dic = self.pathIntoDic(temp1)
        else:
            # if len(temp2) != 21:
            #     print('-------------------------------')
            # print(temp2)
            dic = self.pathIntoDic(temp2)

        newInstance = GeneticAlgorithmInstance()
        newInstance.setGenotype(dic)

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

    def mutation1(self, instance, factor):
        genotype = instance.getGenotype()
        listgenotype = self.dicIntoPath(genotype)
        mutation = random.random()
        if mutation <= factor:
            # print("mutation")
            # print(genotype)
            # print(listgenotype)
            mutationindex1 = -1
            mutationindex2 = -1
            while mutationindex1 == mutationindex2:
                mutationindex1 = random.randint(1, len(listgenotype) - 2)
                mutationindex2 = random.randint(1, len(listgenotype) - 2)
            mutationgene1 = listgenotype[mutationindex1]
            mutationgene2 = listgenotype[mutationindex2]
            listgenotype[mutationindex1] = mutationgene2
            listgenotype[mutationindex2] = mutationgene1
            # print(listgenotype)
        temp = self.pathIntoDic(listgenotype)
        # print(temp)
        instance.setGenotype(temp)

    def substitutePopulation(self, population, children):
        for itr1 in range(len(population)):
            for itr2 in range(itr1 + 1, len(population)):
                if self.fitness(population[itr1]) < self.fitness(population[itr2]):
                    population[itr1], population[itr2] = population[itr2], population[itr1]
        # temp = []
        # for i in range(len(population)):
        #     temp.append(self.fitness(population[i]))
        # print(temp)
        for itr in range(len(children)):
            population[len(population) - len(children) + itr] = children[itr]
        # temp = []
        # for i in range(len(population)):
        #     temp.append(self.fitness(population[i]))
        # print(temp)
        return population

    def substitutePopulationNum(self, population, children, num):
        for itr1 in range(len(population)):
            for itr2 in range(itr1 + 1, len(population)):
                if self.fitness(population[itr1]) < self.fitness(population[itr2]):
                    population[itr1], population[itr2] = population[itr2], population[itr1]
        # temp = []
        # for i in range(len(population)):
        #     temp.append(self.fitness(population[i]))
        # print(temp)

        childIndex = random.randint(0, len(children) - num)
        for i in range(num):
            population[-num + i] = children[childIndex + i]

        # temp = []
        # for i in range(len(population)):
        #     temp.append(self.fitness(population[i]))
        # print(temp)
        return population

    def listIntoDic(self, list):
        list = list
        dic = {}
        itr = 0
        current = 0
        while itr < len(list):
            dic[current] = list[current]
            current = list[current]
            itr = itr + 1
        return dic

    def pathIntoDic(self, list):
        lst = list
        dic = {}
        for i in range(len(lst)):
            if i == len(lst) - 1:
                break
            dic[lst[i]] = lst[i + 1]
        return dic

    def dicIntoPath(self, dic):
        dic = dic
        keys = dic.keys()
        lst = list(keys)
        lst.append(0)
        return lst

    def showUtility(self):
        utilList = []
        utildomain = []
        for i in range(len(self.bestList)):
            utilList.append(self.fitness(self.bestList[i][0]))
            utildomain.append(self.bestList[i][1])
        t = range(0, len(utilList))
        x = utildomain
        y = [utilList[i] for i in t]
        plt.plot(x, y)
        plt.show()