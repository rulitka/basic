def TankRush(H1, W1, S1, H2, W2, S2):
    pre_result_S1 = create_matrix(H1, W1, S1)
    print(pre_result_S1)
    pre_result_S2 = create_matrix(H2, W2, S2)
    print(pre_result_S2)
    tmp = [[0] * W2 for i in range(H2)] #создаем временный массив
    x = 0
    y = 0
    num = 0
    lum = 0
    for i in range(len(pre_result_S1)): 
        for j in range(len(pre_result_S1[i])):
            print(pre_result_S1[i][j])
            print(pre_result_S2[x][y])
            if pre_result_S2 == tmp:
                break
            else:
                if pre_result_S1[i][j] == pre_result_S2[x][y]:
                    tmp = check_matrix(i, j, pre_result_S1, pre_result_S2, H2, W2, tmp)
                    if pre_result_S2 == tmp:
                    	break
                    else:
                        continue
                else:
                    continue
    if pre_result_S2 == tmp:
        print(tmp)
        return True
    else:
        return False


def check_matrix(i, j, pre_result_S1, pre_result_S2, H2, W2, tmp):
    ci = 0
    cj = 0
    a = (i, j)
    number_of_elem_row = 0
    number_of_H2 = 1          
    while number_of_H2 <= H2:
        if pre_result_S2 == tmp:
            break
        else:
            if number_of_elem_row < W2:
                tmp[ci][cj] = pre_result_S1[i][j]
                number_of_elem_row += 1
                cj += 1
                j += 1
                continue
            if number_of_elem_row == W2:
                ci += 1
                cj = 0
                i += 1
                j = a[1]
                number_of_elem_row = 0
                number_of_H2 += 1
    return tmp


def create_matrix(H, W, S):
    result_S = []
    result_S = [0] * H
    a = 0
    j = 0
    for i in range(H):
        result_S[i] = [0] * W
    
    for i in range(len(S)):
        if S[i] == ' ':
            a += 1
            j = 0
            pass
        else:
            result_S[a][j] = int(S[i])
            j += 1
            continue
    return result_S
