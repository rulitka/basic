def swapPosition(F, pos1, pos2):
    get = F[pos1], F[pos2]
    F[pos2], F[pos1] = get
    return F

def rule_one(F):
    Flag = True
    n = 0
    m = 0
    length = len(F)
    pos1 = 0
    pos2 = 0
    for i in range(1, len(F)):
        if F[i]!= F[-1]:
            if F[i] < F[i - 1]:
                if F[i] < F[i + 1]:
                    if F[i + 1] == F[- 1]:
                        if n == 0:
                            pos1 = i - 1
                            n += 1
                            continue
                        if n != 0:
                            if m == 0:
                                pos2 = i
                                m += 1
                            if m != 0:
                                pass
                if F[i + 1] != F[- 1]:
                    if F[i - 1] - F[i] == F[i + 1] - F[i - 1]:
                        if n == 0:                    
                            pos1 = i - 1
                            n += 1
                            continue
                        if n != 0:
                            if m == 0:
                                pos2 = i
                                m += 1
                            if m != 0:
                                pass
                    if F[i - 1] - F[i] == F[i + 1] - F[i - 1]:
                        pass
                if F[i] > F[i + 1]:
                    pass
            if F[i] >  F[i - 1]:
                if F[i] < F[i + 1]:
                    pass
                if F[i] > F[i + 1]:
                    if n == 0:
                        pos1 = i
                        n += 1
                    if n != 0:
                        pass
        if F[i] == F[-1]:
            if F[i] < F[i - 1]:
                if m == 0:
                    pos2 = i
                    m += 1
                if m != 0:
                    pass
            if F[i] > F[i - 1]:
                pass
    F_new = swapPosition(F, pos1, pos2)
    return F_new

def rule_two(F):
    for i in range(len(F) // 2):
        tmp = F[i]
        F[i] = F[len(F) - i - 1]
        F[len(F) - i - 1] = tmp
    return F

def isMonotonic(A):  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


def check_monotone(F):
    Flag = True
    temp_array_ubyv = []
    for i in range(1, len(F)):
        if F[i]!= F[-1]:
            if F[i] == F[0]:
                if F[0] > F[i + 1]:
                    temp_array_ubyv.append(F[0])
                if F[0] < F[i + 1]:
                    temp_array_vosr.append(F[0 + 1])
            if F[i] != F[0]:        
                if  F[i + 1] > F[i] > F[i - 1]:
                    pass
                if F[i + 1] < F[i] < F[i - 1]:
                    temp_array_ubyv.append(F[i])
                if F[i + 1] < F[i] > F[i - 1]:
                    temp_array_ubyv.append(F[i])
                if F[i + 1] > F[i] < F[i - 1]:
                    temp_array_ubyv.append(F[i])
        if F[i] == F[-1]:
            if F[i] > F[i - 1]:
                pass
            if F[i] < F[i - 1]:
                temp_array_ubyv.append(F[i])
    result = isMonotonic(temp_array_ubyv)
    if result is True:
        Flag = True
    if result is False:
        Flag = False
    return Flag

def check_past(temp_result):
    Flag = True
    for i in range(1, len(temp_result)):
        if temp_result[i] > temp_result[i - 1]:
            Flag = True
        elif temp_result[i] < temp_result[i - 1]:
            Flag = False
            break
    return Flag

def Football(F, N):
    Flag = True
    n = 0
    if F[0] < F[1]:
        for i in range(1, len(F)):
            if F[i]!= F[-1]:
                if F[i] >  F[i - 1]:
                    if F[i] > F[i + 1]:
                        n += 1
                    if F[i] < F[i + 1]:
                        pass
                if F[i] <  F[i - 1]:
                    if F[i] < F[i + 1]:
                        n += 1
                    if F[i] > F[i + 1]:
                        n += 1
            if F[i] == F[-1]:
                if F[i] < F[i - 1]:
                    n += 1
                if F[i] > F[i - 1]:
                    pass        
        if n < 2:
            temp_result = F
        if n == 2:
            temp_result = rule_one(F)
        if n > 2:
            half_result = check_monotone(F)
            if half_result is True:
                temp_result = sorted(F)
            if half_result is False:
                temp_result = F	
    if F[0] > F[1]:
        temp_result = rule_two(F)
    result = check_past(temp_result)
    if result is True:
        Flag = True
    if result is False:
        Flag = False
    return Flag
