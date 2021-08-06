import matplotlib.pyplot as plt
import numpy as np

var_plot = []
var_size = []
def threen(a , operation_count):
    if a==4:
        print("Success")
        xpoints = np.array(var_plot)
        ypoints = np.array(var_size)
        operation_count = operation_count + 2
        print("It took " + str(operation_count) + " operation to reach 4,2,1")

        plt.style.use('dark_background')
        plt.plot(ypoints,xpoints)
        plt.show()

    elif (a%2 == 0):
        a = a / 2
        operation_count = operation_count+1
        var_plot.append(a)
        var_size.append(operation_count)
        threen(a , operation_count)
    else:
        a = 3 * a + 1
        operation_count = operation_count + 1
        var_plot.append(a)
        var_size.append(operation_count)
        threen(a , operation_count)

threen(int(input("Enter a number to check 3n+1 validity: ")),0)
