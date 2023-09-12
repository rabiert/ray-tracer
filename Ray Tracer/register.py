from config import *

class Register:
    def __init__(self, point = Point(0, 0, 0), uVector = Vector(0, 0, 0), vVector = Vector(0, 0, 0), normal = Vector(0, 0, 0), rayLambda = 0.0, faceFront = False, color = Color(0, 0, 0), material = Material(), ray = Ray(), depth = 0.0, reflects = False):
        self.point = point
        self.normal = normal
        self.rayLambda = rayLambda
        self.faceFront = faceFront
        self.material = material
        self.ray = ray
        self.depth = depth
        self.vVector = vVector
        self.uVector = uVector
        self.color = color
        self.reflects = reflects

    #SET THE DIRECTION OF THE NORMAL VECTOR#

    def setNormal(self, ray, outNormal):
        outNormal = outNormal.normalize()
        self.faceFront = (Vector.dotProduct(ray.direction, outNormal) < 0.0)
        self.normal = outNormal if self.faceFront else -outNormal

    def interior(self, alpha, beta):
        if alpha < 0 or 1 < alpha or beta < 0 or 1 < beta:
            return False
        self.uVector, self.vVector = alpha, beta
        return True