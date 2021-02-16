#creating program to find y corrdinate of point on a line
def point_finder((a, b), (c, d), x):
    slope = (d-b)/(c-a)
    y = slope*(x-c) + d
    return y