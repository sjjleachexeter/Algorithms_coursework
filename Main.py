#Purpose of this module is to interact with the text file given on ELE
#Then we need 2 variables, number of floors and capacity
#Then we need to read the text file, which has the number of people and the destinations they want to go to
#N.B. we don't need to worry about differentiating between people outside the lift and inside
#Append that to a list/dictionary 

def readinputfile(file = "input1.txt"):
    # This function gives three pieces of data: the total number floors, the capacity of the lift and the requests of each floor.
    global floors, capactiy, requests
    with open(file,"r") as r: #Creates a pointer for the file
        files = r.readlines()
        floors = int(str(files[1])[:files[1].find(",")]) #adjustsable for floors above 9
        capacity = int(str(files[1])[files[1].find(" "):-1])
        requests = files[4:]
        for i in range(len(requests)):
            requests[i] = (str(requests[i])[str(requests[i]).find(":")+1:-1]).split(",") #Makes each line an index in the array
        for x in range(len(requests)):
            for y in range(len(requests[x])):
                try: # This will make each string value an integer unless it is blank, in which case it is given a None value
                    requests[x][y] = int(requests[x][y])
                except ValueError:
                    requests[x][y] = None

readinputfile()