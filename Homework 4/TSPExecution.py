from TravelingSalesmanProblem import *

#data_mode = 'Random'
data_mode = 'Load'
csvfile = "TSP1.csv"
height = 500
width = 700
cities = 15
mutationFactor = 0.1
time = 180

tsp = TravelingSalesmanProblem(data_mode,csvfile,cities,height, width, time)
routes, utility, distance, elapsedTime = tsp.performEvolution(100, 15, 25, mutationFactor, 6)

currentCity = 0
route = ''
for itr in range(len(routes.keys())):
    route = route + '->' + str(currentCity)
    currentCity = routes[currentCity]
print ("===== 20150359, Student =====")
print ("Routes : %s" %(route))
print ("Distance : ", distance)
print ("Elapsed time : ", elapsedTime, "secs")
# tsp.showUtility()

# list = []
# for i in range(8):
#     tsp = TravelingSalesmanProblem(data_mode, csvfile, cities, height, width, time)
#     routes, utility, distance, elapsedTime = tsp.performEvolution(100, 70, 100, mutationFactor)
#     currentCity = 0
#     route = ''
#     list.append(distance)
#     print(list)
#     for itr in range(len(routes.keys())):
#         route = route + '->' + str(currentCity)
#         currentCity = routes[currentCity]
#     print("===== 20150359, Student =====")
#     print("Routes : %s" % (route))
#     print("Distance : ", distance)
#     print("Elapsed time : ", elapsedTime, "secs")
#     # tsp.showUtility()

# list = [[],[],[],[],[],[],[]]
# for i in range(7):
#     if i == 2 or i == 6:
#         for j in range(2):
#             tsp = TravelingSalesmanProblem(data_mode, csvfile, cities, height, width, time)
#             routes, utility, distance, elapsedTime = tsp.performEvolution(100, 70, 100, mutationFactor, i+1)
#
#             currentCity = 0
#             route = ''
#             for itr in range(len(routes.keys())):
#                 route = route + '->' + str(currentCity)
#                 currentCity = routes[currentCity]
#             print("===== 20150359, Student =====")
#             print("Routes : %s" % (route))
#             print("Distance : ", distance)
#             print("Elapsed time : ", elapsedTime, "secs")
#             list[i].append(distance)
#             print(list)
#     elif i == 4:
#         for j in range(1):
#             tsp = TravelingSalesmanProblem(data_mode, csvfile, cities, height, width, time)
#             routes, utility, distance, elapsedTime = tsp.performEvolution(100, 70, 100, mutationFactor, i+1)
#
#             currentCity = 0
#             route = ''
#             for itr in range(len(routes.keys())):
#                 route = route + '->' + str(currentCity)
#                 currentCity = routes[currentCity]
#             print("===== 20150359, Student =====")
#             print("Routes : %s" % (route))
#             print("Distance : ", distance)
#             print("Elapsed time : ", elapsedTime, "secs")
#             list[i].append(distance)
#             print(list)

# list = [[],[],[],[],[],[],[],[]]
# for i in range(0,21):
#     for j in range(1,8):
#         tsp = TravelingSalesmanProblem(data_mode, csvfile, cities, height, width, time)
#         routes, utility, distance, elapsedTime = tsp.performEvolution(100, 10 + i, 20 + i, mutationFactor, j)
#         currentCity = 0
#         route = ''
#         list[j-1].append([distance,10 + i,20 + i])
#         print(list)
#         for itr in range(len(routes.keys())):
#             route = route + '->' + str(currentCity)
#             currentCity = routes[currentCity]
#         print("===== 20150359, Student =====")
#         print("Routes : %s" % (route))
#         print("Distance : ", distance)
#         print("Elapsed time : ", elapsedTime, "secs")