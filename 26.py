def BalancedParentheses(N):
    a = []
    n = 0
    while n <= N - 1:
        a.insert(-1, ')')
        a.insert(0, '(')
        n += 1
    b = []
    k = 0
    for i in range(N*2):
        if i % 2 == 0:
            new_element = ('(')
            b.append(new_element)
        if i % 2 != 0:
            new_element = (')')
            b.append(new_element)
    ta = ''.join(a)
    tb = ''.join(b)
    if ta == tb:
        d = ta
    else:
        d = ta + ' ' + tb
    return d
