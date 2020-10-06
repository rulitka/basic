def WordSearch(width, s, subs):
    s_new = s.split()
    new = [""]
    
    for word in s_new:
        if len(word) <= width:
            if new[-1] == "":
                new[-1] = word
            elif len(word) + len(new[-1]) < width:
                new[-1] += " " + word
            else:
                if len(word) <= width:
                    new.append(word)
                else:
                    new.append(word[:width])
                    new.append(word[width:])
       
        else:
            if new[-1] == "":
                new[-1] = word[:width]
                new.append(word[width:])
            else:    
                new.append(word[:width])
                new.append(word[width:])
        answer = count(new, subs)
    return answer

def count(new, subs):
    k = 0
    result = []
    for x in new:
        if subs in x:
            for i, t in enumerate(x):
                if t == subs[k]:
                    if k == len(subs) - 1:
                        if t == x[-1]:
                            result.append(1)
                            k = 0
                        elif x[i+1]== ' ':
                            result.append(1)
                            k = 0
                        else:
                            result.append(0)
                    else:
                        k += 1
                else:
                    continue    
        else:
            k = 0
            result.append(0)
    return result
