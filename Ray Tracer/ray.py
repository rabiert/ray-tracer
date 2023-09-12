from config import *

class Ray:
    def __init__(self, origin = Point(0, 0, 0), direction = Vector(0, 0, 0)):
        self.origin = origin
        self.direction = direction

    def atPoint(self, rayLambda):
        return (self.origin + rayLambda * self.direction)