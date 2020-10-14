def SumOfThe(N, data):
    for i in data:
        print (i)
        theSum = 0
        count = 0
        for j in data:
            if i == j:
                if count == 0:
                    count += 1
                    continue
                if count >= 1:
                    theSum = theSum + j  
            else:
                theSum = theSum + j
        if theSum == i:
            return theSum
