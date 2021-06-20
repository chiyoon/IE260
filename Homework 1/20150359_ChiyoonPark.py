import math

# class1 : Exponential Function
class ExpFunc:

    def __init__(self, a, b):
        self.coeff = float(a)
        self.cons = float(b)

    def printFunction(self):
        Func = "f(x) = " + str(self.coeff) + " * exp(x) + "+ str(self.cons)
        print(Func)

    def eval(self, x):
        eval = self.coeff * math.exp(float(x)) + self.cons
        return eval

    def deriv(self, x):
        deriv_coeff = self.coeff
        deriv_cons = float(0)
        deriv_eval = deriv_coeff * math.exp(float(x)) + deriv_cons
        return deriv_eval

    def binarySearch(self, a, b, tol):
        self.solBin = None
        self.iterBin = None
        iter = 0
        low = float(a)
        high = float(b)
        mid = (low + high) / 2
        while math.fabs(self.eval(mid)) > tol:
            if self.eval(low) * self.eval(mid) > 0:
                low = mid
            else:
                high = mid
            mid = (low + high) / 2
            iter = iter + 1
        self.solBin = mid
        self.iterBin = iter
        return(self.solBin, self.iterBin)

    def newtonSearch(self, x0, tol):
        x = x0
        iter = 0
        self.solNew = None
        self.iterNew = None
        while math.fabs(self.eval(x)) > tol:
            x = x - (self.eval(x) / self.deriv(x))
            iter = iter + 1
        self.solNew = x
        self.iterNew = iter
        return(self.solNew, self.iterNew)

    def secantSearch(self, a, b, tol):
        self.solSec = None
        self.iterSec = None
        x1 = float(a)
        x2 = float(b)
        iter = 0
        while math.fabs(self.eval(x2)) > tol:
            x = x2 - self.eval(x2) * ((x2 - x1) / (self.eval(x2) - self.eval(x1)))
            x1 = x2
            x2 = x
            iter = iter + 1
        self.solSec = x2
        self.iterSec = iter
        return(self.solSec, self.iterSec)

    def printResult(self, para):

        if para == "Binarysearch":
            print("Binary Search")
            print("Solution : f( " + str(self.solBin) + " ) = " + str(self.eval(self.solBin)) + " after " + str(self.iterBin) + " iterations")
        elif para == "Newtonsearch":
            print("Newton Search")
            print("Solution : f( " + str(self.solNew) + " ) = " + str(self.eval(self.solNew)) + " after " + str(self.iterNew) + " iterations\n")
        elif para == "Secantsearch":
            print("Secant Search")
            print("Solution : f( " + str(self.solSec) + " ) = " + str(self.eval(self.solSec)) + " after " + str(self.iterSec) + " iterations")

# class2 : Cubic Function
class CubicFunc:

    def __init__(self, a, b, c, d):
        self.coeff1 = a
        self.coeff2 = b
        self.coeff3 = c
        self.cons = d

    def printFunction(self):
        Func = "f(x) = " + str(self.coeff1)+" *x^3 + "+str(self.coeff2)+" *x^2 + "+str(self.coeff3)+" *x + "+str(self.cons)
        print(Func)

    def eval(self, x):
        eval = self.coeff1 * math.pow(x, 3) + self.coeff2 * math.pow(x, 2) + self.coeff3 * x + self.cons
        return eval

    def deriv(self, x):
        deriv_cons = self.coeff3
        deriv_coeff3 = self.coeff2 * 2
        deriv_coeff2 = self.coeff1 * 3
        deriv_coeff1 = 0
        deriv_eval = deriv_coeff1 * math.pow(x, 3) + deriv_coeff2 * math.pow(x, 2) + deriv_coeff3 * x + deriv_cons
        return deriv_eval

    def binarySearch(self, a, b, tol):
        self.solBin = None
        self.iterBin = None
        iter = 0
        low = float(a)
        high = float(b)
        mid = (low + high) / 2
        while math.fabs(self.eval(mid)) > tol:
            if self.eval(low) * self.eval(mid) > 0:
                low = mid
            else:
                high = mid
            mid = (low + high) / 2
            iter = iter + 1
        self.solBin = mid
        self.iterBin = iter
        return(self.solBin, self.iterBin)

    def newtonSearch(self, x0, tol):
        x = x0
        iter = 0
        self.solNew = None
        self.iterNew = None
        while math.fabs(self.eval(x)) > tol:
            x = x - (self.eval(x) / self.deriv(x))
            iter = iter + 1
        self.solNew = x
        self.iterNew = iter
        return(self.solNew, self.iterNew)

    def secantSearch(self, a, b, tol):
        self.solSec = None
        self.iterSec = None
        x1 = float(a)
        x2 = float(b)
        iter = 0
        while math.fabs(self.eval(x2)) > tol:
            x = x2 - self.eval(x2) * ((x2 - x1) / (self.eval(x2) - self.eval(x1)))
            x1 = x2
            x2 = x
            iter = iter + 1
        self.solSec = x2
        self.iterSec = iter
        return(self.solSec, self.iterSec)

    def printResult(self, para):

        if para == "Binarysearch":
            print("Binary Search")
            print("Solution : f( " + str(self.solBin) + " ) = " + str(self.eval(self.solBin)) + " after " + str(self.iterBin) + " iterations")
        elif para == "Newtonsearch":
            print("Newton Search")
            print("Solution : f( " + str(self.solNew) + " ) = " + str(self.eval(self.solNew)) + " after " + str(self.iterNew) + " iterations\n")
        elif para == "Secantsearch":
            print("Secant Search")
            print("Solution : f( " + str(self.solSec) + " ) = " + str(self.eval(self.solSec)) + " after " + str(self.iterSec) + " iterations")

# class3 : Logarithmic Function
class LogFunc:

    def __init__(self, a, b):
        self.coeff = float(a)
        self.cons = float(b)

    def printFunction(self):
        Func = "f(x) = " + str(self.coeff) + " * log(x) + "+ str(self.cons)
        print(Func)

    def eval(self, x):
        eval = self.coeff * math.log(x, math.exp(1)) + self.cons
        return eval

    def deriv(self, x):
        deriv_coeff = self.coeff
        deriv_cons = 0
        deriv_eval = deriv_coeff / x + deriv_cons
        return deriv_eval

    def binarySearch(self, a, b, tol):
        self.solBin = None
        self.iterBin = None
        iter = 0
        low = float(a)
        high = float(b)
        mid = (low + high) / 2
        while math.fabs(self.eval(mid)) > tol:
            if self.eval(low) * self.eval(mid) > 0:
                low = mid
            else:
                high = mid
            mid = (low + high) / 2
            iter = iter + 1
        self.solBin = mid
        self.iterBin = iter
        return(self.solBin, self.iterBin)

    def secantSearch(self, a, b, tol):
        self.solSec = None
        self.iterSec = None
        x1 = float(a)
        x2 = float(b)
        iter = 0
        while math.fabs(self.eval(x2)) > tol:
            x = x2 - self.eval(x2) * ( (x2 - x1) / (self.eval(x2) - self.eval(x1)))
            x1 = x2
            x2 = x
            iter = iter + 1
        self.solSec = x2
        self.iterSec = iter
        return(self.solSec, self.iterSec)

    def printResult(self, para):

        if para == "Binarysearch":
            print("Binary Search")
            print("Solution : f( " + str(self.solBin) + " ) = " + str(self.eval(self.solBin)) + " after " + str(self.iterBin) + " iterations")
        elif para == "Secantsearch":
            print("Secant Search")
            print("Solution : f( " + str(self.solSec) + " ) = " + str(self.eval(self.solSec)) + " after " + str(self.iterSec) + " iterations\n")

# class4 : Main class
class main():

    funcExp = ExpFunc(3, -5)
    funcCubic = CubicFunc(2, -3, 4, -5)
    funcLog = LogFunc(3, 10)

    def main(self):
        self.funcExp.printFunction()
        self.funcExp.binarySearch(0, 1, 0)
        self.funcExp.printResult("Binarysearch")
        self.funcExp.secantSearch(0, 1, 0)
        self.funcExp.printResult("Secantsearch")
        self.funcExp.newtonSearch(1, 0)
        self.funcExp.printResult("Newtonsearch")

        self.funcCubic.printFunction()
        self.funcCubic.binarySearch(1, 2, 0.0001)
        self.funcCubic.printResult("Binarysearch")
        self.funcCubic.secantSearch(1, 2, 0.0001)
        self.funcCubic.printResult("Secantsearch")
        self.funcCubic.newtonSearch(2, 0.0001)
        self.funcCubic.printResult("Newtonsearch")

        self.funcLog.printFunction()
        self.funcLog.binarySearch(0.0001, 0.05, 0.001)
        self.funcLog.printResult("Binarysearch")
        self.funcLog.secantSearch(0.0001, 0.05, 0.001)
        self.funcLog.printResult("Secantsearch")

# Execution part
execution = main()
execution.main()
