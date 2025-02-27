#this is the one where we are free to do whatever we want
#let's brainstorm

def my_lift_function(floors, capacity, requests, current_floor = 0) -> list:
    """
    Enacts a custom function that prioritises floors based off a relative value assigned after each movement
    
    args:
    floors (int) - read from the text file to show the total number of floors
    capacity (int) - read from the text file and shows the total capacity of the lift
    requests (list) - read from the text file and is a 2d list that represents the requested floor given by each person on each floor
    current_floor (int = 0) - set to be as 0, this is the starting floor

    returns:
    time_values (list) - a 2d list where every index has two elements: the number of people remaining and the number of time units that have passed
    """
    time_intervals =[]
    rel_values = [0 for x in range(floors)]
    lift_requests = [0 for x in range(floors)]
    people_in_lift = 0
    destination = 0
    done = False

    for x in range(len(requests)):
        if requests[x] == [None]:
            requests[x] = []

    while done == False or sum(lift_requests) != 0:
        
        people_left = 0 
        #People_left counter which adds the number of reqeuests on floors and in the lift
        for x in range(len(requests)):
            people_left += len(requests[x])
        people_left += sum(lift_requests)
    

        time_intervals.append(people_left) #This is the counter that counts the number of people left, it is tracking the number of people left everytime the lift doors open

        if lift_requests[destination] != 0:
            #Removing the current people from the lift if this is their destination
            people_in_lift -= lift_requests[destination]
        lift_requests[destination] = 0

        while people_in_lift < capacity and (len(requests[destination]) != 0 or lift_requests[destination]!= 0): #Checks if there is space in the lift and if there is, if anyone wants to get on
            #Adding people to the lift and putting their requests into lift_requests
            if len(requests[destination]) != 0:
                lift_requests[requests[destination].pop()-1]  += 1
                people_in_lift += 1

        current_floor = destination #changing the floor they've just arrived at to the current floor

        for x in range(floors):
            #Creating a relative value for every floor
            if x == current_floor or (sum(lift_requests) == capacity and lift_requests[x] == 0):
                #As we need to get onto a different floor, the current floor is set to 0
                #The second statement checks to see if there is no room on the lift, as if there isn't then the lift will only go to floors with requests
                rel_values[x] = 0

            else:
                rel_values[x] = (lift_requests[x]+len(requests[x]))/abs(x-current_floor)*capacity

        destination = rel_values.index(max(rel_values)) #The next destination is then chosen as the highest of the values.

            
        clear = False
        for x in range(len(requests)):
            #A final check to see if there are any more requests outside the lift
            if requests[x] == []:
                clear = True
            else:
                clear = False
                break
        if clear == True:
            done = True

    time_intervals.append(0)
    return time_intervals
                
