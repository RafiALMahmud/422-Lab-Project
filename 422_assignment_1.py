from heapq import heappop, heappush


def a_Star_Search_Algo(romainianMapToGraph, start, goal, heuristics):
    
    nextNeighborNodes, eveluatedNodes = [(heuristics[start], start)], set()

    while nextNeighborNodes:
        startToNthCost, node = heappop(nextNeighborNodes)
        parents.append(node)

        if node == goal:
            return [startToNthCost, parents]
        
        if node in eveluatedNodes:
            continue
        eveluatedNodes.add(node)
        startToNthCost -= heuristics[node]

        for neighbour, edge_cost in romainianMapToGraph[node]:
            if neighbour in eveluatedNodes:
                continue
            
            if neighbour == goal:
                allRoutesToGoal[node] = (neighbour, startToNthCost + edge_cost)

            evaluation_func = startToNthCost + edge_cost + heuristics[neighbour]
            heappush(nextNeighborNodes, (evaluation_func, neighbour))

    return -1


input_file = "LOCATION OF THE INPUT FILE"
romainianMapToGraph, heuristicsExtracted = {}, {}
allRoutesToGoal = {}
parents = []

file = open(input_file, 'r')

for neighbourNodes in file:

    lines = neighbourNodes.split()
    neighbors = []
    
    for paths in range(2, len(lines)):
        if paths % 2 == 0:
            if paths + 1 < len(lines):
                neighbors.append((lines[paths], int(lines[paths + 1])))

    romainianMapToGraph[lines[0]] = neighbors

    heuristicsExtracted[lines[0]] = int(lines[1])


startNode, destination = input("Start node: "), input('Destination: ')
finalArray = a_Star_Search_Algo(romainianMapToGraph, startNode, destination, heuristicsExtracted)
totalDistance = finalArray[0]

if finalArray != -1:

    if heuristicsExtracted[destination] != 0:
        totalDistance -= heuristicsExtracted[destination]
    
    path = finalArray[1]
    lowestPathCost = min(allRoutesToGoal.values())

    for k, v in allRoutesToGoal.items():
        if v != lowestPathCost:
            path.remove(k)

    print(f'Path: ', end='')
    for p in range(len(path) - 1):
        print(path[p], end=' -> ')
    print(path[-1])
    print(f"Total Distance: {totalDistance} km")

else:
    print('NO PATH FOUND')


file.close()