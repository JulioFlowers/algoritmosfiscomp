import bpy

#Clase para el atractor de Lorentz
#Usando el método de diferencias finitas
#implementar aca algun metodo de runge kutta a la verga o justificar porque no se necesita la precision

class Lorenz:
    def _init_(self,sceneRef, objName, color, initX, initY, initZ):
        self.X, self.Y, self.Z = initX, initY, initZ
        self.dt = 0.005
        self.a, self.b, self.c = 10, 28, 8/3
        self.color = color
        self.objName = objName
        self.sceneRef = sceneRef

    def Step(self):
        self.X = self.X + (self.dt *self.a * (self.Y - self.X))
        self.Y = self.Y + (self.dt *(self.X *(self.d - self.Z) - self.Y))
        self.Z = self.Z + (self.dt *(self.X *self.Y - self.c *self.Z))

    def Generar(self):
        #definiendo el numero de puntos a usar
        numPuntos = 10000

        #Creando un bloque de datos de la curva:
        self.curve = bpy.data.curves.new("CurvaLorenz", type='CURVE')
        self.curve.dimensions = '3D'
        self.curve.bevel_depth = 0.1

        #Creando un cuerpo ligado al bloque de datos
        atractorPoly = self.curve.splines.nem('POLY')
        atractorPoly.points.add(numPuntos - 1)

        #Generar las coordenas para la linea 
        for i in range(0, numPuntos):
            atractorPoly.points[i].co = (self.x, self.Y, self.Z, 1)
            self.Step()
        
        #Crear un objeto que aprarezc en la escena de Blender
        self.body = bpy.data.objects.nem('curve', self.curve)

        #Renombrar el objeto y añadirlo a la escena
        self.body.name = self.objName
        self.sceneRef.collection.objects.link(self.body)

#Poniendo una referencia en la escena.
scene = bpy.context.scene

#Crear el atractor de Lorenz
atractor1 = Lorenz(scene, "atractor1", (1.0, 0.4, 0.0, 1.0), 0.1, 0.0, 0.0)
atractor1.Generar()


    

