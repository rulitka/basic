def Unmanned(L, N, track):
    num = 0
    number_of_tr_light = 0
    real_time = 0
    for i in range(1, L+1):
        tr_light = track[number_of_tr_light][0]
        if i == tr_light:
            real_time += 1
            num += 1
            red = track[number_of_tr_light][1]
            green = track[number_of_tr_light][2]
            color_tl = get_color(real_time,red, green, flag = True)
            if color_tl == 'red':
                while color_tl =='red':
                    real_time += 1
                    color_tl = get_color(real_time,red, green, flag = True)
                if color_tl == 'green':
                    real_time -= 1
            if color_tl == 'green':
                if num < N:
                    number_of_tr_light += 1
                    print(number_of_tr_light)
                if num == N:
                    continue
        else:
            real_time += 1
    return real_time
        

def get_color(real_time,red, green, flag = True):
    counter = 1
    for i in range(1, real_time+1):
        if flag == True:
            if counter <= red:
                result = 'red'
                counter +=1
            else:
                counter = 1
                flag = False
                if counter <= green:
                    result = 'green'
                    counter += 1
                    continue
        if flag == False:
            if counter <= green:
                result = 'green'
                counter +=1
            else:
                counter = 1
                flag = True
                if counter <= red:
                    result = 'red'
                    counter += 1
                    continue
    
    return result
