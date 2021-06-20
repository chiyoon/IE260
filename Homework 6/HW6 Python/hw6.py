import sys
import Dijkstra
import Tree2
import Graph
import NetworkClustering
import csv
import time
import random

class SupplyHub:

    def __init__(self, graph):
        self.graph = graph
        self.component = self.graph.findComponent()

    def newmanClustering(self, k):
        clustering = NetworkClustering.NewmanClustering()
        clustering.performNewmanClustering(self.graph, k)
        self.component = self.graph.findComponent()

    def findMst(self, component, ind):
        visited = []
        edge = []
        visited.append(component[ind])

        while True:
            mincost = 9999
            minsrc = None
            mindst = None
            for i in range(len(visited)):
                neighborStation, neighborCost = self.graph.getNeighbors(visited[i])
                for j in range(len(neighborStation)):
                    if neighborCost[j] < mincost:
                        if neighborStation[j] in visited:
                            pass
                        else:
                            mincost = neighborCost[j]
                            minsrc = visited[i]
                            mindst = neighborStation[j]
            visited.append(mindst)
            edge.append([minsrc, mindst])
            if len(visited) == len(component):
                break

        return visited, edge

    def treeBalancing(self, component, tree):
        current = tree
        while True:
            currentRoot = current.root
            currentDepth = current.printHeight()
            while True:
                lenChild = currentRoot.getLengthChild()
                child = currentRoot.getChild()
                maxSub = -9999
                maxChild = None
                for i in range(lenChild):
                    subDepth = child.getHeight(0)
                    if subDepth > maxSub:
                        maxSub = subDepth
                        maxChild = child
                    child = child.getNext()
                ind = component.index(maxChild.getData())
                visited, edge = self.findMst(component, ind)
                newTree = Tree2.Tree(self.graph)
                for j in range(len(edge)):
                    newTree.add(edge[j])
                newDepth = newTree.root.getHeight(0)
                if newDepth >= currentDepth:
                    return current
                else:
                    break
            current = newTree

    def printResult(self):
        for i in range(len(self.component)):
            print("---------------------------------------------------------------")
            print(str(i+1) + ". Component of ", self.component[i])
            visited, edge = self.findMst(self.component[i], 0)
            tree = Tree2.Tree(self.graph)
            for j in range(len(edge)):
                tree.add(edge[j])
            balanced = self.treeBalancing(self.component[i], tree)
            print("Local Supply Tree")
            balanced.printTree()
            print("Max. Depth =",float(balanced.printHeight()))

if __name__ == "__main__":
    g = Graph.DenseGraph('Subway-Seoul-ver-2.csv')
    # g = Graph.DenseGraph('Subway-Seoul.csv')
    inittime = time.time()
    supply = SupplyHub(g)
    supply.newmanClustering(10)
    fintime = time.time()
    supply.printResult()
    # print("Elapsed time : "+str(fintime - inittime))