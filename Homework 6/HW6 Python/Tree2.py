import Stack
import Graph
import csv

class Tree:
    root = None

    def __init__(self, graph):
        self.objgraph = graph

    def add(self, edge):
        if self.root == None:
            src = Node(edge[0])
            dst = Node(edge[1])
            src.setChild(dst)
            dst.setParent(src, self.objgraph.getWeight(edge[0], edge[1]))
            self.root = src
        else:
            src = self.find(edge[0])
            dst = Node(edge[1])
            src.setChild(dst)
            dst.setParent(src, self.objgraph.getWeight(edge[0], edge[1]))

    def find(self, data):
        visited = []
        path = []
        stack = Stack.Stack()
        stack.push(self.root)
        object = None

        while stack.isEmpty() != True:
            current = stack.pop()
            if current.getData() == data:
                object = current
                return object

            if current.getData() not in visited:
                visited.append(current.getData())
                path.append(current.getData())
                child = current.getChild()
                len = current.getLengthChild()
                for i in range(len):
                    if child.getData() not in visited:
                        stack.push(child)
                        path.append(child.getData())
                    child = child.getNext()

        if object == None:
            return False

    def printTree(self):
        print(self.root.getString(0), end = '')

    def printHeight(self):
        # print(self.root.getHeight(0))
        return self.root.getHeight(0)

class Node:
    data = None
    parent = None
    distanceWithParent = 0
    child = None
    lengthChild = 0
    next = None

    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, node):
        self.next = node

    def getNext(self):
        return self.next

    def setParent(self, parent, weigh):
        self.parent = parent
        self.distanceWithParent = weigh

    def getParent(self):
        return self.parent

    def printParent(self):
        if self.parent != None:
            print(self.parent.getData())
        else:
            # print("This node hasn't parent")
            pass

    def setChild(self, node):
        if self.child == None:
            self.child = node
            self.lengthChild += 1
        else:
            current = self.child
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(node)
            self.lengthChild += 1

    def getChild(self):
        return self.child

    def printChild(self):
        printList = []
        current = self.child
        while True:
            if current == None:
                break
            else:
                printList.append(current.getData())
                current = current.getNext()
        print(printList)

    def getDistance(self):
        return self.distanceWithParent

    def getLengthChild(self):
        return self.lengthChild

    def getString(self, depth):
        ret = ""
        for itr in range(depth):
            ret = ret + "...."
        ret = ret + str(self.getData()) + "\n"
        child = self.getChild()
        len = self.getLengthChild()
        for i in range(len):
            ret = ret + child.getString(depth + 1)
            child = child.getNext()
        return ret

    def getHeight(self, height):
        hList = []
        len = self.getLengthChild()
        child = self.getChild()
        if child == None:
            return height + self.getDistance()
        else:
            height = height + self.getDistance()
            for i in range(len):
                subHeight = child.getHeight(height)
                hList.append(subHeight)
                child = child.getNext()
            return max(hList)


if __name__ == "__main__":
    g = Graph.DenseGraph('Subway-Seoul.csv')
    tree = Tree(g)
    edgeList = [['소요산', '동두천'], ['동두천', '보산'], ['보산', '동두천중앙'], ['동두천중앙', '지행'], ['지행', '덕정'], ['덕정', '덕계'], ['덕계', '양주'], ['양주', '녹양'], ['녹양', '가능'], ['가능', '의정부'], ['의정부', '회룡'], ['회룡', '망월사'], ['망월사', '도봉산'], ['도봉산', '도봉'], ['도봉', '방학']]
    for i in range(len(edgeList)):
        tree.add(edgeList[i])
    tree.printTree()
    print(tree.printHeight())


