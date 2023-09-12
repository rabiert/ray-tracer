from config import *


class Texture:
    def __init__(self):
        pass

    def value(self, point):
        pass

class ConstantColor(Texture):
    def __init__(self, color = Color()):
        self.color = color

    @staticmethod
    def create(R, G, B):
        return ConstantColor(Color(R, G, B))
    
    def value(self, point):
        return self.color
    
class Checker(Texture):
    def __init__(self, scale, even = Color(0, 0, 0), odd = Color(1, 1, 1)):
        self.invScale = (1.0 / scale)
        self.odd = odd
        self.even = even

    def create(self, scale, colorEven, colorOdd):
        self.invScale = (1.0 / scale)
        self.even = colorEven
        self.off = colorOdd

    def value(self, point):
        xInt = floor(self.invScale * point.x)
        yInt = floor(self.invScale * point.y)
        zInt = floor(self.invScale * point.z)

        isEven = ((xInt + yInt + zInt) % 2 == 0)

        return self.even if isEven else self.odd