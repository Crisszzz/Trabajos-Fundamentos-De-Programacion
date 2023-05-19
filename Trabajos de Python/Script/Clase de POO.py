class Persona:
    def inicializar(self,nom,edad):
        self.nombre=nom
        self.edad=edad
    def imprimir(self):
        print("Nombre",self.nombre)
        print("Edad",self.edad)

persona1=Persona() #Contruir un objeto de tipo clase
persona1.inicializar("Pedro",10)  #Mensaje paara escoger un objeto
persona1.imprimir()

persona2=Persona() #Construir un objeto tipo clase
persona2.inicializar("Carla",12) #Mensaje para escoger un objeto
persona2.imprimir()

if (persona1.edad)>(persona2.edad):
   print("Pedro es mayor que Carla")
else:
    print("Carla es mayor que Pedro")