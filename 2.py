def odometer(N):
    long = len(N)
    if long >= 2:
        sum_distance = 0
        distance_all = 0
        for index, number in enumerate(N):
            if index%2 == 0:
                speed = N[index]
            else:
                time = N[index]
                if N[index] == N[-1]:
                    print (N[-1])
                    print (N[-3])
                    time = N[-1] - N[-3]
                distance = speed*time
                sum_distance += distance
        distance_all += sum_distance
        return distance_all
    else:
        print ("Exit")
