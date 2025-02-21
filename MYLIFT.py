#this is the one where we are free to do whatever we want
#let's brainstorm

def my_lift_function(floors, capacity, requests, current_floor = 0, method = 0):
    if method == 0:
        time_intervals =[]
        tu = 0
        rel_values == [0 for x in range(floors)]
        lift_requests = [0 for x in range(floors)]
        while not requests == True:
            for x in range(floors):
                if x == current_floor or (sum(lift_requests) == capacity and lift_requests[x] == 0):
                    rel_values[x] = 0
                else:
                    rel_values[x] = lift_requests[x]*len(requests[x])/abs(x-current_floor)
            destination = rel_values.index(max(rel_values))
            tu += abs(destination-current_floor)
            while sum(lift_requests) < capacity:
                if lift_requests[x] != 0:
                    lift_requests[x] = 


            

    
"""
weights: number of people on the floor, the floor they want to go to, how far away the target floor is, capacity
weight of weights: 
- capacity is variable : check number of requests on a floor against available capacity, enter panic when capacity is full
- 
"""