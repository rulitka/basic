def TankRush(H1, W1, S1, H2, W2, S2):
    tmp = []
    new_storke = ''
    number_of_elem_new_stroke = 0
    index_of_elem_result_S2 = 0
    pre_result_S1 = create_matrix(H1, W1, S1)
    result_S1 = ' '.join(pre_result_S1)
    result_S2 = create_matrix(H2, W2, S2)
    len_result_S2 = len(result_S2)
    Flag = False
    for i in range(len(result_S1)):
        if result_S1[i] == ' ':
            new_storke = ''
            number_of_elem_new_stroke = 0
            continue                    
        else:
            if Flag == False:
                convert_element = result_S2[index_of_elem_result_S2]
                simbols = get_simbols(convert_element)
            else:
                pass
            new_storke += result_S1[i]
            number_of_elem_new_stroke += 1
            if number_of_elem_new_stroke < simbols:
                Flag = True
                continue
            if number_of_elem_new_stroke == simbols:
                if len(result_S2) == len(tmp):
                    break
                else:
                    if  new_storke == result_S2[index_of_elem_result_S2]:
                        tmp.append(new_storke)
                        new_storke = ''
                        number_of_elem_new_stroke -= 1
                        if index_of_elem_result_S2 < len_result_S2 - 1:
                            index_of_elem_result_S2 += 1
                            Flag = False
                        if index_of_elem_result_S2 == len_result_S2 - 1:
                            continue   
                    else:
                        new_storke = remove_character(new_storke, 0)
                        number_of_elem_new_stroke -= 1
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

def remove_character(new_storke, index):
    s = list(new_storke)
    del s[0]
    new_storke = "".join(s)
    return new_storke 

def get_simbols(convert_element):
    stroke_element = str(convert_element)
    simbols = 0
    for i in range(len(stroke_element)):
        simbols += 1
    return simbols
