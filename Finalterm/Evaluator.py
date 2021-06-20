
###################### DO NOT TOUCH THE BELOW CODE - IL-CHUL MOON #############
class Evaluator:
    def __init__(self,objGraph):
        self.objGraph = objGraph

    def evaluate(self,lstPlan,intRequestedAgent):
        dicVisit = {}

        if len(lstPlan) != intRequestedAgent:
            print("Plan Num Error : Requested : " + str(intRequestedAgent)+", Planned : "+str(len(lstPlan)))
            return -9999999

        for i in range(len(self.objGraph.vertexes)):
            dicVisit[self.objGraph.vertexes[i]] = False

        for i in range(len(lstPlan)):
            for j in range(len(lstPlan[i])):
                strVisit = lstPlan[i][j]
                dicVisit[strVisit] = True

        lstKey = list(dicVisit.keys())
        for i in range(len(dicVisit.keys())):
            strKey = lstKey[i]
            if dicVisit[strKey] == False:
                print("No visit : "+strKey)
                return -9999999

        intCnt = 0
        for i in range(len(lstPlan)):
            for j in range(len(lstPlan[i])):
                intCnt = intCnt + 1
                if lstPlan[i][j] not in self.objGraph.edges.keys():
                    print("Invalid Node : " + str(lstPlan[i][j]))
                    return -9999999
                if j < len(lstPlan[i])-1:
                    if lstPlan[i][j+1] not in self.objGraph.edges[lstPlan[i][j]].keys():
                        print("Invalid Edge : " + str(lstPlan[i][j]) + "," + str(lstPlan[i][j+1]))
                        return -9999999

        return 1000-intCnt
