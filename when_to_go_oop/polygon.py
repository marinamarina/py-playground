import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        'find distance between two points'
        return math.sqrt((self.x-point.x)**2 + (self.y-point.y)**2)

class Polygon:
    def __init__(self, *points):
        self.vertices = points
        for point in points:
            self.vertices.append(point)

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]

        for i in range(len(points)-1):
            perimeter += points[i].distance(points[i+1])

        return perimeter

square1 = Polygon(Point(1,1), Point(1,2), Point(2,2), Point(2,1))

print "Perimeter %s" % square1.perimeter()