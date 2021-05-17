def to_bool(new_matrix):
    for i in range(len(new_matrix)):
        if new_matrix[i]  == True:
            new_matrix[i] = '1'
        elif new_matrix[i]  == False:
            new_matrix[i] = '0'
    return  new_matrix

def Keymaker(k):
    new_matrix = [False]*k
    for i in range(1, k + 1):
        for index in range(i - 1, len(new_matrix), i):
            new_matrix[index] = not new_matrix[index]
        #print(new_matrix)
    convert_array = to_bool(new_matrix)
    result = ''.join(convert_array)
    return result
