from Main import main, readfloors, readcapacity, readrequests


#the function deals with... it's in the name
def look_functionality(floors, capacity, requests):
    floors_to_go_to = []
    current_floor = 0
    current_capacity = 0
    #for this variable, if it set to 1, it is upwards, if it -1, it is downward, 0 is stationary
    #we start with direction of travel set to 1 on the assumption that the lift starts on the ground floor
    direction_of_travel = 1
    
    
    #iterate through the floors, at each one:
    # 1. drop off passangers
    # 2. check capacity
    # 3. check the direction people want to go in
    # 4. Add people if possible
    # 5. Check either if we've reached the top or if there are requests above

    #set a while loop that checks whether all requests have been cleared
    for values in requests:
        while all(x is not None for x in values):
            #iterate through the floors
            for floor in range(len(floors)):
                #check the list of floors passengers inside the elevator wish to go to
                for destination in floors_to_go_to:
                    #if one of them wants to go to the current floor, remove them
                    if floor == destination:
                        floors_to_go_to.remove(destination)
                #check all the requests on the current floor, making note of requests starting from 0 and floors starting from 1
                for current_floor in requests[current_floor]:
                    #check that they are heading in the direction the elevator is and there is room for them
                    #append them to floors to go to and remove them from requests, then increase current_capacity
                    if request > floor and direction_of_travel == 1 and current_capacity < 5:
                        floors_to_go_to.append(request)
                        requests.remove(request)
                        current_capacity += 1
                    elif request < i and direction_of_travel == -1 and current_capacity < 5:
                        floors_to_go_to.append(request)
                        requests.remove(request)
                        current_capacity += 1
                
                #now we check the floors above or below to see if there are more requests
                number_of_floors_left = len(floors) - floor
                #if there are no more requests in above or below floors:
                if all(floor in requests and floor in floors_to_go_to > number_of_floors_left and if direction_of_travel == 1 is None or floor in requests and floor in floors_to_go_to < number_of_floors_left if direction_of_travel == -1 is None):
                    #change the direction
                    direction_of_travel = -direction_of_travel
                    if direction_of_travel == -1:
                        current_floor -= 1
                    elif direction_of_travel == 1:
                        current_floor += 1
                    #stop the for loop iterating
                    break
                else:
                    if direction_of_travel == -1:
                        current_floor -= 1
                    elif direction_of_travel == 1:
                        current_floor += 1
                    continue

                #now we check if we're at the top or bottom floor
                if current_floor == 0 and a in requests and floors_to_go_to are not None:
                    direction_of_travel = 1
                elif current_floor == max(floors) and a in request and floors_to_go_to are not None:
                    direction of travel = -1
            
            
        
            



            
            
            



    

