from config import *

class Interval:
    def __init__(self, minimum, maximum):
        self.minimum = min(minimum, maximum)
        self.maximum = max(maximum, minimum)

    def __str__(self):
        return f"({self.minimum}, {self.maximum})"

    def contains(self, x):
        return (self.minimum <= x and x <= self.maximum)
    
    def surrounds(self, x):
        return (self.minimum < x and x < self.maximum)
    
    def clamp(self, x):
        if (x < self.minimum):
            return self.minimum
        if (x > self.maximum):
            return self.maximum
        else:
            return x