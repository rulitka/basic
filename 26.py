def combinations(N, left, right, toClose, str=""):
    if toClose < 0 or toClose > N or left < 0 or right < 0:
        return

    if left + right < 1:
        combs.append(str)
        return

    for s in ['(', ')']:
        str += s
        if s == '(':
            combinations(N, left - 1, right, toClose + 1, str)
        else:
            combinations(N, left, right - 1, toClose - 1, str)
        str = str[:-1]
    return


def BalancedParentheses(N):
    global combs
    combs = []
    combinations(N, left = N, right = N, toClose = 0, str="")
    result = ' '.join(combs)
    return result
