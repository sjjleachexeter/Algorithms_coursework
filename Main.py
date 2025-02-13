#Purpose of this module is to interact with the text file given on ELE
#Then we need 2 variables, number of floors and capacity
#Then we need to read the text file, which has the number of people and the destinations they want to go to
#N.B. we don't need to worry about differentiating between people outside the lift and inside
#Append that to a list/dictionary 

from LiftMovement import direction_of_travel

def main(file = "input1.txt") -> None:
    """ This function gives three pieces of data: the total number floors, the capacity of the lift and the requests of each floor."""
    with open(file,"r") as r: #Creates a pointer for the file
        files = r.readlines()
        floors = readfloors(files)
        capacity = readcapacity(files)
        requests = readrequests(files)
    return floors,capacity, requests
    

def readfloors(file) -> int:
    """
    reads file to find number of total floors
    
    args:
    file (list) - that has been read from a text file and has now been converted to a list

    returns:
    floors (int) - the total number of floors
    """
    floors = int(str(file[1])[:file[1].find(",")])
    return floors

def readcapacity(file) -> int:
    """
    reads file to find the capacity of the lift
    
    args:
    file (list) - that has been read from a text file and has now been converted to a list

    returns:
    capacity (int) - the total number of people who can fit inside the lift at one time
    """
    capacity = int(str(file[1])[file[1].find(" "):-1]) 
    return capacity
    
def readrequests(file) -> list:
    """
    reads file and sanitises requests from each floor
    
    args:
    file (list) - that has been read from a text file and has now been converted to a list

    returns:
    requests (list) - the requests for each floor where the floor is denoted by the index. The element of the list will show none if there are no requests
    """
    requests = file[4:]
    for i in range(len(requests)):
        requests[i] = (str(requests[i])[str(requests[i]).find(":")+1:-1]).split(",") #Makes each line an index in the array
    for x in range(len(requests)):
        for y in range(len(requests[x])):
            try: # This will make each string value an integer unless it is blank, in which case it is given a None value
                requests[x][y] = int(requests[x][y])
            except ValueError:
                requests[x][y] = None
    return requests

    

if __name__ == '__main__':
    print(main())
