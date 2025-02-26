import numpy as np
from matplotlib import pyplot as plt

with open("data.txt","r") as r:
    file = r.readlines()
    for i in range(3):
        x_values = []
        y_values = []
        data = eval(file[1+i])
        for t in range(len(data)):
            x_values.append(int(data[t][1]))
            y_values.append(int(data[t][0]))
        plt.plot(x_values, y_values, label = "MYLIFT"+str(t))

    plt.legend()
    plt.show()
