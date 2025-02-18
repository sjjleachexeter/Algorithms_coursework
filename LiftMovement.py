#we need the lift to know what direction it is going in
#so we will define a function which deals with this

#we need to define how the lift recognises what floor it's on first
def direction_of_travel(current_floor, destination):
    if current_floor < destination:
        direction_of_travel = 1
    elif current_floor > destination:
        direction_of_travel = -1
    else:
        direction_of_travel = 0
    return direction_of_travel