import math


class Circle(object):
    ' An advance circle analytic tool kit'

    version = '1.0'

    def __init__(self, radius):
        self.radius = radius

    @property                         #gives dotted access to method calls
    def radius(self):
        'Radius of a circle'
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter  = radius * 2.0

    def area(self):
        return math.pi * self.radius ** 2.0

    def perimeter(self):
        return self.radius * math.pi * 2.0

    @classmethod                        # alternative constructor
    def from_bbd(cls, bbd):
        'construct a circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return Circle(radius)

    @staticmethod                       # Attach function to class
    def angle_to_grade(angle):
        'convert angle in degree to percentage grade'
        return math.tan(math.radians(angle)) * 100.0


class Tyre(Circle):

    def perimeter(self):
        print('hi')
        return Circle.perimeter(self) * 1.25

