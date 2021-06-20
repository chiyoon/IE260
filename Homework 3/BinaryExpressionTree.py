import sys
import numpy as np

class BinaryExpressionTree:

    priorities = {"+":1, "-":1, "*":2, "/":2, "^":3, "(":0}
    unaryPriority = 4

    def __init__(self,line):
        tokens = line.split(" ")
        self.stackOperator = Stack()
        self.stackOperand = Stack()
        self.root = self.buildTree(tokens)
        print("Tokens : "+str(tokens))
        print("Prefix : " + self.traversPreFix())
        print("Postfix : " + self.traversPostFix())

    def buildTree(self,tokens):
        for itr in range(len(tokens)):
            token = tokens[itr]
            if self.isDigit(token) == True:
                tokenNode = Node(token, -1, True, False)
                self.stackOperand.push(tokenNode)
            elif token == "-" and ( self.stackOperator.getLength() == 0 or self.stackOperator.top().getValue() == '('):
                tokenOperator = Node(token, self.unaryPriority, False, False)
                self.stackOperator.push(tokenOperator)
            elif token == "ln":
                tokenOperator = Node(token, self.unaryPriority, False, False)
                self.stackOperator.push(tokenOperator)
            elif token == ')':
                while self.stackOperator.top().getValue() != '(':
                    self.mergeLastTwoOperand()
                self.stackOperator.pop()
            else:
                tokenNode = Node(token, self.priorities[token], False, False)
                if tokenNode.getValue() == '(':
                    self.stackOperator.push(tokenNode)
                else:
                    while (self.stackOperator.getLength() != 0) and (self.stackOperator.top().getPriority() >= tokenNode.getPriority()):
                        self.mergeLastTwoOperand()
                    self.stackOperator.push(tokenNode)
            print("Step. " + str(itr + 1))
            print("Stack Operator : " + str(self.stackOperator))
            print("Stack Operand : " + str(self.stackOperand))
        while self.stackOperator.top() != None:
            self.mergeLastTwoOperand()
        return self.stackOperand.top()

    def evaluate(self, node=None):
        if node == None:
            node = self.root
        if node.getLeft() != None:
            valueLeft = self.evaluate(node.getLeft())
        if node.getRight() != None:
            valueRight = self.evaluate(node.getRight())
        if node.getLeft() != None and node.getRight() == None:
            operator = node.getValue()
            if operator == '-':
                return -1 * float(valueLeft)
            elif operator == 'ln':
                return np.log(float(valueLeft))
        elif node.getLeft() != None and node.getRight() != None:
            operator = node.getValue()
            if operator == '+':
                return float(valueLeft) + float(valueRight)
            elif operator == '-':
                return float(valueLeft) - float(valueRight)
            elif operator == '*':
                return float(valueLeft) * float(valueRight)
            elif operator == '/':
                return float(valueLeft) / float(valueRight)
            elif operator == '^':
                return float(valueLeft) ** float(valueRight)
        else:
            return float(node.getValue())

    def __str__(self):
        return self.root.getString(0)

    def traversPreFix(self, node=None):
        if node == None:
            node = self.root
        ret = ""
        if node.getLeft() == None and node.getRight() == None:
            ret = ret + node.getValue()
        elif node.getLeft() != None and node.getRight() == None:
            ret = ret + node.getValue() + self.traversPreFix(node.left)
        elif node.getLeft() == None and node.getRight() != None:
            ret = ret + node.getValue() + self.traversPreFix(node.right)
        elif node.getLeft() != None and node.getRight() != None:
            ret = ret + node.getValue() + self.traversPreFix(node.left) + self.traversPreFix(node.right)
        return ret

    def traversPostFix(self, node=None):
        if node == None:
            node = self.root
        ret = ""
        if node.getLeft() == None and node.getRight() == None:
            ret = ret + node.getValue()
        elif node.getLeft() != None and node.getRight() == None:
            ret = ret + self.traversPostFix(node.left) + node.getValue()
        elif node.getLeft() == None and node.getRight() != None:
            ret = ret + self.traversPostFix(node.right) + node.getValue()
        elif node.getLeft() != None and node.getRight() != None:
            ret = ret + self.traversPostFix(node.left) + self.traversPostFix(node.right) + node.getValue()
        return ret

    def mergeLastTwoOperand(self):
        nodeOperator = self.stackOperator.pop()
        if nodeOperator.getPriority() == self.unaryPriority:
            operand = self.stackOperand.pop()
            nodeOperator.setLeft(operand)
            self.stackOperand.push(nodeOperator)
        else:
            operand2 = self.stackOperand.pop()
            operand1 = self.stackOperand.pop()
            nodeOperator.setLeft(operand1)
            nodeOperator.setRight(operand2)
            self.stackOperand.push(nodeOperator)

    def isDigit(self,token):
        try:
            float(token)
            return True
        except ValueError:
            return False

class Stack:
    def __init__(self):
        self.head = Node(None,-1,False,blnTop=True)
        self.length = 0
    def top(self):
        if self.head.getNext() != None:
            return self.head.getNext()
        return None
    def push(self,node):
        node.setNext(self.head.getNext())
        self.head.setNext(node)
        self.length = self.length + 1
    def pop(self):
        ret = self.head.getNext()
        if ret != None:
            self.head.setNext(ret.getNext())
            self.length = self.length - 1
        return ret
    def __str__(self):
        currentNode = self.head.getNext()
        ret = ""
        while currentNode != None:
            ret = str(currentNode.getValue()) + "," + ret
            currentNode = currentNode.getNext()
        return ret
    def getLength(self):
        return int(self.length)

class Node:
    def __init__(self,value,priority,blnDigit,blnTop=False):
        self.value = value
        self.priority = priority
        self.blnTop = blnTop
        self.next = None
        self.left = None
        self.right = None
        self.blnDigit = blnDigit
    def isDigit(self):
        return self.blnDigit
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def setRight(self,node):
        self.right = node
    def setLeft(self,node):
        self.left = node
    def setNext(self,node):
        self.next = node
    def getNext(self):
        return self.next
    def getValue(self):
        return self.value
    def getPriority(self):
        return self.priority
    def isTop(self):
        return self.blnTop
    def getString(self,depth):
        ret = ""
        for itr in range(depth):
            ret = ret + "...."
        ret = ret + str( self.getValue() ) + "\n"
        if self.getLeft() != None:
            ret = ret + self.getLeft().getString(depth+1)
        if self.getRight() != None:
            ret = ret + self.getRight().getString(depth + 1)
        return ret

if __name__ == "__main__":
    line = input("Enter formula : ")
    # line = '3 + 5 - 2 * 7'
    # line = '3 + ( 5 - 2 ) * 7'
    # line = '- 3 + ( - ln 5 - 2 ) * 7'
    tree = BinaryExpressionTree(line)
    print ("Evauate : "+str(tree.evaluate()))
    print ("Tree : \n"+str(tree))