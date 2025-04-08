import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import csv


# Read data from CSV
def readData(file_path):
    y = []
    x = []
    with open(file=file_path, mode='r') as file:        
        reader = csv.reader(file)
        next(reader)   # Go to next line
        for row in reader:
            x.append(row[0])   # Get first colum of csv
            y.append(int(row[1]))    # Get second colum of csv REMEMBER TO CAST FROM STRING TO THE DESIRE VALUE
    return x, y        
    



# Make Graph
def makeGraph(xlist=[], ylist=[], title="Matplotlib Graph", xL="X Label", yL="Y Label"):
    plt.figure(figsize=(10, 7.5))
    #           X,  Y
    plt.plot(xlist, ylist, marker="o")
    plt.title(title)
    plt.xlabel(xL)
    plt.ylabel(yL)
    plt.axis([0, 10, 500, 1000])
    plt.xticks(rotation=45)  # Sets the rotation of the X label values
    #plt.ylim(600, 1000)
    ax = plt.gca()  # Get the current axes
    ax.yaxis.set_major_locator(MultipleLocator(50))  # Sets a spacing of 50 between y-axis ticks
    
    for i in range(len(xlist)):
        #           X       Y           TEXT
        plt.text(xlist[i], ylist[i], f'{xlist[i]}:{ylist[i]}', fontsize=9, ha='center', va='bottom')
    
    plt.show()  # Show the window


if __name__ == "__main__":   

    x, y = readData("Graphs/points.csv")
    makeGraph(x, y, "Footballers", "Names", "Goals")
    