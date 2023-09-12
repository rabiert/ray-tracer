from config import *

class Color(Vector):
    @staticmethod
    def linearToGamma(linearComponent):
        return sqrt(linearComponent)
    
    def intensity(self):
        return (self.x + self.y + self.z) / 3
    
    @staticmethod
    def getVariance(colors):
        intensities = []
        for color in colors:
            intensities.append(color.intensity())
        return Color.variance(intensities)
    
    @staticmethod
    def variance(intensities):
        mean = 0
        var = 0
        for intensity in intensities:
            mean += intensity
        mean /= len(intensities)
        for i in range(len(intensities)):
            var += (intensities[i] - mean) * (intensities[i] - mean)
        var /= (len(intensities) - 1)
        return var
        

    def rgbToHex(self, R, G, B):
        return f'#{R:02x}{G:02x}{B:02x}'

    
    def getColor(self, numSamples):
        R = self.x
        G = self.y
        B = self.z

        scale = 1.0 / numSamples

        R *= scale
        G *= scale
        B *= scale

        R = Color.linearToGamma(R)
        G = Color.linearToGamma(G)
        B = Color.linearToGamma(B)

        intensity = Interval(0.000, 0.999)
        return Color(256 * intensity.clamp(R), 256 * intensity.clamp(G), 256 * intensity.clamp(B))

    def writePixel(self, numSamples):
        col = self.getColor(numSamples)
        return self.rgbToHex(int(col.x), int(col.y), int(col.z))