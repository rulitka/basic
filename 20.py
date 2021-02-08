def check_string(command):
    elem =[]
    len_str = len(command)
    if len_str == 1:
        for i in range(len(command)):
            elem.append(int(command[i]))
    if len_str > 1:
        elem_temp = command.split(" ", 1)
        for i in range(len(elem_temp)):
            if i == 0:
                elem.append(int(elem_temp[i]))
                if elem[0] == 1:
                    elem.append(elem_temp[1])
                else:
                    elem.append(int(elem_temp[1]))
    return elem

def reset_history(history, position_in_history):
    history_new = []
    for i in range(len(history)):
        if i == position_in_history:
            history_new.append(history[i])
        else:
            continue
    history = history_new
    return history

def BastShoe(command):
    final_string = ''
    history = []
    position_in_history = -1
    Flag = False
    for i in range(len(command)):
        check_str = check_string(command[i])
        if check_str[0] == 1:
            if Flag == False:
                final_string += check_str[1]
                history.append(final_string)
                position_in_history += 1
            if Flag == True:
                final_string += check_str[1]
                history = reset_history(history, position_in_history)
                history.append(final_string)	
        if check_str[0] == 2:
            if Flag == False:
                n = check_str[1]
                len_str = len(final_string)
                if n > len_str:
                    final_string = ' '
                    exit
                else:
                    while n:
                        final_string = final_string[:-1]
                        n -= 1
                        history.append(final_string)
                    position_in_history += 1        
            if Flag == True:
                n = check_str[1]
                while n:
                    final_string = final_string[:-1]
                    n -= 1
                history = reset_history(history, position_in_history)
                history.append(final_string)
                position_in_history += 1
        if check_str[0] == 3:
            index_el = check_str[1]
            len_str = len(final_string)
            if index_el > len_str:
                final_string = ' '
                exit
            else:
                final_string = str(final_string[index_el])
        if check_str[0] == 4:
            if position_in_history == 0:
                position_in_history = 0
                final_string = history[position_in_history]            	
            if position_in_history != 0:	
                position_in_history -= 1
                final_string = history[position_in_history]
            Flag = True
        if check_str[0] == 5:
            if history[position_in_history] == history[-1]:
                final_string = history[position_in_history]
            else:
                position_in_history += 1
                final_string = history[position_in_history]
    return final_string
