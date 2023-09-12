from config import *

class Vector:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        else:
            return self.z
        
    def __setitem__(self, key, newVal):
        if key == 0:
            self.x = newVal
        if key == 1:
            self.y == newVal
        if key == 2:
            self.z == newVal
        return self
        
    #VECTOR OPERATIONS#

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self  
      
    def __imul__(self, other):
        assert not isinstance(other, Vector)
        self.x *= other
        self.y *= other
        self.z *= other
        return self  
      
    def __idiv__(self, other):
        assert not isinstance(other, Vector)
        self.x /= other
        self.y /= other
        self.z /= other
        return self

    def __str__(self):
        return f"{self.x} {self.y} {self.z}"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        assert not isinstance(other, Vector)
        return Vector(self.x / other, self.y / other, self.z / other)
    
    @staticmethod
    def multiply(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
    
    @staticmethod
    def dotProduct(self, other):
        return float(self.x * other.x + self.y * other.y + self.z * other.z)
    
    @staticmethod
    def crossProduct(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)
    
    def magnitudeSquared(self):
        return Vector.dotProduct(self, self)
    
    def magnitude(self):
        return sqrt(self.magnitudeSquared())
    
    def normalize(self):
        return self / self.magnitude()
    
    #CHECK IF THE VECTOR IS NEAR ZERO#

    def nearZero(self):
        epsilon = 10 ** (-8)
        return (abs(self.x) < epsilon and abs(self.y) < epsilon and abs(self.z) < epsilon)
    
    #COMPUTE RECURSION RAYS#

    @staticmethod
    def reflect(self, normal):
        return self - 2 * Vector.dotProduct(self, normal) * normal
    
    @staticmethod
    def refract(self, normal, refrRatio):
        cosTheta = min(Vector.dotProduct(self, -normal), 1.0)
        perpendicularVector = refrRatio * (self + cosTheta * normal)
        parallelVector = -sqrt(abs(1.0 - perpendicularVector.magnitudeSquared())) * normal
        
        return (perpendicularVector + parallelVector)
    
    #COMPUTE RANDOM VECTORS# DEFOCUS DISK

    @staticmethod
    def randomVector(min, max):
        return Vector(rd.uniform(min, max), rd.uniform(min, max), rd.uniform(min, max))

    @staticmethod
    def randomUnit():
        while(True):
            unitVec = Vector.randomVector(-1, 1)
            return unitVec.normalize()