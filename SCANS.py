def scanning_algorithm(floors,capacity,requests, current_floor = 0, direction = 1):
    done = False
    lift_requests = [0 for x in range(floors)]
    destination = 0
    time_intervals = []
    people_in_lift = 0

    for x in range(len(requests)):
        if requests[x] == [None]:
            requests[x] = []

    while done == False or sum(lift_requests) != 0:

        people_left = 0
        for x in range(len(requests)):
            if requests[x] != [None]:
                people_left += len(requests[x])
        people_left += sum(lift_requests)

        time_intervals.append(people_left)

        if lift_requests[destination] != 0:
            people_in_lift -= lift_requests[destination]
        lift_requests[destination] = 0

        while people_in_lift < capacity and (len(requests[destination]) != 0 or lift_requests[destination] != 0):
            if len(requests[destination]) != 0 and requests[destination] != [None]:
                lift_requests[requests[destination].pop()-1]  += 1
                people_in_lift += 1
        
        print(current_floor)
        current_floor = destination

        if current_floor == floors-1:
            direction = -1
        elif current_floor == 0:
            direction = 1
        
        destination = current_floor + direction

        clear = False
        for x in range(len(requests)):
            if requests[x] == [] or requests[x] == [None]:
                clear = True
            else:
                clear = False
                break
        if clear == True:
            done = True

    time_intervals.append(0)
    return time_intervals
                
        
