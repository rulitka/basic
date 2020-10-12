def SumofThe(N, data):
    d = N -1
    list1a=data[:d]
    list1b=data[d:]
    summa = sum(list1a)
    if summa == list1b[0]:
        return summa
    else:
        shift(data)


def shift(data):
    data[0:1] = [data.pop(),data[0]]
    SumofThe(N, data)
