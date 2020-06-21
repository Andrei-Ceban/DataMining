from itertools import chain, combinations
from combiner import combiner
from dictList import Dictlist

def maper(data, maxNrInCombination):
    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(maxNrInCombination + 1))
    itemSetDict = Dictlist()
    for ind, transaction in enumerate(data):
        transactionItems = str(transaction[0:-1]).split(' ')
        for combo in powerset(transactionItems):
            if combo:
                itemSetDict[combo] = 1
    return combiner(itemSetDict)