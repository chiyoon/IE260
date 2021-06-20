class PlanNode:
    def __init__(self, numNo, strSerialNumber, strModel, numModelNumber, dateStart, numAssemblyOrder, dateEnd,
                 strOrderOrigin, nextNode = None, prevNode = None):
        self.numNo = numNo
        self.strSerialNumber = strSerialNumber
        self.strModel = strModel
        self.numModelNumber = numModelNumber
        self.dateStart = dateStart
        self.numAssemblyOrder = numAssemblyOrder
        self.dateEnd = dateEnd
        self.strOrderOrigin = strOrderOrigin
        self.nextNode = nextNode
        self.prevNode = prevNode

    def printOut(self):
        print('No :', self.numNo, ', SerialNum : ', self.strSerialNumber, ',Model:', self.strModel, ',Start Date:',
              self.dateStart)

    def getNextNode(self):
        # Problem 1. complete this method
        nextNum = self.nextNode
        return nextNum

    def getPrevNode(self):
        # Problem 1. complete this method
        prevNum = self.prevNode
        return prevNum

    def setNextNode(self, node):
        # Problem 1. complete this method
        self.nextNode = node

    def setPrevNode(self, node):
        # Problem 1. complete this method
        self.prevNode = node