print("\nEjercicio 1")

#Definicion de la clase Estudiante
class EstudiantesSecundaria:
    
    #metodo __init__, constructor de la clase estudiante
    def __init__(self, nombre, edad, curso):
        
        #inicializacion de atributos con los valores proporcionados
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

#metodo para mostrar la informacion del estudiante
    def mostrarInformacion(self):
        #imprime la informacion utilizando atributos de la instancia
        print(f"Estudiante: {self.nombre}, {self.edad} años, Curso: {self.curso}")

#creacion de una instancia de la clase EstudiantesSecundaria
estudiante1 = EstudiantesSecundaria("Karla Andrade", "15", "decimo")
estudiante2 = EstudiantesSecundaria("Adrian Gomez", "18", "once")

#acceso al atributo 'nombre' del objeto estudiante1, estudiante2 e impresión
print(estudiante1.nombre)  #imprime 'Karla Andrade'
print(estudiante2.nombre)  #imprime 'Adrian Gomez'

#llamada al metodo 'mostrarInformacion' del objeto estudiante1 y estudiante2
estudiante1.mostrarInformacion()  
estudiante2.mostrarInformacion() #imprime: Estudiante: Karla Andrade, 15 años, Curso: decimo
