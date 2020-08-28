def MadMax(N, Tele):
    Tele_new = random.sample(Tele, k=N)
    lst_new = []
    lst_curr = []
    Tele_new.sort()
    center = int(len(Tele_new)/2)
    max_element = max(Tele_new)
    max_idx = Tele_new.index(max_element)
    Tele_new[max_idx], Tele_new[center] = Tele_new[center], Tele_new[max_idx]
    for i in range(len(Tele_new)):
        if i <= center:
            lst_new.append(Tele_new[i])
        if i > center:
            lst_curr.append(Tele_new[i])
    lst_curr.sort(reverse=1)
    joinedList = [*lst_new, *lst_curr]
    return joinedList
