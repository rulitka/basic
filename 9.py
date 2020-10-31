s = 'отдай мою кроличью лапку'
encode = True

def TheRabbitsFoot(s, encode):
    if encode == True:
        b = s.split()
        b = ''.join(b)
        length_b = len(b)
        square =  round(length_b ** .5)
        N = square
        M = square
        new_box = []
        for i in range(N):
            new_box.append([])
            for char in b[i * N: (i + 1) * N]:
                new_box[-1].append(char)
        my_string = ''
        for i in range(N):
            for j in range(M):
                my_string += new_box[j][i]
            my_string += ' '
        return my_string
TheRabbitsFoot(s, encode)
# Сначала я превращаю строку в матрицу:
[['о', 'т', 'д', 'а', 'й'], 
['м', 'о', 'ю', 'к', 'р'], 
['о', 'л', 'и', 'ч', 'ь'], 
['ю', 'л', 'а', 'п', 'к'], 
['у']]
# А потом создаю строку my_string в которую хочу добавить все элементы по столбцам.
У меня успешно создается 'омоюу толл', а потом выходит ошибка:
IndexError: list index out of range, потому что заканчиваются столбцы,
и я не знаю, что делать дальше.
