from config import *

def rayColor(ray, sceneObject, MAX_DEPTH):
    background = Color(0, 0, 0)
    registry = Register()
    if(MAX_DEPTH <= 0):
        return Color(0, 0, 0)
    a = Interval(0.001, 10**6)
    if  (sceneObject.hit(ray, a, registry)) is False:
        return background
    colorFromEmission = registry.material.emitted(registry.point)
    if (registry.material.scatter(ray, registry)) is False:
        return colorFromEmission
    ray = registry.ray
    colorFromScatter = Vector.multiply(registry.color, rayColor(ray, sceneObject, MAX_DEPTH - 1))
    col = colorFromEmission + colorFromScatter
    return Color(col.x, col.y, col.z)
    
def rayDepth(ray, ObjectsList, MAX_DEPTH, SUM = 0):
    registry = Register()
    if(MAX_DEPTH <= 0):
        return 0
    a = Interval(0.001, 10**6)
    if(ObjectsList.hit(ray, a, registry)):
        if (registry.material.scatter(ray, registry)):
            SUM += registry.depth
            if registry.reflects is True:
                ray = registry.ray
                return rayDepth(ray, ObjectsList, MAX_DEPTH - 1, SUM)  
    return SUM

def pathTrace(ray, sceneObject, MAX_DEPTH):
    registry = Register()
    if(MAX_DEPTH <= 0):
        return Color(0, 0, 0)
    a = Interval(0.001, 10**6)
    if(sceneObject.hit(ray, a, registry)):
        if (registry.material.scatter(ray, registry)):
            ray = registry.ray
            return Vector.multiply(registry.color, pathTrace(ray, sceneObject, MAX_DEPTH - 1))
    unitDir = ray.direction.normalize()
    a = 0.5 * (unitDir.y + 1.0)
    myCol = (1-a) * Color(1.0, 1.0, 1.0) + (a) * Color(0.5, 0.7, 1.0)
    return (Color(myCol.x, myCol.y, myCol.z))