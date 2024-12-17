class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * self.width * self.height

class Circle(Shape):
     def __init__(self, radius):
         self.radius = radius
     def area(self):
         return self.radius * self.radius * 3.14
     def circumference(self):
         return 2 * self.radius * 3.14

class Lozenge(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
    def circumference(self):
        return 4 * self.length

class Triangle(Shape):
    def __init__(self,bottom,height):
        self.bottom = bottom
        self.height = height
    def area(self):
        return 0.5 * self.bottom * self.height
    # def circumference(self):

a1 = Rectangle(12,32)
print(a1.area())
print(a1.circumference())

b1 = Lozenge(12)
print(b1.area())
print(b1.circumference())

c1 = Circle(1)
print(c1.area())
print(c1.circumference())

d1 = Triangle(12,32)
print(d1.area())


