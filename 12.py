def MassVote(N, Votes):
    mx = Votes[0]
    n = 0
    for i in range(len(Votes)):
        if Votes[i] > mx:
            mx = Votes[i]
    for i in range(len(Votes)):
        if mx == Votes[i]:
            n += 1
    summa_el = sum(Votes)
    precent = (mx/summa_el)*100
    precent_res = round(precent, 3)
    if precent_res > 50:
        index_el = Votes.index(mx)
        number_of_candidate = index_el + 1
        result = 'majority winner {}'.format(number_of_candidate)
    if precent_res <= 50:
        if n <= 1:
            index_el = Votes.index(mx)
            number_of_candidate = index_el + 1
            result = 'minority winner {}'.format(number_of_candidate)
        else:
            result = 'no winner'
    return result
