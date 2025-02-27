def scanning_algorithm(floors,capacity,requests, current_floor = 0, direction = 1):    
    """
    Imitates a lift that only switches directions at the top and bottom floors
    
    args:
    floors (int) - read from the text file to show the total number of floors
    capacity (int) - read from the text file and shows the total capacity of the lift
    requests (list) - read from the text file and is a 2d list that represents the requested floor given by each person on each floor
    current_floor (int = 0) - set to be as 0, this is the starting floor
    direction - set to be 1, a positive direction shows that the lift is moving upwards and negative is the opposite

    returns:
    time_intervals (list) - a list that records the number of people left in the lift. It is recorded every single time the doors on the lift would open.
    """
    done = False # The variable that checks to see if any requests are left on floors
    lift_requests = [0 for x in range(floors)]
    destination = 0
    time_intervals = []
    people_in_lift = 0

    for x in range(len(requests)): 
        # Data sanitisation
        if requests[x] == [None]:
            requests[x] = []

    while done == False or sum(lift_requests) != 0:
        
        people_left = 0
        for x in range(len(requests)):
            if requests[x] != [None]:
                people_left += len(requests[x])
        people_left += sum(lift_requests) # This sections gives an accurate representation of how many people are to be served

        time_intervals.append(people_left) # Recording the number of people left

        if lift_requests[destination] != 0:
            #Removes the people who have arrived at their floor
            people_in_lift -= lift_requests[destination]
        lift_requests[destination] = 0

        while people_in_lift < capacity and (len(requests[destination]) != 0 or lift_requests[destination] != 0):
            #This adds people to the lift if there is enough space
            if len(requests[destination]) != 0 and requests[destination] != [None]:
                lift_requests[requests[destination].pop()-1]  += 1
                #This line above means that each list within the 2d list acts like a stack as the latest requests are served first (last in first out system)
                people_in_lift += 1
        
        current_floor = destination

        # Movement
        if current_floor == floors-1:
            direction = -1
        elif current_floor == 0:
            direction = 1
        
        destination = current_floor + direction

        # The final checker which goes through the requests and sees if it's empty
        clear = False
        for x in range(len(requests)):
            if requests[x] == []:
                clear = True
            else:
                clear = False
                break
        if clear == True:
            done = True

    time_intervals.append(0)
    return time_intervals
                
        
