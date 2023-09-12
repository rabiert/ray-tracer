from config import *

class Scene:
    def __init__(self):
        material_white = Lambertian(ConstantColor(Color(1, 1, 1)))
        material_center = Lambertian(ConstantColor(Color(0.1, 0.5, 0.7)))
        material_reflective = Metal(ConstantColor(Color(0.6, 0.7, 0.4)), 0.01)
        material_right = Metal(ConstantColor(Color(0.4, 0.3, 0.9)), 0.0)
        mirror = Metal(ConstantColor(Color(0.8, 0.8, 0.8)), 0.0)
        dielectric_material = Dielectric(1.5)

        difflight = DiffuseLight(ConstantColor(Color(0, 15, 15)))

        #green wall
        QUAD1 = Quad(Point(-1, -1, 0.01), Vector(0,2,0), Vector(0,0,-2.01), Lambertian(ConstantColor(Color(.12, .45, .15))))
        
        #white wall
        QUAD2 = Quad(Point(1, -1, 0.01), Vector(0,2,0), Vector(0,0,-2.01), Lambertian(ConstantColor(Color(.73, .73, .73))))
        
        #floor
        QUAD3 = Quad(Point(-1, 1, 0.01), Vector(2,0,0), Vector(0,0,-2.01), Lambertian(ConstantColor(Color(.73, .73, .73))))
        
        #ceiling
        QUAD4 = Quad(Point(-1, -1, 0.01), Vector(2,0,0), Vector(0,0,-2.01), Lambertian(ConstantColor(Color(.12, .12, .12))))
        
        #plane back
        QUAD5 = Quad(Point(-1, -1, -2), Vector(2,0,0), Vector(0,2,0), mirror)

        #red wall
        QUAD6 = Quad(Point(-1, -1, 0.01), Vector(2,0,0), Vector(0,2,0), Lambertian(ConstantColor(Color(.65, .05, .05))))
        
        #light
        QUAD7 = Quad(Point(-0.50, 0.99, -0.50), Vector(1,0,0), Vector(0,0,-1), DiffuseLight(ConstantColor(Color(5, 5, 5))))
        

        #Refractive spheres
        SPHERE1 = Sphere(Point(-0.5, -0.50, -1.5), 0.48, dielectric_material)
        SPHERE2 = Sphere(Point(-0.50, -0.50, -1.5), 0.38, dielectric_material)
        
        #reflective sphere
        SPHERE3 = Sphere(Point(0.6, 0.25, -1.1), 0.24, material_reflective)

        #white lambertian sphere
        SPHERE4 = Sphere(Point(0.65, -0.65, -1.2), 0.35, material_white)

        #Lambertian sphere close to the camera
        SPHERE5 = Sphere(Point(-0.12, 0.02, -0.12), 0.07, material_center)


        self.objectsList = ObjectsList([SPHERE1, SPHERE2, SPHERE3, SPHERE4, QUAD1, QUAD2, QUAD3, QUAD4, QUAD5, QUAD6, QUAD7])