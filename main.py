from mpi4py import MPI
from getData import getLines
from map import maper
from reduce import reduce
from dictList import Dictlist

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
N = comm.Get_size()
status = MPI.Status()

mapTag = 11
reduceTag = 12
stopTag = 13
ready = 14
condition = True

master = 0

if rank != master:
    comm.send(ready, dest=0, tag=mapTag)

if rank == master:
    dataDict = getLines(N)

    for data in dataDict:
        info = comm.recv(source=MPI.ANY_SOURCE, tag=mapTag, status=status)

        if info == ready:
            comm.send(dataDict[data], dest=status.source, tag=mapTag)
    totalItemSetDict = Dictlist()

    for i in range(1, N):
        combinedItemSetDict = comm.recv(source=MPI.ANY_SOURCE, tag=reduceTag, status=status)
        for item in combinedItemSetDict:
            totalItemSetDict[item] = combinedItemSetDict[item]
    minSupport = 100
    goodSupport = reduce(totalItemSetDict, minSupport)
    for i in goodSupport:
        print(str(i) + ' - Support = ' + str(goodSupport[i]))

else:
    while(condition):
        data = comm.recv(source=master, tag=mapTag, status=status)
        maxNrInCombination = 2
        if data:
            combinedItemSetDict = maper(data, maxNrInCombination)
            comm.send(combinedItemSetDict, dest=master, tag=reduceTag)
            condition = False