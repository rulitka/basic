def check_similar(in_put):
    Flag = True
    for i in range(len(in_put) - 1):
        next_simbol = in_put[i+1]
        if in_put[i] == next_simbol:
            Flag = False
            continue
        else:
            continue
    return Flag

def rotateChar(in_put):
    temp_matrix = list(in_put)
    for i in range(1, len(temp_matrix), 2):
        temp_matrix[i - 1], temp_matrix[i] = temp_matrix[i], temp_matrix[i - 1]
        string = ''.join([str(i) for i in temp_matrix])
    return string


def oddswap(in_put):
    temp_matrix = list(in_put)
    full_matrix = []
    part_matrix= []

        
    for c in range(0,len(temp_matrix),2):
        if c < 1:
            continue
        if c > 1:
            t=temp_matrix[c]
            temp_matrix[c]=temp_matrix[c+1]
            temp_matrix[c+1]=t
            string = "".join(temp_matrix)
            full_matrix.append(string)
            
    for c in range(0,len(temp_matrix),2):
        t=temp_matrix[c]
        temp_matrix[c]=temp_matrix[c+1]
        temp_matrix[c+1]=t
        string = "".join(temp_matrix)
        full_matrix.append(string)
    return full_matrix


def BiggerGreater(in_put):
    new_string = ''
    result = ''
    checked_string = check_similar(in_put)
    if checked_string == True:
        length_str = len(in_put)
        if length_str == 2:
            new_string = rotateChar(in_put)
            if new_string > in_put:
                result = new_string
            else:
                result = ''
        elif length_str > 2:
            new_string = oddswap(in_put) 
            sort_string = sorted(new_string)
            result = sort_string[0]
    elif checked_string == False:
        return result
    return result
