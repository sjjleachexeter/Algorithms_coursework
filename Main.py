#Purpose of this module is to interact with the text file given on ELE
#Then we need 2 variables, number of floors and capacity
#Then we need to read the text file, which has the number of people and the destinations they want to go to
#N.B. we don't need to worry about differentiating between people outside the lift and inside
#Append that to a list/dictionary 

def readinputfile(file = "input1.txt"):
    with open(file,"r") as r:
        file = r.readlines()
        print(file)

readinputfile()