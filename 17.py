def LineAnalysis(line):
    first_check = chech_first_last(line)
    if first_check == True:
        if len(line) <= 3:
            return True
        if len(line) > 3:  
            new_matrix = check_string(line)
            result = check_index(new_matrix)
    else:
        return False
    return result


def chech_first_last(line):
    Flag = True
    if len(line) == 1:
        if line[0] == '*':
            Flag = True
        else:
            Flag = False
    if len(line) >= 2: 
        if line[0] == '*':
            Flag = True
        else:
            Flag = False
        if line[-1] == '*':
            Flag = True
        else:
            Flag = False 
    return Flag


def check_string(line):
    new_matrix = []
    for i in range (len(line)):
        if line[i] == '*':
            new_matrix.append(i)
    return new_matrix


def check_index(new_matrix):
    Flag = True
    x = new_matrix[1] - new_matrix[0]
    for i in range(2, len(new_matrix)):
        if new_matrix[i] - new_matrix[i-1] != x:
            Flag = False
            break
        else:
            Flag = True
    return Flag
