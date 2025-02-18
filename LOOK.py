from Main import main, readfloors, readcapacity, readrequests 
from LiftMovement import direction_of_travel


#the function deals with... it's in the name
def look_functionality(floors, capacity, requests):
    floors = floors - 1
    floors_to_go_to = []
    current_floor = 0
    #check if there are any requests for floors
    for y in floors:
        if requests[current_floor] == None
            current_floor += 1
        else:
            for x in requests[current_floor]:
                if x > current_floor:
                    capacity += 1
                    floors_to_go_to

    

