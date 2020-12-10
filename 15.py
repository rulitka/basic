def TankRush(H1, W1, S1, H2, W2, S2):
    tmp = []
    new_stroke = ''
    number = 0
    lumber = 0
    result_S2 = create_matrix(H2, W2, S2)
    len_result_S2 = len(result_S2)
    Flag = False
    for i in range(len(S1)):
        if S1[i] == ' ':
            new_stroke = ''
            number = 0
            continue                    
        else:
            if Flag == False:
                convert_element = result_S2[lumber]
                simbols = get_simbols(convert_element)
            else:
                pass
            new_stroke += S1[i]
            number += 1
            if number < simbols:
                Flag = True
                continue
            if number == simbols:
                if len(result_S2) == len(tmp):
                    break
                else:
                    if  new_stroke == result_S2[lumber]:
                        tmp.append(new_stroke)
                        new_stroke = ''
                        number = 0
                        if lumber < len_result_S2 - 1:
                            lumber += 1
                            Flag = False
                        if lumber == len_result_S2 - 1:
                            continue   
                    else:
                        new_stroke = remove_character(new_stroke, 0)
                        number -= 1
                        Flag = True
                        continue
    if result_S2 == tmp:
        return True
    else:
        return False
       
def create_matrix(H2, W2, S2):
    result_S2 = []
    result_S2.append(str(H2))
    result_S2.append(str(W2))
    S2 = S2.split(" ")
    for i in range(len(S2)):
        result_S2.append(S2[i])
    return result_S2

def remove_character(new_stroke, index):
    s = list(new_stroke)
    del s[0]
    new_stroke = "".join(s)
    return new_stroke

def get_simbols(convert_element):
    stroke_element = str(convert_element)
    simbols = 0
    for i in range(len(stroke_element)):
        simbols += 1
    return simbols
