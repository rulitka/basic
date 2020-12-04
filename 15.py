def TankRush(H1, W1, S1, H2, W2, S2):
    tmp = []
    new_storke = ''
    number = 0
    lumber = 0
    result_S2 = S2.split(" ")
    for i in range(len(S1)):
        if S1[i] == ' ':
            new_storke = ''
            number = 0
            continue                    
        else:
            if number <= W2 - 1:
                new_storke += S1[i]
                number += 1
            if number == W2:
                if len(result_S2) == len(tmp):
                    break
                else:
                    if  new_storke == result_S2[lumber]:
                        tmp.append(new_storke)
                        if lumber < W2 - 1:
                            lumber += 1
                        if lumber == W2 - 1:
                            new_storke = remove_character(new_storke, 0)
                            number = 1
                            continue
                    else:
                        new_storke = remove_character(new_storke, 0)
                        number = 1
                        continue
    if result_S2 == tmp:
        return True
    else:
        return False
        
def remove_character(new_storke, index):
    s = list(new_storke)
    del s[0]
    new_storke = "".join(s)
    return new_storke
