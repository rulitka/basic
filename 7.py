def WordSearch(width, s, subs):
    s_new = s.split()  
    capacity = width # сколько места в текущей строке  
    cur_s = 0
    result = []
    for word in s_new:
        flag = True if word == subs else False  # искомое слово или нет
        length = len(word)
        
        if capacity == width and capacity >= length: # добавляем в пустую строку и все влезло
            capacity -= length
            if flag:
                result.append(1)
            else:
                result.append(0)
            continue
        
        if capacity != width and capacity > length: # добавляем в непустую строку и все влезло
            capacity -= length + 1
            if flag:
                result[-1] = 1
            continue 
        
        if length <= width: # в текущую строку не влезло и влезло в НОВУЮ пустую
            cur_s += 1
            capacity = width - length
            if flag:
                result.append(1)
            else:
                result.append(0)
            continue 
            
        while length > width:
            cur_s += 1
            length -= width
            check(result,flag, cur_s)
            if flag:
                result.append(1)
            else:
                result.append(0)   
                 
        cur_s += 1
        capacity -= length
        check(result,flag, cur_s)  
        if flag:
                result.append(1)
        else:
                result.append(0)  
        
    return result
