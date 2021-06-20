import sys
import Dijkstra
import Graph
import Stack
from Evaluator import Evaluator
import time
import csv

class MultiAgentNetworkCoverage:

    def __init__(self,objGraph):
        self.objGraph = objGraph
        self.component = self.objGraph.findComponent()

    def newmanClustering(self, agent):
        vertexes = self.objGraph.vertexes
        numVertexes = len(self.objGraph.vertexes)
        if agent == 1:
            components = self.objGraph.findComponent()
            self.component = components
        else:
            while True:
                betweenness = self.calculateBetweenness()
                max = -9999
                idx1, idx2 = None, None

                for i in range(numVertexes):
                    for j in range(numVertexes):
                        if betweenness[vertexes[i]][vertexes[j]] > max:
                            max = betweenness[vertexes[i]][vertexes[j]]
                            idx1, idx2 = i, j

                self.objGraph.removeEdge(vertexes[idx1], vertexes[idx2])
                self.objGraph.removeEdge(vertexes[idx2], vertexes[idx1])
                components = self.objGraph.findComponent()
                print("Clustering...")
                if len(components) == agent:
                    break
                if len(components) == len(self.objGraph.vertexes):
                    print("Num of agent is bigger than Num of Vertexes")
                    break
                print("Num of component : ", len(components))
            self.component = self.objGraph.findComponent()

    def calculateBetweenness(self):
        vertexes = self.objGraph.vertexes
        numVertexes = len(self.objGraph.vertexes)
        betweenness = {}

        for i in range(numVertexes):
            betweenness[vertexes[i]] = {}
            for j in range(len(vertexes)):
                betweenness[vertexes[i]][vertexes[j]] = 0.0

        for i in range(numVertexes):
            dist, path, routes = Dijkstra.performAllDestinationDijkstra(self.objGraph, vertexes[i])
            for j in range(numVertexes):
                if i == j:
                    continue
                if routes[vertexes[j]] != None:
                    for k in range(len(routes[vertexes[j]]) - 1):
                        srcEdge = routes[vertexes[j]][k]
                        dstEdge = routes[vertexes[j]][k + 1]
                        betweenness[srcEdge][dstEdge] = betweenness[srcEdge][dstEdge] + 1
                        betweenness[dstEdge][srcEdge] = betweenness[dstEdge][srcEdge] + 1
        return betweenness

    def findRoute(self, component, start):
        visited = {}
        path = []
        for i in range(len(component)):
            visited[component[i]] = False

        stack = Stack.Stack()
        stack.push(component[start])

        while stack.isEmpty() != True:
            current = stack.pop()
            if visited[current] == False:
                visited[current] = True
                path.append(current)
                neighborStation, neighborCost = self.objGraph.getNeighbors(current)
                for i in range(len(neighborStation)):
                    if visited[neighborStation[i]] == False:
                        stack.push(neighborStation[i])

        # print("Path : ",path)
        return path

    def findBestRoute(self, component):
        point = []
        lenNeighbor = []
        lenPath = []

        for i in range(len(component)):
            neighborStation, neighborCost = self.objGraph.getNeighbors(component[i])
            lenNeighbor.append(len(neighborStation))

        point.append(component[0])
        point.append(component[-1])

        for i in range(len(lenNeighbor)):
            if lenNeighbor[i] == 1:
                if not component[i] in point:
                    point.append(component[i])

        # print(point)

        for i in range(len(point)):
            Route = self.findRoute(component, component.index(point[i]))
            path = self.findPath(Route)
            lenPath.append(path)

        min = 9999
        idxMin = None
        for i in range(len(lenPath)):
            if len(lenPath[i]) < min:
                idxMin = i

        # print(lenPath[idxMin])
        return lenPath[idxMin]

    def findPath(self, visitedList):
        path = []
        path.append(visitedList[0])
        for i in range(1, len(visitedList)):
            neighborStation = self.objGraph.getNeighbors(path[-1])
            if visitedList[i] in neighborStation:
                path.append(visitedList[i])
            else:
                dist, p, course, list = Dijkstra.performDijkstra(self.objGraph, path[-1], visitedList[i])
                temp = list[1:]
                path = path + temp

        # print("Route : ", path)
        return path

    def generateCoverage(self, intNumAgents):
        lstPlan = []
        self.newmanClustering(intNumAgents)
        print("Finished clusturing")
        for i in range(intNumAgents):
            print("Compnent : ", i, " ", self.component[i])
            a = self.findBestRoute(self.component[i])
            print("Route : ", a)
            print("---------------------------------------------")
            lstPlan.append(a)
        print("Plan List : ", lstPlan)
        return lstPlan

if __name__ == "__main__":
    # g = Graph.DenseGraph('Subway-Seoul-ver-2.csv')
    # g_eval = Graph.DenseGraph('Subway-Seoul-ver-2.csv')
    g = Graph.DenseGraph('Subway-Seoul.csv')
    g_eval = Graph.DenseGraph('Subway-Seoul.csv')
    ###################### DO NOT TOUCH THE BELOW CODE - IL-CHUL MOON #############
    objCoverage = MultiAgentNetworkCoverage(g)
    print("Input Number of Agents : ")
    strInput = input()
    objStartTime = time.time()
    lstPlan = objCoverage.generateCoverage(int(strInput.strip()))
    objEndTime = time.time()
    objElapseTime = objEndTime - objStartTime
    print("Elapse Time : " + str(objElapseTime))
    objEvaluator = Evaluator(g_eval)
    dblScore = objEvaluator.evaluate(lstPlan, int(strInput.strip()))
    print("Evaluation Score:")
    print(dblScore)