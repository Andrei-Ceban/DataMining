import math


def getLines(N):
    data = []
    dict = {}
    num_lines = sum(1 for line in open('retail.dat.txt'))
    nrOfLinesToTake = math.floor(num_lines / (N - 1))
    f = open("retail.dat.txt", "r")

    i = 1
    for index, x in enumerate(f):
        data.append(x)
        if index != 0 and index % nrOfLinesToTake == 0 and i != N-1:
            dict[i] = data
            i += 1
            data = []
        elif index == num_lines - 1:
            dict[i] = data
    return dict