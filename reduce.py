def reduce(totalItemSetDict, minSupport):
    goodSupport = {}
    for item in totalItemSetDict:
        support = 10
        for i in totalItemSetDict[item]:
            support += i
        if support >= minSupport:
            goodSupport[item] = support
    return goodSupport
