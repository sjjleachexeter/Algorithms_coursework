from collections import deque

#the function deals with... it's in the name
def look_functionality(floor, capacity, requests):
    #create a queue that we will use to address requests of people in the lift
    floors_to_go_to = deque()
    current_floor = 0
    current_capacity = 0
    #here we define how we measure the algorith, in number of people left to serve and time units (check bottom of doc for specification on time units)
    def number_of_people_left_to_serve(): 
        people = sum(len([r for r in values if isinstance(r, int)]) for values in requests) + len(floors_to_go_to) 
        return people
    #we'll use the following function to check if floors above have values or not

    time_intervals = []
    tu = 0
    #for this variable, if it set to 1, it is upwards, if it -1, it is downward, 0 is stationary
    #we start with direction of travel set to 1 on the assumption that the lift starts on the ground floor
    direction_of_travel = 1

    for x in range(len(requests)): 
        # Data sanitisation
        if requests[x] == [None]:
            requests[x] = []
    
    #iterate through the floors, at each one:
    # 1. drop off passangers
    # 2. check capacity
    # 3. check the direction people want to go in
    # 4. Add people if possible
    # 5. Check either if we've reached the top or if there are requests above

    # Here we're going to clean up the input
    for i in range(len(requests)):
        if requests[i] is None:
            requests[i] = []


    #set a while loop that keeps on going until all requests in the elevator have been cleared
    while any(request not in ([], [None]) for request in requests) or floors_to_go_to: #all loop didn't work

        if len(time_intervals) > 2000:
            print("Safety break: possible infinite loop")
            break

        if current_floor + 1 in floors_to_go_to or len(requests[current_floor]) > 0:
        
            #first we want to remove all the people who want to get off at this floor
            #here we use the filter method to get rid of all values equal to the current floor and setting floors to go to equal to that queue
            floors_to_go_to = deque(person for person in floors_to_go_to if person != current_floor + 1)
            #now we want to adjust the capacity of the lift
            current_capacity = len(floors_to_go_to)


            #now we check the requests on the floor we have arrived at
            if 0 <= current_floor < len(requests) and requests[current_floor] and current_capacity < capacity:
                new_passengers = []
    
                for request in requests[current_floor][::-1]:  # Iterate over a reverse copy to avoid skipping and pop them off the end
                    if current_capacity < capacity:
                        new_passengers.append(request)
                        requests[current_floor].remove(request)
                        current_capacity += 1
    
                floors_to_go_to.extend(new_passengers)
                    


        
        
        #to decide how we want the lift to operate having finished with this floor, we need to know what direction if needs to go in
        if direction_of_travel == 1:
            #now we check if we're at the top
            if current_floor == len(requests) - 1:
                direction_of_travel = -1
            #if there are no more requests in above or below floors:
            elif not any(request for request in requests[current_floor:]) and not any(x>current_floor+1 for x in floors_to_go_to):
                #change the direction
                direction_of_travel = -1



        elif direction_of_travel == -1:
            #if there are no more requests in above or below floors:
            #now we check if we're at the bottom
            if current_floor == 0:
                direction_of_travel = 1
            #here I checked if there were no more requests below
            elif not any(request for request in requests[:current_floor]) and not any(x<current_floor+1 for x in floors_to_go_to):
                #change the direction
                direction_of_travel = 1

        if direction_of_travel == 1:
            current_floor += 1
        elif direction_of_travel == -1:
            current_floor -=1

        time_intervals.append(number_of_people_left_to_serve())



    return time_intervals
        


#time_intervals is an empty list I created at the top of LOOK, where I would like you to log the amount of time units (tu) that have passed and number of people
#time units: 1 time unit passes for interchange of people, 1 floor is 1 unit of time