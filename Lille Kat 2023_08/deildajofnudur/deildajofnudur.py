from sys import stdin

offeredGrants = int(next(stdin))
grantDedications = next(stdin).strip()


def canBeAccepted(n):
    for i in range(len(grantDedications)):
        d = addToDictionary(grantDedications[i : i + n])

        if i + n > len(grantDedications):
            return False
        elif isEqual(grantDedications[i], d):
            return True


def addToDictionary(list):
    d = {}
    for i in list:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d


def isEqual(i0, dic):
    for key in dic.keys():
        if dic[key] != dic[i0]:
            return False
    return True


for i in range(offeredGrants, -1, -1):
    if canBeAccepted(i):
        print(i)
        exit(0)
