def string_to_matrix(Matrix):
    result = []
    for s in Matrix:
        my_string = " ".join(s)
        my_list = my_string.split()
        new_list = [int(x) for x in my_list]
        result.append(new_list)
    return result


def rotateMatrix(mat):
    top = 0
    bottom = len(mat)-1

    left = 0
    right = len(mat[0])-1

    while left < right and top < bottom:

        prev = mat[top+1][left]


        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1


        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1


        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1


        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat

def convert_to_string(pre_result, M, N):
    result = []
    new_matrix = [[0]*N for i in range (M)]
    for i in range(len(pre_result)):
        for j in range(len(pre_result[i])):
            new_matrix[i][j] = str(pre_result[i][j])
    for elem in range(len(new_matrix)):
        result.append(''.join(new_matrix[elem]))
    return result

def MatrixTurn(Matrix, M, N, T):
    mat = string_to_matrix(Matrix)
    n = 0
    while  n <= T - 1:
        pre_result = rotateMatrix(mat)
        n += 1
        result = convert_to_string(pre_result, M, N)
    return result
