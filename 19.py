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


def summ_elements(inputStrNew):
    N_new = len(inputStrNew)
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
    len_new_items = len(new_items)
    if len_new_items == 1:
        result = True
        exit
    else:
        for i in range(len(new_items) - 1):
            if new_items[i][0] == new_items[i + 1][0]:
                result = False
                break
            else:
                result = True
    return result


def merge_string(inputStrNew):
    for i in range(len(inputStrNew)):
        inputStrNew[i][1] = str(inputStrNew[i][1])
    return inputStrNew 


def return_to_start(start_string):
    end_string = []
    for i in range(len(start_string)):
        end_string.append(" ".join(start_string[i]))
    return end_string


def ShopOLAP(N, items):
    divide_it = divide_string(N, items)
    inputStrRes = sortByName(divide_it)
    result = False
    while result == False:
        new_items = summ_elements(inputStrRes)
        result = search_dubl(new_items)
    inputStrNew = sortByLength(new_items)
    start_string =  merge_string(inputStrNew)
    end_string = return_to_start(start_string)
    return end_string
