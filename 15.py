def TankRush(H1, W1, S1, H2, W2, S2):
    tmp = []
    new_string = ''
    number_of_elem_new_string = 0
    index_of_elem_result_S2 = 0
    pre_result_S1 = create_matrix(H1, W1, S1)
    result_S1 = ' '.join(pre_result_S1)
    result_S2 = create_matrix(H2, W2, S2)
    len_result_S2 = len(result_S2)
    Flag = False
    for i in range(len(result_S1)):
        if result_S1[i] == ' ':
            new_string = ''
            number_of_elem_new_string = 0
            continue                    
        else:
            if Flag == False:
                convert_element = result_S2[index_of_elem_result_S2]
                simbols = get_simbols(convert_element)
            else:
                pass
            new_string += result_S1[i]
            number_of_elem_new_string += 1
            if number_of_elem_new_string < simbols:
                Flag = True
                continue
            if number_of_elem_new_string == simbols:
                if len(result_S2) == len(tmp):
                    break
                else:
                    if  new_string == result_S2[index_of_elem_result_S2]:
                        tmp.append(new_string)
                        new_string = ''
                        number_of_elem_new_string -= 1
                        if index_of_elem_result_S2 < len_result_S2 - 1:
                            index_of_elem_result_S2 += 1
                            Flag = False
                        if index_of_elem_result_S2 == len_result_S2 - 1:
                            continue   
                    else:
                        new_string = remove_character(new_string, 0)
                        number_of_elem_new_string -= 1
                        Flag = True
                        continue
    if result_S2 == tmp:
        return True
    else:
        return False
       
def create_matrix(H, W, S):
    result_S = []
    result_S.append(str(H)) 
    result_S.append(str(W))
    S_n = S.split(" ")
    for i in range(len(S_n)):
        result_S.append(S_n[i])
    return result_S

def remove_character(new_string, index):
    s = list(new_string)
    del s[0]
    new_string = "".join(s)
    return new_string 

def get_simbols(convert_element):
    string_element = str(convert_element)
    simbols = 0
    for i in range(len(string_element)):
        simbols += 1
    return simbols
