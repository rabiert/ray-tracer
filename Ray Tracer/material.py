from config import *

class Material:
    def __init__(self):
        pass

    def scatter(self, ray, registry):
        return True

    def emitted(self, point):
        return Color(0, 0, 0)

class Lambertian(Material):
    def __init__(self, texture):
        self.texture = texture

    def scatter(self, ray, registry):
        scatterDirection = registry.normal + Vector.randomUnit()
        if (scatterDirection.nearZero()):
            scatterDirection = registry.normal
        registry.ray = Ray(registry.point, scatterDirection)
        registry.color = self.texture.value(registry.point)
        registry.reflects = False
        return True
    
class Metal(Material):
    def __init__(self, texture, fuzz):
        self.texture = texture
        self.fuzz = fuzz if (fuzz < 1) else 1

    def scatter(self, ray, registry):
        reflected = Vector.reflect(ray.direction.normalize(), registry.normal)
        registry.ray = Ray(registry.point, reflected + Vector.randomUnit() * self.fuzz)
        registry.color = self.texture.value(registry.point)
        registry.reflects = True
        return (Vector.dotProduct(registry.ray.direction, registry.normal) > 0)
    
class Dielectric(Material):
    def __init__(self, refractionIndex):
        self.refractionIndex = refractionIndex

    def scatter(self, ray, registry):
        registry.color = Color(1.0, 1.0, 1.0)
        
        refrRatio = 1.0 / self.refractionIndex if (registry.faceFront) else self.refractionIndex
        
        unitDirection = ray.direction.normalize()
        cosTheta = min(Vector.dotProduct(-unitDirection, registry.normal), 1.0)
        sinTheta = sqrt(1.0 - cosTheta * cosTheta)

        noRefraction = (refrRatio * sinTheta > 1.0)
        direction = Vector.reflect(unitDirection, registry.normal) if noRefraction or Dielectric.reflectance(cosTheta, refrRatio) > rd.uniform(0, 1) else Vector.refract(unitDirection, registry.normal, refrRatio)
        registry.reflects = True
        registry.ray = Ray(registry.point, direction)
        return True
    
    #SCHLICKS APPROXIMATION FOR REFLECTANCE#
    @staticmethod
    def reflectance(cosine, refrIndex):
        reflCoef = (1 - refrIndex) / (1 + refrIndex)
        reflCoef *= reflCoef
        return (reflCoef + (1 - reflCoef) * ((1 - cosine) ** 5))
    
class DiffuseLight(Material):
    def __init__(self, texture):
        self.texture = texture

    def scatter(self, ray, registry):
        registry.reflects = False
        return False
    
    def emitted(self, point):
        return self.texture.value(point)