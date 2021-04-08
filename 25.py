def S(A):
    B = []
    count = 0
    largest = 0
    for i in range(len(A) - 1):
        for j in range (len(A) - i - 1):
            k = i + j
            for j in range(k):
                if count == 0:
                    largest = A[i]
                if A[i] > largest:
                    largest = A[i]
        B.append(largest)   
    return B  

def TransformTransform(A, N):
    first_transform = S(A)
    second_transform = S(first_transform)
    sum_second = sum(second_transform)
    if (sum_second % 2) == 0:
        return True
    else:
        return False
