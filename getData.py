from dictList import Dictlist


def getAdjList():
    adjList = Dictlist()

    f = open("graph.txt", "r")

    for index, x in enumerate(f):
        if str(x).split('  ')[1]:
            adjList[str(x).split('  ')[0]] = str(x).split('  ')[1][1]

    return adjList