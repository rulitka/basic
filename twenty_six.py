def recursion_one(N, a):
    if N == 0:
        return a
    else:
        a.append('()')
        return recursion_one(N - 1, a)

def recursion_two(N, b):
    if N == 0:
        return b
    else:
        b.insert(-1, ')')
        b.insert(0, '(')
        return recursion_two(N - 1, b)

def BalancedParentheses(N):
    a = []
    a = recursion_one(N, a)
    b = []
    b = recursion_two(N, b)
    tb = ''.join(b)
    if ta == tb:
        d = ta
    if ta != tb:
        d = ta + ' ' + tb
    return d
