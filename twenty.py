final_string = ''
history = []
position_in_history = -1
Flag = False


def check_string(command):
    elem = []
    len_str = len(command)
    if len_str < 1:
        elem = []
    if len_str == 1:
        for i in range(len(command)):
            if command[i].isdigit() == True:
                elem.append(int(command[i]))
            else:
                elem.append((command[i]))
    if len_str > 1:
        elem_temp = command.split(" ", 1)
        for i in range(len(elem_temp)):
            if i == 0:
                check_elem = elem_temp[i]
                if check_elem.isdigit() == True:
                        elem.append(int(elem_temp[i]))
                        if elem[0] == 1:
                            elem.append(elem_temp[1])
                        if 1 < elem[0] < 6:
                            elem.append(int(elem_temp[1]))
                        if elem[0] >= 6:
                            elem.append((elem_temp[1]))
                else:
                    elem = elem_temp
    return elem


def reset_history():
    global history
    global position_in_history
    history_new = []
    for i in range(len(history)):
        if i == position_in_history:
            history_new.append(history[i])
        else:
            continue
    history = history_new
    position_in_history = 0
    return history


def add_string(check_str):
    global Flag
    global final_string
    global history
    global position_in_history
    if Flag == False:
        final_string += check_str[1]
        history.append(final_string)
        position_in_history += 1
    if Flag == True:
        final_string += check_str[1]
        history = reset_history()
        history.append(final_string)
        position_in_history += 1
    Flag = False
    return final_string


def del_elements(check_str):
    global final_string
    global history
    global position_in_history
    global Flag
    if Flag == False:
        n = check_str[1]
        len_str = len(final_string)
        if n > len_str:
            final_string = ''
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
        history = reset_history()
        history.append(final_string)
        position_in_history += 1
    return final_string


def get_index_element(check_str):
    global final_string
    final_elem = ''
    index_el = check_str[1]
    len_str = len(final_string)
    if index_el >= len_str:
        final_elem = ''
        exit
    else:
        final_elem = str(final_string[index_el])
    return final_elem


def undo_position():
    global final_string
    global history
    global position_in_history
    global Flag
    if position_in_history == 0:
        position_in_history = 0
        final_string = history[position_in_history]
    if position_in_history != 0:
        position_in_history -= 1
        final_string = history[position_in_history]
    Flag = True
    return final_string


def redo_position(check_str):
    global final_string
    global history
    global position_in_history
    if history[position_in_history] == history[-1]:
        final_string = history[position_in_history]
    else:
        position_in_history += 1
        final_string = history[position_in_history]
    return final_string


def BastShoe(command):
    check_str = check_string(command)
    final_elem = ''
    global final_string
    if check_str[0] == 1:
        final_string = add_string(check_str)
    if check_str[0] == 2:
        final_string = del_elements(check_str)
    if check_str[0] == 3:
        final_elem = get_index_element(check_str)
        return final_elem
    if check_str[0] == 4:
        final_string = undo_position()
    if check_str[0] == 5:
        final_string = redo_position(check_str)
    return final_string
