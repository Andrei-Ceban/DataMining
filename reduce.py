def reduce(nodeID, newdistances, precDistances):
    for d in newdistances:
        try:
            if newdistances[d] < precDistances[d]:
                precDistances[d] = newdistances[d]
        except:
            precDistances[d] = newdistances[d]

    return precDistances