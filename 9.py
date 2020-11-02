def TheRabbitsFoot(s, encode):
    if encode == True:
        b = s.split()
        b = ''.join(b)
        length_b = len(b)
        square =  round(length_b ** .5)
        sq_2 = square*square
        if sq_2 < length_b:
            N = square
            M = square+1    
            sq_new = N*M
            for elem in b:
                if sq_new > len(b):
                    out = '0'
                    b = b + out
                else:
                    break
        if sq_2 >= len(b):
            N = square
            M = square
            sq_new = N*M
            for elem in b:
                if sq_new > len(b):
                    out = '0'
                    b = b + out
                else:
                    break
        new_box = [[0]*N for _ in range(M)]
        n = 0
        for i in range(N):
            for j in range(M):
                new_box[i][j] = b[n]
                n += 1
        my_string = ''
        for i in range(N):
            for j in range(M):
                my_string += new_box[j][i]
            my_string += ' '
        result = my_string.replace("0", '')
        return result

    if encode == False:
        b = s.split()
        lenght_first = len(b[0])
        for i in range(len(b)):
            lenght_0 = len(b[0])
            lenght_i = len(b[i])
            if lenght_0 > lenght_i:
                b[i] = b[i] + '0'
            if lenght_0 == lenght_i:
                continue
        my_string = ''
        for i in range(len(b)):
            for j in range(len(b[i])):
                my_string += b[j][i]
            my_string += ' '
        my_1 = my_string.replace("0", '')
        result = my_1.replace(" ", '')
        return result
