# creating program to find y corrdinate of point on a line
def point_finder(p1, p2, x):
    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
    y = slope*(x-p2[0]) + p2[1]
    return y

#additional work
def point_check(p1, p2, p3):
    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
    y = slope*(p3[0]-p2[0]) + p2[1]
    if y == p3[1]:
        return True
    else:
        return False
