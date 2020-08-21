def odometer(N):
    long = len(N)
    if long >= 2:
        num = 0
        sum_distance = 0
        distance_all = 0
        for index, number in enumerate(N):
            if index%2 == 0:
                speed = N[index]
            else:
                if num == 0:
                    time = N[index]
                    num=+1
                    distance = speed*time  
                else:
                    time_new = N[index] - time
                    time = N[index]
                    distance = speed*time_new
                sum_distance += distance
        distance_all += sum_distance
        return distance_all
    else:
        exit()
