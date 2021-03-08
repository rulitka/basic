def create_dict(s):
    count = {}
    for elem in s:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1
    return count

def SherlockValidString(s):
    number = 0
    Flag = True
    count_dict = create_dict(s)
    new_values = []    
    for i in count_dict.values():
        new_values.append(i)
    for elem in range(len(new_values) - 1):
        if number == 0:
            if new_values[elem] == new_values[elem + 1]:
                continue
            elif new_values[elem] != new_values[elem + 1]:
                number += 1
                if number == 1:
                    if new_values[elem + 1] - new_values[elem] == 1:
                        Flag = True
                        continue
                    elif new_values[elem] - new_values[elem + 1] == 1:
                        Flag = True
                        continue
                    else:
                        Flag = False
                else:
                   Flag = False
        else:
            Flag = False
    return Flag
