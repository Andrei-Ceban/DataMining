from mpi4py import MPI
from getData import getAdjList
from map import maper
from reduce import reduce
from dictList import Dictlist

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
status = MPI.Status()

startTag = 10
mapTag = 11
reduceTag = 12
stopTag = 13
ready = 14
condition = True

master = 0

startNode = 3

if rank != master:
    comm.send(ready, dest=0, tag=startTag)

if rank == master:
    adjList = getAdjList()

    comm.recv(source=MPI.ANY_SOURCE, tag=startTag, status=status)
    dataToSend = {"NodeID": startNode, "Structure": {"adjacecyList": adjList[str(startNode)], "distance": 0, "distances": {}}}
    comm.send(dataToSend, dest=status.source, tag=mapTag)
    oldDistances = {}
    counter = 0
    while (True):

        distances = comm.recv(source=MPI.ANY_SOURCE, tag=mapTag, status=status)


        for d in distances:
            oldDistances[d] = distances[d]
            print(oldDistances)
            stat = comm.recv(source=MPI.ANY_SOURCE, tag=startTag, status=status)
            if stat == ready:
                dataToSend = {"NodeID": d, "Structure": {"adjacecyList": adjList[str(d)], "distance": distances[d], "distances": oldDistances}}
                comm.send(dataToSend, dest=status.source, tag=mapTag)
        counter += 1
        if counter == 4:
            break
else:
    while(True):
        data = comm.recv(source=master, tag=mapTag, status=status)
        precDistances = data["Structure"]["distances"]
        newDistances = maper(data["NodeID"], data["Structure"])
        distances = reduce(data["NodeID"], newDistances, precDistances)
        comm.send(distances, dest=status.source, tag=mapTag)
        comm.send(ready, dest=0, tag=startTag)
        break


