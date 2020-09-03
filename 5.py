def SynchronizingTables(N, ids, salary):
    ids_2 = sorted(ids)
    salary_2 = sorted(salary)
    x = list(zip(ids_2,salary_2))
    lst_new = []
    for item in range(N):
        for i in range(N):
            if ids[item] == x[i][0]:
                lst_new.append(x[i][1])
    return lst_new
