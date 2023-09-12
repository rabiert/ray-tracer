from config import *

class RenderWindow(tk.Toplevel):
    def __init__(self, parent, diopter, samples, depth, renderOpt):
        super().__init__(parent)
        self.cameraObj = Camera(diopter, samples, depth)
        self.width = self.cameraObj.imageWidth
        self.height = self.cameraObj.imageHeight
        self.canvas = tk.Canvas(self, width = self.width, height = self.height)
        self.canvas.pack()
        self.scene = Scene().objectsList
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill='black')
        self.canvas.update_idletasks()
        begin = time.time()
        self.render(self.cameraObj, self.scene, renderOpt)  
        end = time.time()
        self.saveImage(f"img/render/{samples}x{samples}-{depth}-D{diopter}.png")
        print(end - begin)
        
    def render(self, cameraObj, scene, rendOpt):
        if rendOpt == 1:
            if(cameraObj.diopter < 0):
                return self.renderMyopia(cameraObj, scene)
            if(cameraObj.diopter > 0):
                return self.renderHypermetropia(cameraObj, scene)
            if cameraObj.diopter == 0:
                return self.renderRegular(cameraObj, scene)
        else:
            if(cameraObj.diopter < 0):
                return self.pathMyopia(cameraObj, scene)
            if(cameraObj.diopter > 0):
                return self.pathHypermetropia(cameraObj, scene)
            if cameraObj.diopter == 0:
                return self.renderPath(cameraObj, scene)

    def renderPath(self, cameraObj, scene):
        for j in range(self.height):
            for i in range(self.width):
                pixelColor = Color(0,0,0)
                for num in range(cameraObj.numSamplesSQ):
                    ray = cameraObj.shootRay(i, j, num)
                    pixelColor += pathTrace(ray, scene, cameraObj.maxDepth)
                a = pixelColor.writePixel(cameraObj.numSamplesSQ)
                self.canvas.create_line(i, j, i + 1, j, fill = a)
            self.canvas.update_idletasks()

    
    def pathMyopia(self, cameraObj, scene):
        for j in range(self.height):
            for i in range(self.width):
                pixelColor = Color(0,0,0)
                ray = cameraObj.shootRay(i, j, 1)
                depth = rayDepth(ray, scene, cameraObj.maxDepth, 0)
                for num in range(cameraObj.numSamplesSQ):
                    if depth <= cameraObj.focusDistance:   
                        ray = cameraObj.shootRay(i, j, num)
                    else:
                        ray = cameraObj.shootRay(i, j, num, True)
                    pixelColor += pathTrace(ray, scene, cameraObj.maxDepth)
                a = pixelColor.writePixel(cameraObj.numSamplesSQ)
                self.canvas.create_line(i, j, i + 1, j, fill = a)
            self.canvas.update_idletasks()

    def pathHypermetropia(self, cameraObj, scene):
        for j in range(self.height):
            for i in range(self.width):
                pixelColor = Color(0,0,0)
                ray = cameraObj.shootRay(i, j, 1)
                depth = rayDepth(ray, scene, cameraObj.maxDepth)
                for num in range(cameraObj.numSamplesSQ):
                    if depth <= cameraObj.focusDistance:
                        ray = cameraObj.shootRay(i, j, num, True)
                    else:
                        ray = cameraObj.shootRay(i, j, num)
                    pixelColor += pathTrace(ray, scene, cameraObj.maxDepth)
                a = pixelColor.writePixel(cameraObj.numSamplesSQ)
                self.canvas.create_line(i, j, i + 1, j, fill = a)
            self.canvas.update_idletasks()

    def renderRegular(self, cameraObj, scene):
        for j in range(self.height):
            for i in range(self.width):
                pixelColor = Color(0,0,0)
                for num in range(cameraObj.numSamplesSQ):
                    ray = cameraObj.shootRay(i, j, num)
                    pixelColor += rayColor(ray, scene, cameraObj.maxDepth)
                a = pixelColor.writePixel(cameraObj.numSamplesSQ)
                self.canvas.create_line(i, j, i + 1, j, fill = a)
            self.canvas.update_idletasks()

    def renderMyopia(self, cameraObj, scene):
        for j in range(self.height):
            for i in range(self.width):
                pixelColor = Color(0,0,0)
                ray = cameraObj.shootRay(i, j, 1)
                depth = rayDepth(ray, scene, cameraObj.maxDepth, 0)
                for num in range(cameraObj.numSamplesSQ):
                    if depth <= cameraObj.focusDistance:   
                        ray = cameraObj.shootRay(i, j, num)
                    else:
                        ray = cameraObj.shootRay(i, j, num, True)
                    pixelColor += rayColor(ray, scene, cameraObj.maxDepth)
                a = pixelColor.writePixel(cameraObj.numSamplesSQ)
                self.canvas.create_line(i, j, i + 1, j, fill = a)
            self.canvas.update_idletasks()
    
    def renderHypermetropia(self, cameraObj, scene):
        for j in range(self.height):
            for i in range(self.width):
                pixelColor = Color(0,0,0)
                ray = cameraObj.shootRay(i, j, 1)
                depth = rayDepth(ray, scene, cameraObj.maxDepth)
                for num in range(cameraObj.numSamplesSQ):
                    if depth <= cameraObj.focusDistance:
                        ray = cameraObj.shootRay(i, j, num, True)
                    else:
                        ray = cameraObj.shootRay(i, j, num)
                    pixelColor += rayColor(ray, scene, cameraObj.maxDepth)
                a = pixelColor.writePixel(cameraObj.numSamplesSQ)
                self.canvas.create_line(i, j, i + 1, j, fill = a)
            self.canvas.update_idletasks()

    def saveImage(self, file):
        ps = self.canvas.postscript(colormode='color')
        image = Image.open(io.BytesIO(ps.encode('utf-8')))
        image.save(file)