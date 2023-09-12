from config import *

class Camera:
    def __init__(self, diopter, numSamples, maxDepth):
        self.imageWidth = 400
        self.imageHeight = 400
        self.maxDepth = maxDepth
        self.numSamples = numSamples
        self.numSamplesSQ = numSamples * numSamples
        self.diopter = diopter

        self.fov = 90
        self.defocusRate = 2

        self.lookfrom = Point(0, 0, 0)
        self.lookat = Point(0, 0, -1)
        self.vup = Vector(0, 1, 0)

        #SET FOCUS DISTANCE#
        if (self.diopter < 0):
            self.focusDistance = (1 / abs(self.diopter)) * self.defocusRate
        elif(self.diopter > 0):
            self.focusDistance = (1 / (5 - abs(self.diopter))) * self.defocusRate
            
        else:
            #IF DIOPTER IS 0 FOCUS DISTANCE IS EQUAL TO FOCAL LENGTH#
            self.focusDistance = (self.lookfrom - self.lookat).magnitude()

        self.h = tan( radians(self.fov) / 2)

        #SET VIEWPORT#
        self.vpHeight = 2.0 * self.h * self.focusDistance
        self.vpWidth = self.vpHeight * self.imageWidth / self.imageHeight
        self.cameraCenter = self.lookfrom

        self.w = (self.lookfrom - self.lookat).normalize()
        self.u = Vector.crossProduct(self.vup, self.w).normalize()
        self.v = Vector.crossProduct(self.w, self.u)

        self.vpuVector = self.vpWidth * self.u
        self.vpvVector = -self.vpHeight * self.v

        #SET PIXELS#
        self.pixelWidth = self.vpuVector / self.imageWidth
        self.pixelHeight = self.vpvVector / self.imageHeight

        #RENDERING STARTS FROM VIEWPORT UPPER LEFT#
        self.vpUpperLeft = self.cameraCenter - (self.focusDistance * self.w) - (self.vpuVector / 2) - (self.vpvVector / 2)
        self.pixelCenter = self.vpUpperLeft + 0.5 * (self.pixelWidth + self.pixelHeight)

        self.defocusRadius = 0.005
        self.defocusUDISK = self.u * self.defocusRadius
        self.defocusVDISK = self.v * self.defocusRadius

    def defocusDisk(self):
        px, py = rd.uniform(-1, 1), rd.uniform(-1, 1)
        return (self.cameraCenter + px * self.defocusUDISK + py * self.defocusVDISK)

    def pixelSample(self):
        px, py = -0.5 + rd.uniform(0, 1), (-0.5 + rd.uniform(0, 1))
        ret = (px) * self.pixelWidth +  py * self.pixelHeight
        return Vector(ret.x, ret.y, ret.z)
 
    def shootRaySamp(self, i, j, num, depth = False):
        pixelCenter = self.pixelCenter + (i * self.pixelWidth) + (j * self.pixelHeight)
        pixelSample =  pixelCenter + self.pixelSample()
        
        rayOrigin = self.cameraCenter if not depth else self.defocusDisk()
        rayDirection = pixelSample - rayOrigin
            
        return Ray(rayOrigin, rayDirection)

    #SHOOTING RAYS
    def shootRay(self, i, j, num, depth = False):   
        pixelCenter = self.pixelCenter + (i * self.pixelWidth) + (j * self.pixelHeight)

        pixelUpperLeft = pixelCenter - (self.pixelWidth / 2) - (self.pixelHeight / 2)

        row = int(num/self.numSamples)
        column = num % (self.numSamples)
        pixelSample = pixelUpperLeft + (column * self.pixelWidth / self.numSamples) + (row * self.pixelHeight / self.numSamples)
        rayOrigin = self.cameraCenter if not depth else self.defocusDisk()
        rayDirection = pixelSample - rayOrigin
            
        return Ray(rayOrigin, rayDirection)

