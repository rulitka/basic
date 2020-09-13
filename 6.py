def PatternUnlock(N, hits):
    string_result = 0
    summ = 0
    sum_all =0
    for i in range(1, len(hits)):
        if (hits[i] - hits[i-1]) == 1:
            summ =+1
        else:
            summ =+1.41421356237
        sum_all +=summ
    string_rounding = float('{:.5f}'.format(sum_all))
    string_convert = str(string_rounding)
    string_no_point = string_convert.replace('.', '')
    string_result = ''
    old_with_null = '0'
    new_no_null = ''
    for i in string_no_point:
        if i == old_with_null:
            i = new_no_null
        string_result += i
    return string_result
