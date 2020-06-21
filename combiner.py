def combiner(itemSetDict):
    combinedItemSetDict = {}
    for itemSet in itemSetDict:
        combinedItemSetDict[itemSet] = len(itemSetDict[itemSet])
    return combinedItemSetDict