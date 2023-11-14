print("\nEjercicio 1 Polimorfismo")

#importa el modulo math para operaciones matematicas
import math

#definicion de la clase base FormaGeometrica
class FormaGeometrica:
    #metodo para calcular el area (se implementara en las clases derivadas)
    def calcularArea(self):
        pass

#definicion de la clase derivada Circulo que hereda de FormaGeometrica
class Circulo(FormaGeometrica):
    #constructor que recibe el radio como parametro
    def __init__(self, radio):
        #inicializa el atributo de instancia radio con el valor proporcionado
        self.radio = radio

    #implementacion del metodo para calcular el area de un circulo
    def calcularArea(self):
        #aqui se realiza el calculo del area del circulo, se multiplica π por el cuadrado del radio
        return math.pi * self.radio**2

#definicion de la clase derivada Cuadrado que hereda de FormaGeometrica
class Cuadrado(FormaGeometrica):
    #constructor que recibe el lado como parametro
    def __init__(self, lado):
        #inicializa el atributo de instancia lado con el valor proporcionado
        self.lado = lado

    #implementacion del metodo para calcular el area de un cuadrado
    def calcularArea(self):
        return self.lado**2

#definicion de la clase derivada Triangulo que hereda de FormaGeometrica
class Triangulo(FormaGeometrica):
    #constructor que recibe la base y la altura como parametros
    def __init__(self, base, altura):
        #inicializa los atributos de instancia base y altura con los valores proporcionados
        self.base = base
        self.altura = altura

    #implementacion del metodo para calcular el area del triangulo
    def calcularArea(self):
        #se realiza el calculo del area del triangulo tomando la base y la altura de la clase Triangulo, el 0.5 es un factor y esta establecido en la formula del area del triangulo
        return 0.5 * self.base * self.altura

#funcion para calcular el area total de una lista de formas geometricas
#define una funcion llamada calcularAreaTotal que toma una lista de formas geometricas como parametro.
def calcularAreaTotal(formas):
    #inicializa una variable llamada total con el valor 0. Esta variable se utilizara para acumular el area total
    total = 0
    
    #bucle for para iterar sobre cada forma en la lista y suma sus areas al total
    for forma in formas:
        
        #llama al metodo calcularArea de cada forma y agrega el resultado al total, este paso se repite para cada forma en la lista
        total += forma.calcularArea()
        
    #La funcion retorna el area total acumulada
    return total

#creacion de instancias de las clases Circulo, Cuadrado y Triangulo. Con valores establecidos
circulo = Circulo(5)
cuadrado = Cuadrado(4)
triangulo = Triangulo(3, 6)

#calcula el area total de las formas geometricas en la lista [circulo, cuadrado, triangulo]
areaTotal = calcularAreaTotal([circulo, cuadrado, triangulo])

#imprime el resultado
print(f"Área total de las formas: {areaTotal:.0f}")
