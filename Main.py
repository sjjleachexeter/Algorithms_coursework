from SCANS import scanning_algorithm as s
from LOOK import look_functionality as l
from MYLIFT import my_lift_function as m

def fileread(file = "input3.txt") -> None:
    """ 
    This function reads a text file and calls three other functions to pull data from it.
    
    args:
    file (txt file) -  a text file that is set to one of our example input files

    returns:
    floors (int) - the total number of floors
    capacity (int) - the capacity of the lift
    requests (list) - 2d list containing each request by each person per floor
    """
    with open(file,"r") as r: #Creates a pointer for the file
        files = r.readlines()
        floors = readfloors(files)
        capacity = readcapacity(files)
        requests = readrequests(files)
    return floors,capacity, requests

def main(algorithm = "SCAN"):
    """
    chooses which algorithm is being used for the lift

    args:
    algorithm (str) - one of "SCAN","LOOK" or "MYLIFT" and the appropriate algorithm is used

    returns:
    time_values (list) - a 2d list where every index has two elements: the number of people remaining and the number of time units that have passed
    """
    floor, capacity, requests = fileread()
    if algorithm == "SCAN":
        time_values = s(floor,capacity,requests)
    elif algorithm == "LOOK":
        time_values = l(floor,capacity,requests)
    elif algorithm == "MYLIFT":
        time_values = m(floor,capacity,requests)
    return time_values
        


    

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
    with open("data.txt","a") as a:
        a.write(str(main())+"\n") #Appending to our data to be used by plotting graphs
