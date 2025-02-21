#this is the one where we are free to do whatever we want
#let's brainstorm

def my_lift_function(floors, capacity, requests, current_floor = 0, method = 0):
    if method == 0:
        time_intervals =[]
        tu = 0
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
            for x in range(len(requests)):
                if requests[x] != [None]:
                    people_left += len(requests[x])
            people_left += sum(lift_requests)
            time_intervals.append([people_left,tu])
            print(people_left,tu)


            print(requests)
            while people_in_lift < capacity and len(requests[destination]) != 0 and requests[destination] != [None]:
                if lift_requests[destination] != 0:
                    people_in_lift -= lift_requests[destination]
                    lift_requests[destination] = 0
                if len(requests[destination]) != 0 and requests[destination] != [None]:
                    lift_requests[requests[destination].pop()-1]  += 1
                    people_in_lift += 1
            tu += 1
            print(requests,lift_requests)

            destination = current_floor
            for x in range(floors):
                if x == current_floor or (sum(lift_requests) == capacity and lift_requests[x] == 0):
                    rel_values[x] = 0
                else:
                    rel_values[x] = (lift_requests[x]+len(requests[x]))/abs(x-current_floor)*capacity


            destination = rel_values.index(max(rel_values))
            print(rel_values)
            tu += abs(destination-current_floor)
            
            clear = False
            for x in range(len(requests)):
                if requests[x] == [] or requests[x] == [None]:
                    clear = True
                else:
                    clear = False
                    break
            if clear == True:
                done = True
    return time_intervals
                



    
"""
weights: number of people on the floor, the floor they want to go to, how far away the target floor is, capacity
weight of weights: 
- capacity is variable : check number of requests on a floor against available capacity, enter panic when capacity is full
- 
"""