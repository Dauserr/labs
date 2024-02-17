import math
def polygon(sides, length):
    gradus = (2*math.pi)/(sides*2)
    a = (1/math.tan(gradus))*(length/2)
    area = (sides*length)*a/2
    return area

print(polygon(int(input("number of sides: ")), int(input("length of the side: "))))
