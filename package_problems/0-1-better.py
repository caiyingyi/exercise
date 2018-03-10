import numpy as np


def solve2(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros((totalWeight) + 1, dtype=np.int32)
    for i in range(1, totalLength + 1):
        for j in range(totalWeight, 0, -1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j], resArr[j - wlist[i]] + vlist[i])
        print resArr
    return resArr[-1]


if __name__ == '__main__':
    v = [0, 60, 100, 120]
    w = [0, 10, 20, 30]
    weight = 50
    n = 3
    result = solve2(v, w, weight, n)
    print(result)
