def rotatedArrays(box):
    res = []
    res.append(box)
    res.append([box[1], box[2], box[0]])
    res.append([box[2], box[0], box[1]])
    return res


def comparePackage(pkg, rotatedArrays):
    for box in rotatedArrays:
        if pkg[0] <= box[0] and pkg[1] <= box[1] and pkg[2] <= box[2]:
            return True
    return False


def volume(box):
    return box[0] * box[1] * box[2]


def packageBoxing(pkg, boxes):
    minVol = 10000000000
    minIndex = -1
    finalres = False
    for i, box in enumerate(boxes):

        rotatedArray_boxes = rotatedArrays(box)
        rotatedArray_pkgs = rotatedArrays(pkg)
        if i == 7: print rotatedArray_boxes
        for p in rotatedArray_pkgs:
            res = comparePackage(p, rotatedArray_boxes)
            print res, i
            finalres = res or finalres
        if finalres == True:
            print i, volume(box)
            if (volume(box) < minVol):
                minIndex = i
                minVol = volume(box)
            finalres = False

    return minIndex


pkg = [16, 48, 91]

boxes = [[23, 91, 82],
         [32, 5, 64],
         [24, 29, 74],
         [91, 86, 74],
         [64, 69, 59],
         [37, 32, 96],
         [18, 14, 84],
         [78, 18, 97],
         [50, 67, 37],
         [20, 46, 48],
         [86, 29, 19],
         [32, 28, 72]]

print packageBoxing(pkg, boxes)
