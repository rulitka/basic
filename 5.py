def SynchronizingTables(N, ids, salary):
    if len(ids) == len(salary) == N:
        ids_2 = sorted(ids)
        salary_2 = sorted(salary)
        x = zip(ids_2,salary_2)
        xs = sorted(x, key=lambda tup: tup[0])
        lst_new = []
        for item in range(len(ids)):
            for i in range(len(xs)):
                for j in range(len(xs[i])):
                    if ids[item] == xs[i][j]:
                        lst_new.append(xs[i][j+1])
        return lst_new
