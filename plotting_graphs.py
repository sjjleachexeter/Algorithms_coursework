import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker as ticker

colors = ["red","green","blue"]
with open("data.txt","r") as r:
    file = r.readlines()
    for i in range(3):
        x_values = []
        y_values = []
        data = eval(file[1+i*4])
        for t in range(len(data)):
            y_values.append(int(data[t]))
            x_values.append(t)
        plt.plot(x_values, y_values,label = str(file[i*4])[:-1]+" 1", color = colors[i])

    plt.legend()
    plt.title("Input1.txt results")
    plt.xlabel("Floors visited")
    plt.ylabel("Number of people left")
    plt.xticks(np.arange(0, 21, 1)) 
    plt.yticks(np.arange(0, 6, 1)) 
    plt.show()
    for j in range(3):
        x_values = []
        y_values = []
        data = eval(file[2+j*4])
        for t in range(len(data)):
            y_values.append(int(data[t]))
            x_values.append(t)
        plt.plot(x_values, y_values,label = str(file[j*4])[:-1]+" 2", color = colors[j])

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
        plt.plot(x_values, y_values,label = str(file[k*4])[:-1]+" 3", color = colors[k])

    plt.legend()
    plt.title("Input3.txt results")
    plt.xlabel("Floors visited")
    plt.ylabel("Number of people left")
    plt.xticks(np.arange(0, 351, 50)) 
    plt.yticks(np.arange(0, 121, 10)) 
    plt.show()

