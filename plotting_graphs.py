import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker as ticker

'''
this is external code that is run after running main from our example code. it uses the data from data.txt 
it creates 3 line graphs that track the effectiveness of each graph
'''
colors = ["red","green","blue"] #MYLIFT is always in red, LOOK is always in green and SCAN in blue
with open("data.txt","r") as r:
    file = r.readlines()

    for i in range(3):
        x_values = []
        y_values = []
        data = eval(file[1+i*4])
        for t in range(len(data)):
            y_values.append(int(data[t]))
            x_values.append(t)
        plt.plot(x_values, y_values,label = str(file[i*4])[:-1]+" 1", color = colors[i], alpha = 0.5) #Reads the top of the file for each name of the algorithm

    plt.legend() #formatting of the first graph
    plt.title("Input1.txt results")
    plt.xlabel("Floors visited")
    plt.ylabel("Number of people left")
    plt.xticks(np.arange(0, 21, 1)) 
    plt.yticks(np.arange(0, 6, 1)) 
    plt.show()

    # The sections above repeat twice more as the formatting is unique for each line chart

    for j in range(3):
        x_values = []
        y_values = []
        data = eval(file[2+j*4])
        for t in range(len(data)):
            y_values.append(int(data[t]))
            x_values.append(t)
        plt.plot(x_values, y_values,label = str(file[j*4])[:-1]+" 2", color = colors[j], alpha = 0.5)

    plt.legend()
    plt.title("Input2.txt results")
    plt.xlabel("Floors visited")
    plt.ylabel("Number of people left")
    plt.xticks(np.arange(0, 41, 2)) 
    plt.yticks(np.arange(0, 16, 1)) 
    plt.show()

    for k in range(3):
        x_values = []
        y_values = []
        data = eval(file[3+k*4])
        for t in range(len(data)):
            y_values.append(int(data[t]))
            x_values.append(t)
        plt.plot(x_values, y_values,label = str(file[k*4])[:-1]+" 3", color = colors[k], alpha = 0.5)

    plt.legend()
    plt.title("Input3.txt results")
    plt.xlabel("Floors visited")
    plt.ylabel("Number of people left")
    plt.xticks(np.arange(0, 351, 50)) 
    plt.yticks(np.arange(0, 121, 10)) 
    plt.show()

