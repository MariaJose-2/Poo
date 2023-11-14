print("\nEjercicio 2")

#Definicion de la clase Libro
class Libro:
    
    #metodo __init__, constructor de la clase Libro
    def __init__(self, titulo, autor, añoPub):
        
        #inicializacion de atributos con los valores proporcionados
        self.titulo = titulo
        self.autor = autor
        self.añoPub = añoPub

#metodo para mostrar los detalles del Libro
    def mostrarDetalles(self):
        
        #imprime la informacion utilizando atributos de la instancia
        print(f"Titulo: {self.titulo} \nAutor: {self.autor} \nAño de publicacion: {self.añoPub}")

#creacion de una instancia de la clase Libro
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "1615")

#acceso al atributo 'titulo' del objeto libro1
print(libro1.titulo)  #imprime: 'Don Quijote de la Mancha'

#llamada al metodo 'mostrarDetalles' del objeto libro1
libro1.mostrarDetalles()