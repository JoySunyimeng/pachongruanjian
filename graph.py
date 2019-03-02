
from point import Point
import math
class Triangle():
    def __init__(self,p1,p2,p3):
        self.A = p1
        self.B = p2
        self.C = p3
        
        self.a = p1.distance(p2)
        self.b = p2.distance(p3)
        self.c = p3.distance(p1)
    def __str__(self):
        return "Point:(%s,%s,%s)\nBorder:(%f,%f,%f)"%(self.A, self.B,self.C,self.a, self.b,self.c) 
    def area(self):
        s = (self.a + self.b + self.c)/2
        area = math.sqrt(s*((s-self.a)*(s-self.b)*(s-self.c)))
        return area
    def perimeter(self):
        return self.a + self.b + self.c
    def toPoints(self):
        return [self.A.getXY(),self.B.getXY(),self.C.getXY(),self.A.getXY()]
 
 
class Rectangle():
    def __init__(self,center,breadth,length):
        self.center = center
        self.breadth = breadth
        self.length = length
    def __str__(self):
        return "Center:(%s)\nBorder:(%f,%f)"%(self.center, self.breadth,self.length) 
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def toPoints(self):
        return [(self.center.X-self.breadth/2,self.center.Y - self.length),(self.center.X-self.breadth/2,self.center.Y + self.length),
               (self.center.X+self.breadth/2,self.center.Y + self.length),(self.center.X+self.breadth/2,self.center.Y - self.length),(self.center.X-self.breadth/2,self.center.Y - self.length)]

class Circle():
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
    def __str__(self):
        return "Center:(%s)\radius:(%f)"%(self.center,self.radius)
    def area(self):
        return math.pi * self.radius ** 2
 
    def perimeter(self):
        return 2 * math.pi * self.radius