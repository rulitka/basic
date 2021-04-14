def S(A):
    B = []
    largest = 0 
    for i in range(len(A)):      
        for j in range (len(A) - i):
            k = i + j
            for z in range(j, k + 1):
                if z == j:
                    largest = A[j]
                else:
                    if A[z] > largest:
                        largest = A[z]
            if largest != 0:
                B.append(largest)
            else:
                pass
    return B 

def TransformTransform(A, N):
    first_transform = S(A)
    second_transform = S(first_transform)
    sum_second = sum(second_transform)
    if (sum_second % 2) == 0:
        return True
    else:
        return False
