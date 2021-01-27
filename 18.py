def check_list(N, data):    
    temp_matrix = []
    for i in range(len(data) - 2):
        temp_matrix.append(data[i])
        temp_matrix.append(data[i + 1])
        temp_matrix.append(data[i + 2])
        for j in range(len(temp_matrix) - 1):
            if temp_matrix[j + 1] > temp_matrix[j]:
                continue
            else:
                for _ in range(0, 2):
                    if temp_matrix[_] < temp_matrix[_ + 1]:
                        continue
                    else:
                        shift = temp_matrix.pop(_)
                        temp_matrix.append(shift)
                        for _ in range(0, 2):
                            if temp_matrix[_] < temp_matrix[_ + 1]:
                                continue
                            else:
                                shift = temp_matrix.pop(_)
                                temp_matrix.append(shift)
                data[i] =  temp_matrix[0]
                data[i + 1] =  temp_matrix[1]
                data[i + 2] =  temp_matrix[2]
        exit
        temp_matrix = []
    exit
    return data

def check_matrix_one(new_data):
    Flag = True
    for i in range(1, len(new_data)):
        if new_data[i] <= new_data[i-1]:
            Flag = False
            break
        else:
            Flag = True
    return Flag
    
def check_matrix_two(new_data):
    Flag = True
    x = 1 
    for i in range(1, len(new_data)):
        if new_data[i] - new_data[i-1] != x:
            Flag = False
            break
        else:
            Flag = True
    return Flag       

def MisterRobot(N, data):
    Flag = False
    while Flag == False:    
        new_data = check_list(N, data)
        check_matrix_1 = check_matrix_one(new_data)
        if check_matrix_1 == True:
            Flag = True
        else:
            Flag = False
            continue
    if Flag == True:
        check_matrix_2 = check_matrix_two(new_data)
        if check_matrix_2 == False:
            Flag = False
            exit
        else:
            Flag = True
            exit
    return Flag
