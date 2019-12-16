import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1 #x1 and y1
        self.coor2 = coor2 #x2 and y2
    
    #Uses distance formula to calculate distance
    def distance(self):
        part1 = (self.coor2[0] - self.coor1[0]) ** 2 #(x2 - x1)^2
        part2 = (self.coor2[1] - self.coor1[1]) ** 2 #(y2 - y1)^2
        return math.sqrt(part1 + part2)

    #Uses slope formula to calculate slope
    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]) 

# EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print('The distance is {}'.format(li.distance()))
print('The slope is {}'.format(li.slope()))
