
#the function deals with... it's in the name
def look_functionality(floors, capacity, requests):
    floors_to_go_to = []
    current_floor = 0
    current_capacity = 0
    time_intervals = []
    tu = 0
    #for this variable, if it set to 1, it is upwards, if it -1, it is downward, 0 is stationary
    #we start with direction of travel set to 1 on the assumption that the lift starts on the ground floor
    direction_of_travel = 1
    
    
    #iterate through the floors, at each one:
    # 1. drop off passangers
    # 2. check capacity
    # 3. check the direction people want to go in
    # 4. Add people if possible
    # 5. Check either if we've reached the top or if there are requests above

    #set a while loop that keeps on going until all requests in and out of the elevator have been cleared
    for values in requests:
        for more_values inn values:
            for destinations in floors_to_go_to: #to fix
            
                while all(values and destinations != None):

                    while direction_of_travel == 1:
                        #iterate through the floors
                        for current_floor in requests:
                            #check the list of floors passengers inside the elevator wish to go to
                            for destination in floors_to_go_to:
                                #if one of them wants to go to the current floor, remove them
                                if current_floor == destination:
                                    floors_to_go_to.remove(destination)

                            #now we check the requests on the floor we have arrived at
                            for request in requests[current_floor]:
                                #check that they are heading in the direction the elevator is and there is room for them
                                #append them to floors to go to and remove them from requests, then increase current_capacity
                                if request > current_floor and current_capacity < 5:
                                    floors_to_go_to.append(request)
                                    requests[current_floor].remove(request)
                                    current_capacity += 1
                        
                        
                            #if there are no more requests in above or below floors:
                            if all(i is None for i in requests[current_floor][0:]) and all(x is None for x in floors_to_go_to if x < current_floor):
                                #change the direction
                                current_floor -= 1
                                direction_of_travel = -1
                                break

                            #now we check if we're at the top
                            if current_floor == len(requests):
                                current_floor -= 1
                                direction_of_travel = -1
                                break
                            
                            #having checked we're not at the top floor, and there are more requests are above us, we can go to the next floor
                            current_floor += 1

                    while direction_of_travel == -1:
                        for current_floor in requests:
                            #check the list of floors passengers inside the elevator wish to go to
                            for destination in floors_to_go_to:
                                #if one of them wants to go to the current floor, remove them
                                if current_floor == destination:
                                    floors_to_go_to.remove(destination)

                            #now we check the requests on the floor we have arrived at
                            for request in requests[current_floor]:
                                #check that they are heading in the direction the elevator is and there is room for them
                                #append them to floors to go to and remove them from requests, then increase current_capacity
                                if request < current_floor and current_capacity < 5:
                                    floors_to_go_to.append(request)
                                    requests[current_floor].remove(request)
                                    current_capacity += 1

                            #if there are no more requests in above or below floors:
                            if all(i is None for i in requests[current_floor][:0]) and all(x is None for x in floors_to_go_to if x < current_floor):
                                #change the direction
                                direction_of_travel = 1
                                break

                            #now we check if we're at the bottom
                            if current_floor == 0:
                                direction_of_travel = 1
                                break
                            
                            #having checked we're not at the top floor, and there are more requests are above us, we can go to the next floor
                            current_floor -= 1
                        

                    
                

#time_intervals is an empty array I created at the top of LOOK, where I would like you to log the amount of time units (tu) that have passed
#



        

