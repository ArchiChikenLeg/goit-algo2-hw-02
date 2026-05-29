def min_max_find(arr):
    if len(arr) == 1:
        return arr[0],arr[0]
    if len(arr) == 2:
        if(arr[0] >= arr[1]):
            return arr[1], arr[0]
        else:
            return arr[0], arr[1]
    leftPart = arr[:len(arr)//2]
    rightPart = arr[len(arr)//2:]

    lftMin, lftMax = min_max_find(leftPart)
    rgtMin, rgtMax = min_max_find(rightPart)

    if lftMin >= rgtMin:
        finMin = rgtMin
    else: 
        finMin = lftMin

    if lftMax >= rgtMax:
        finMax = lftMax
    else:
        finMax = rgtMax

    return finMin, finMax

##print(len([2, -4, 1, 9, -6, 7, -3]))
print(min_max_find([2, -4, 1, 9, -6, 7, -3]))