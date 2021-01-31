def divide_string(N, items):
    items_split = [0]*N
    n = 0
    for i in range(len(items)):
        elem = items[i].split()
        elem[1] = int(elem[1])
        elem_new = list(elem)
        items_split[n] = elem_new
        n += 1
    return items_split


def sortByName(divide_it):
    newList = sorted(divide_it)
    return newList

def summ_elements(N, inputStrNew):
    N_new = N
    z = 0
    for i in range(len(inputStrNew) - 1):
        if z < N_new - 1:
            if inputStrNew[i][0] == inputStrNew[i + 1][0]:
                inputStrNew[i][1] = inputStrNew[i][1] + inputStrNew[i+ 1][1]
                inputStrNew.pop(i+1)
                N_new = len(inputStrNew)
                z += 1
            else:                
                z += 1
        if z == N_new:
            break
    return inputStrNew


def sortByLength(new_items):
    inputStrNew = sorted(new_items, key=lambda x: (-x[1], x[0]))
    return inputStrNew

def search_dubl(new_items):
    result = False
    for i in range(len(new_items) - 1):
        if new_items[i][0] == new_items[i + 1][0]:
            result = False
            break
        else:
            result = True
    return result


def ShopOLAP(N, items):
    divide_it = divide_string(N, items)
    inputStrRes = sortByName(divide_it)
    result = False
    while result == False:
        new_items = summ_elements(N, inputStrRes)
        result = search_dubl(new_items)
    inputStrNew = sortByLength(new_items)
    return inputStrNew
