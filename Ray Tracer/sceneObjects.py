from config import *

class SceneObject:
    def __init__(self, ray, lambdaMin, lambdaMax, registry):
        pass

class Sphere(SceneObject):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def hit(self, ray, interval, registry):
        OC = ray.origin - self.center
        A = ray.direction.magnitudeSquared()
        halfB = Vector.dotProduct(OC, ray.direction)
        C = OC.magnitudeSquared() - self.radius * self.radius
        discriminant = halfB * halfB - A * C

        if discriminant < 0:
            return False
        
        #CHECK WHETHER THERE ARE SOLUTIONS IN FRONT OF THE CAMERA#
        SQ = sqrt(discriminant)
        ROOT = (-halfB - SQ) / (A)
        if not interval.surrounds(ROOT):
            ROOT = (-halfB + SQ) / (A)
            if not interval.surrounds(ROOT):
                return False
            
        registry.point = ray.atPoint(ROOT)
        registry.rayLambda = ROOT

        #DEFINE NORMAL VECTOR NORMALIZED#
        outNormal = (registry.point - self.center) / self.radius
        registry.setNormal(ray, outNormal)
        registry.material = self.material
        registry.depth = (ray.origin + ROOT * ray.direction).magnitude()
        return True

class Quad(SceneObject):
    def __init__(self, startPoint = Point(0,0,0), uVector = Vector(0,0,0), vVector = Vector(0,0,0), material = Material()):
        self.startPoint = startPoint
        self.uVector = uVector
        self.vVector = vVector
        self.material = material
        self.normal = Vector.crossProduct(uVector, vVector)
        self.unitNormal = self.normal.normalize()
        self.D = Vector.dotProduct(self.unitNormal, self.startPoint)
        self.W = self.normal / self.normal.magnitudeSquared()

    def hit(self, ray, interval, registry):
        denominator = Vector.dotProduct(self.unitNormal, ray.direction)
        if (abs(denominator) < 10 ** (-6)):
            return False
        
        rayLambda = (self.D - Vector.dotProduct(self.unitNormal, ray.origin)) / denominator
        if not interval.contains(rayLambda):
            return False
        
        intersection = ray.atPoint(rayLambda)

        planeHits = intersection - self.startPoint
        alpha = Vector.dotProduct(self.W, Vector.crossProduct(planeHits, self.vVector))
        beta = Vector.dotProduct(self.W, Vector.crossProduct(self.uVector, planeHits))

        #CHECK IF THE INTERESCTION IS INSIDE THE PLANE#
        if not registry.interior(alpha, beta):
            return False
        
        registry.point = intersection
        registry.rayLambda = rayLambda
        registry.setNormal(ray, self.unitNormal)
        registry.material = self.material
        registry.depth = (ray.origin + rayLambda * ray.direction).magnitude()
        return True

class ObjectsList(SceneObject):
    def __init__(self, objectsList):
        self.objectsList = objectsList

    def hit(self, ray, interval, registry):
        temporaryRegistry = registry
        hitAnything = False
        closestLambda = interval.maximum
        for object in self.objectsList:
            if object.hit(ray, Interval(interval.minimum, closestLambda), temporaryRegistry):
                hitAnything = True
                closestLambda = temporaryRegistry.rayLambda
                registry.point = temporaryRegistry.point
                registry.normal = temporaryRegistry.normal
                registry.depth = temporaryRegistry.depth
        return hitAnything