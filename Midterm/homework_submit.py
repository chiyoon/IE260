import numpy
import math
from datetime import datetime

class MakeFormulaIntoTree:

    def __init__(self, formula):
        self.formula = formula
        self.stackoperator = Stack()
        self.stackoperand = Stack()
        self.tree = None

    def makeTree(self):
        lastappendnode = None
        for i in range(len(self.formula)):
            node = Node(self.formula[i])

            if node.getValue() == "-":
                if lastappendnode == None:
                    node.type = "unaryoper"
                    node.priority = 4

                else:
                    if lastappendnode.getValue() == ")":
                        pass
                    elif lastappendnode.getType() != "digit" and  lastappendnode.getType() != "variable":
                        node.type = "unaryoper"
                        node.priority = 4

            if node.getType() == "digit" or node.getType() == "variable":
                self.stackoperand.push(node)

            else:
                if node.getType() == "unaryoper" or node.getType() == "parentheses":
                    self.stackoperator.push(node)

                elif node.getValue() == ")":
                    while self.stackoperator.getTop().getValue() != "(":
                        self.mergeOperand()
                    self.stackoperator.pop()

                else:
                    while (self.stackoperator.getLength() != 0) and (self.stackoperator.getTop().getPriority() >= node.getPriority()):
                        self.mergeOperand()
                    self.stackoperator.push(node)

            lastappendnode = node

        while self.stackoperator.getLength() != 0:
            self.mergeOperand()

        self.tree = self.stackoperand.pop()

    def mergeOperand(self):
        node = self.stackoperator.pop()
        if node.getType() == "unaryoper":
            unaryoperand = self.stackoperand.pop()
            node.setUnary(unaryoperand)
            self.stackoperand.push(node)

        elif node.getType() == "binaryoper":
            binaryoperand1 = self.stackoperand.pop()
            binaryoperand2 = self.stackoperand.pop()
            node.setLeft(binaryoperand2)
            node.setRight(binaryoperand1)
            self.stackoperand.push(node)

    def eval(self, node, x):

        vari = x

        if node.getType() == "variable":
            return float(vari)

        elif node.getType() == "unaryoper":

            if node.getValue() == "-":
                return - float(self.eval(node.getUnary(), vari))

            elif node.getValue() == "ln":
                if float(self.eval(node.getUnary(), vari)) <= 0:
                    return numpy.log(float(0.0000000000000000000001))

                else:
                    return numpy.log(float(self.eval(node.getUnary(), vari)))

            elif node.getValue() == "cos":
                return numpy.cos(float(self.eval(node.getUnary(), vari)))

            elif node.getValue() == "sin":
                return numpy.sin(float(self.eval(node.getUnary(), vari)))

            elif node.getValue() == "tan":
                return numpy.tan(float(self.eval(node.getUnary(), vari)))

            elif node.getValue() == "exp":
                return numpy.exp(float(self.eval(node.getUnary(), vari)))

        elif node.getType() == "binaryoper":

            if node.getValue() == '+':
                return float(self.eval(node.getLeft(), vari)) + float(self.eval(node.getRight(), vari))

            elif node.getValue() == '-':
                return float(self.eval(node.getLeft(), vari)) - float(self.eval(node.getRight(), vari))

            elif node.getValue() == '*':
                return float(self.eval(node.getLeft(), vari)) * float(self.eval(node.getRight(), vari))

            elif node.getValue() == '/':
                return float(self.eval(node.getLeft(), vari)) / float(self.eval(node.getRight(), vari))

            elif node.getValue() == '^':
                return float(self.eval(node.getLeft(), vari)) ** float(self.eval(node.getRight(), vari))

        elif node.getType() == "digit":
            return float(node.getValue())

    def getTree(self):
        return self.tree

class Stack:

    def __init__(self):
        self.head = Node("head")
        self.length = 0

    def getTop(self):
        if self.length != 0:
            return self.head.getNext()

        else:
            return None

    def push(self, node):
        node.setNext(self.getTop())
        self.head.setNext(node)
        self.length = self.length + 1

    def pop(self):
        if self.length == 0:
            raise IndexError("empty stack")

        else:
            temp = self.getTop()
            self.head.setNext(temp.getNext())
            self.length = self.length - 1
            return temp

    def getLength(self):
        return self.length

    def returnStack(self):
        if self.length == 0:
            return []

        else:
            tempNode = self.getTop()
            tempList = []
            for i in range(self.length):
                tempList.append(tempNode.getValue())
                if not i == self.length - 1:
                    tempNode = tempNode.getNext()
            tempList.reverse()
            return tempList

class Node:

    unaryoper = ["ln","sin","cos","tan","exp"]
    binary1 = "+-"
    binary2 = "*/"
    binary3 = "^"
    parentheses = "("
    head = "head"
    variable = "xX"

    def __init__(self, value):
        self.value  = value
        self.left = None
        self.right = None
        self.unary = None
        self.next = None
        self.type = None
        self.priority = None

        try:
            float(value)
            self.type = "digit"
            self.priority = -1

        except ValueError:

            if value in self.unaryoper:
                self.type = "unaryoper"
                self.priority = 4

            elif value in self.binary1:
                self.type = "binaryoper"
                self.priority = 1

            elif value in self.binary2:
                self.type = "binaryoper"
                self.priority = 2

            elif value in self.binary3:
                self.type = "binaryoper"
                self.priority = 3

            elif value in self.parentheses:
                self.type = "parentheses"
                self.priority = 0

            elif value in self.variable:
                self.type = "variable"
                self.priority = -1

            elif value in self.head:
                self.type = "stackhead"
                self.priority = -100

    def getValue(self):
        return self.value

    def getType(self):
        return self.type

    def getPriority(self):
        return self.priority

    def setNext(self, node):
        self.next = node

    def setRight(self, node):
        self.right = node

    def setLeft(self, node):
        self.left = node

    def setUnary(self, node):
        self.unary = node

    def getNext(self):
        return self.next

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getUnary(self):
        return self.unary

    def isNext(self):
        if self.next != None:
            return True

        else:
            return False

    def isRight(self):
        if self.right != None:
            return True

        else:
            return False

    def isLeft(self):
        if self.left != None:
            return True

        else:
            return False

    def isUnary(self):
        if self.unary != None:
            return True

        else:
            return False

def findSoluton1(treeLeft, treeRight, min, max):
    treeLeft = treeLeft
    treeRight = treeRight
    minRan = min
    maxRan = max
    domainList = []
    temp = minRan
    solutionList = []
    currentime = datetime.now()

    while temp <= maxRan:

        tempTuple = (temp, temp + 0.0001)

        if temp + 0.0001 > maxRan:
            tempTuple = (temp, maxRan)

        leftmin = treeLeft.eval(treeLeft.getTree(), tempTuple[0])
        leftmax = treeLeft.eval(treeLeft.getTree(), tempTuple[1])
        rightmin = treeRight.eval(treeRight.getTree(), tempTuple[0])
        rigthmax = treeRight.eval(treeRight.getTree(), tempTuple[1])

        bool = check(leftmin, rightmin, leftmax, rigthmax)

        if bool == True:
            domainList.append(tempTuple)
            mid = (tempTuple[0] + tempTuple[1]) / 2
            solutionList.append(mid)

        temp = temp + 0.0001
    endtime = datetime.now()

    return solutionList, (endtime - currentime)

def findSolution2(treeLeft, treeRight, min, max, iter = 0):

    iter = iter
    treeLeft = treeLeft
    treeRight = treeRight
    minRan = min
    maxRan = max
    mid = ( minRan + maxRan ) / 2
    solutionList = []
    init = datetime.now()

    if iter < 15:
        temp1, time1 = findSolution2(treeLeft, treeRight, minRan, mid, iter + 1)
        temp2, time2 = findSolution2(treeLeft, treeRight, mid, maxRan, iter + 1)
        solutionList = solutionList + temp1 + temp2

    if iter == 15:

        leftmin = treeLeft.eval(treeLeft.getTree(), minRan)
        leftmax = treeLeft.eval(treeLeft.getTree(), maxRan)
        rightmin = treeRight.eval(treeRight.getTree(), minRan)
        rightmax = treeRight.eval(treeRight.getTree(), maxRan)

        if check(leftmin, rightmin, leftmax, rightmax) == True:

            solution = binarySearch(treeLeft, treeRight, minRan, maxRan)
            solutionList.append(solution)

    finish = datetime.now()
    time = finish - init

    return solutionList, time

def binarySearch(treeLeft, treeRight, min, max):
    treeLeft = treeLeft
    treeRight = treeRight
    minRan = min
    maxRan = max
    mid = (minRan + maxRan) / 2

    leftmin = treeLeft.eval(treeLeft.getTree(), minRan)
    rightmin = treeRight.eval(treeRight.getTree(), minRan)

    while not math.fabs(treeLeft.eval(treeLeft.getTree(), mid) - treeRight.eval(treeRight.getTree(), mid)) < 0.00001:

        if check(leftmin, rightmin, treeLeft.eval(treeLeft.getTree(), mid), treeRight.eval(treeRight.getTree(), mid)) == False:
            minRan = mid
            mid = (minRan + maxRan) / 2

        else:
            maxRan = mid
            mid = (minRan + maxRan) / 2

    return mid

def check(leftmin, rightmin, leftmax, rightmax):
    if leftmin > rightmin:

        if leftmax <= rightmax:
            return True

        else:
            return False
    elif leftmin < rightmin:

        if leftmax >= rightmax:
            return True

        else:
            return False

    else:
        return True

def overlap(solution):
    sortsolution = []

    for i in range(len(solution)):
        if i == len(solution) - 1:
            sortsolution.append(solution[i])
        else:
            if solution[i + 1] - solution[i] >= 0.01:
                sortsolution.append(solution[i])
            else:
                pass

    return sortsolution

def main():

    while True:
        print("Write Exit to terminate the program.")
        line = input("Enter Equation : ")

        if line == "Exit":
            break

        if not "=" in line:
            print("Please input equation in correct order\n")
            continue

        else:
            token = line.split(" ")
            index = 0

            err = False
            for i in range(len(token)):
                try:
                    float(token[i])

                except ValueError:
                    if not token[i] in ["ln","sin","cos","tan","exp","=","+","-","*","/","^","(",")","x","X"]:
                        err = True

            if err == True:
                print("Please input equation in correct order\n")
                continue

            while (line[index] != "="):
                index = index + 1
            leftSide = line[:index - 1]
            rightSide = line[index + 2:]

            index2 = token.index("=")
            tokenLeftSide = token[:index2]
            tokenRightSide = token[index2 + 1:]

            if tokenLeftSide == [''] or tokenLeftSide == [] or tokenRightSide == [''] or tokenRightSide == []:
                print("Please input equation in correct order\n")
                continue

            minRan = input("Enter Min Range : ")
            try:
                float(minRan)
                minRan = float(minRan)

            except ValueError:
                print("Please input range\n")
                continue

            maxRan = input("Enter Max Range : ")
            try:
                float(maxRan)
                maxRan = float(maxRan)

            except ValueError:
                print("Please input range\n")
                continue

            print("Left Side : " + leftSide)
            print("Right Side : " + rightSide)

            treeLeft = MakeFormulaIntoTree(tokenLeftSide)
            treeLeft.makeTree()
            treeRight = MakeFormulaIntoTree(tokenRightSide)
            treeRight.makeTree()

            solution, time = findSolution2(treeLeft, treeRight, minRan, maxRan)

            if solution == []:
                print("No Solution")

            else:
                sortsolution = overlap(solution)
                for i in range(len(sortsolution)):
                    print("Solution : "+str(sortsolution[i]))
                    print("Left Side Evaluation : "+str(treeLeft.eval(treeLeft.getTree(), sortsolution[i])))
                    print("Right Side Evaluation : "+str(treeRight.eval(treeRight.getTree(), sortsolution[i])))
            print("Elapsed sec : " + str(time.total_seconds()) + "\n")

if __name__ == "__main__":
    main()