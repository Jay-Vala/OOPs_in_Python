#Create a circle class and add properties for its area and perimeter

class Circle():

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return (3.14 * (self.radius ** 2))

    @property
    def perimeter(self):
        return (2 * 3.14 * self.radius)
    

circle1 = Circle(5)
print(circle1.radius)
print(circle1.area)
print(circle1.perimeter)

circle1.radius = 7
print(circle1.radius)
print(circle1.area)
print(circle1.perimeter)