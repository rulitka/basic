def to_start(tree):
    new_matrix = []
    for i in range(len(tree)):
        new_matrix.append(list(tree[i]))
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[i])):
                if new_matrix[i][j] == '+':
                    new_matrix[i][j] = 0
                if new_matrix[i][j] == '.':
                    new_matrix[i][j] = -1
    return  new_matrix

def add_branches(new_matrix):
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] += 1
    return  new_matrix

def delete_branches(new_matrix, H, W):
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
                if new_matrix[i][j] >= 3:
                    new_matrix[i][j] = 0
                    if i == 0 and j == 0:
                        new_matrix[i][j + 1] = 0
                        new_matrix[i + 1][j] = 0
                    elif i == 0 and j < W - 1:
                        new_matrix[i][j + 1] = 0
                        new_matrix[i][j - 1] = 0
                        new_matrix[i + 1][j] = 0
                    elif i == 0 and j == W - 1:
                        new_matrix[i][j - 1] = 0
                        new_matrix[i + 1][j] = 0
                    elif i < H - 1 and j == 0:
                        new_matrix[i][j + 1] = 0
                        new_matrix[i + 1][j] = 0
                        new_matrix[i - 1][j] = 0
                    elif i == H - 1 and j == 0:
                        new_matrix[i][j + 1] = 0
                        new_matrix[i - 1][j] = 0
                    elif i == H - 1 and j != W - 1:
                        new_matrix[i][j - 1] = 0
                        new_matrix[i ][j + 1] = 0
                        new_matrix[i - 1][j] = 0
                    elif i != H - 1 and j == W - 1:
                        new_matrix[i + 1][j] = 0
                        new_matrix[i][j - 1] = 0
                        new_matrix[i - 1][j] = 0
                    elif i == H - 1 and j == W - 1:
                        new_matrix[i][j - 1] = 0
                        new_matrix[i - 1][j] = 0
                    else:
                        new_matrix[i][j + 1] = 0
                        new_matrix[i][j - 1] = 0
                        new_matrix[i + 1][j] = 0
                        new_matrix[i - 1][j] = 0
    return new_matrix

def convert_to_symbol(H, W, new_matrix):
    pre_result = [[0]*W for i in range (H)]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            if new_matrix[i][j] > 0:
                pre_result[i][j] = '+'
            if new_matrix[i][j] == 0:
                pre_result[i][j] = '.'
    return pre_result

def convert_to_string(pre_result):
    result = []
    for elem in range(len(pre_result)):
        result.append(''.join(pre_result[elem]))
    return result

def TreeOfLife(H, W, N, tree):
    result = []
    new_matrix = to_start(tree)
    years = 1
    while years < N:
        if years % 2 == 0:
            new_matrix = add_branches(new_matrix)
            pre_result = convert_to_symbol(H, W, new_matrix)
            post_result = convert_to_string(pre_result)
            result.append(post_result)
            years += 1
        if years % 2 != 0:
            new_matrix = add_branches(new_matrix)
            new_matrix = delete_branches(new_matrix, H, W)
            pre_result = convert_to_symbol(H, W, new_matrix)
            post_result = convert_to_string(pre_result)
            result.append(post_result)
            years += 1
    if years == N:
        if years % 2 == 0:
            new_matrix = add_branches(new_matrix)
            pre_result = convert_to_symbol(H, W, new_matrix)
            post_result = convert_to_string(pre_result)
            result.append(post_result)
        if years % 2 != 0:
            new_matrix = add_branches(new_matrix)
            new_matrix = delete_branches(new_matrix, H, W)
            pre_result = convert_to_symbol(H, W, new_matrix)
            post_result = convert_to_string(pre_result)
            result.append(post_result)  
    return result
