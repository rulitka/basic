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
                    shift = temp_matrix.pop(0)
                    temp_matrix.append(shift)
                    continue
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
     

def MisterRobot(N, data):
    Flag = False
    n = 0
    while Flag == False:
        if n <= 200:        
            new_data = check_list(N, data)
            n += 1
            check_matrix_1 = check_matrix_one(new_data)
            if check_matrix_1 == True:
                Flag = True
            else:
               Flag = False
               continue
        if n > 200:
            Flag = False
            return Flag
    return Flag
