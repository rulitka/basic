def MaximumDiscount(N, price):
    price.sort(reverse=True)
    if N < 3:
        max_discount = 0
    if N >= 3:
        new_massive = create_matrix(N, price)
        max_discount = get_max_discount(new_massive)
    return max_discount


def get_max_discount(new_massive):
    max_discount = 0
    for i in range(len(new_massive)):
        for j in range(len(new_massive[i])):
            if j == 2:
                max_discount += new_massive[i][j]
            else:
                continue
    return max_discount


def create_matrix(N, price):
    H = 3 
    W = (int(N / H) + (N % H > 0)) 
    result_S = []
    result_S = [0] * W
    a = 0
    j = 0
    n_elem = 0
    for i in range(W):
        result_S[i] = [0] * H
    
    for i in range(len(price)):
        if n_elem < 3:
            result_S[a][j] = int(price[i])
            j += 1
            n_elem += 1
        if n_elem == 3:
                a += 1
                j = 0
                n_elem = 0
    return result_S
