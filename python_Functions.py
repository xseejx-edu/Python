import math

def calculateArea(type):
    if type == "circle":
        ray = int(input("Insert ray length >  "))
        return ray**2*math.pi
    if type == "rectangle":
        base = int(input("Insert Base length >  "))
        height = int(input("Insert Height length >  "))
        return base*height        
    if type == "square":
        line = int(input("Insert Line length >  "))
        return line**4



if __name__ == "__main__":
    print(calculateArea(str(input("Insert a Type of shape [Circle, Rectangle, Square] >  ")).lower()))