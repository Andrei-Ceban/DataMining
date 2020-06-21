def maper(nodeID, N):
    d = N["distance"]
    newDistances = {}
    for node in N["adjacecyList"]:
        newDistances[node] = d + 1
    return newDistances

