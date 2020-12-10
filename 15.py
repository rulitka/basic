def TankRush(H1, W1, S1, H2, W2, S2):
    tmp = []
    new_storke = ''
    number = 0
    lumber = 0
    result_S2 = create_matrix(H2, W2, S2)
    len_result_S2 = len(result_S2)
    Flag = False
    for i in range(len(S1)):
        if S1[i] == ' ':
            new_storke = ''
            number = 0
            continue                    
        else:
            if Flag == False:
                convert_element = result_S2[lumber]
                simbols = get_simbols(convert_element)
            else:
                pass
            new_storke += S1[i]
            number += 1
            if number < simbols:
                Flag = True
                continue
            if number == simbols:
                if len(result_S2) == len(tmp):
                    break
                else:
                    new_storke_int = int(new_storke)
                    if  new_storke_int == result_S2[lumber]:
                        tmp.append(new_storke_int)
                        new_storke = ''
                        number -= 1
                        if lumber < len_result_S2 - 1:
                            lumber += 1
                            Flag = False
                        if lumber == len_result_S2 - 1:
                            continue   
                    else:
                        new_storke = remove_character(new_storke, 0)
                        number -= 1
                        Flag = True
                        continue
    if result_S2 == tmp:
        return True
    else:
        return False
       
def create_matrix(H2, W2, S2):
    result_S2 = []
    result_S2.append(H2) 
    result_S2.append(W2)
    S2 = S2.split(" ")
    for i in range(len(S2)):
        result_S2.append(int(S2[i]))
    return result_S2

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
