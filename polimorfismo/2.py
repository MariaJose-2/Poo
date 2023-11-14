print("\nEjercicio 2 Polimorfismo")

#definicion de la clase base Animal
class Animal:
    #metodo abstracto para hacer un sonido (se implementara en las clases derivadas)
    def hacerSonido(self):
        pass

#definicion de la clase derivada Dinosaurio que hereda de Animal
class Dinosaurio(Animal):
    #implementacion del metodo para hacer sonar a un Dinosaurio
    def hacerSonido(self):
        return "¡rawr!"

#definicion de la clase derivada Pato que hereda de Animal
class Pato(Animal):
    #implementacion del metodo para hacer sonar a un pato
    def hacerSonido(self):
        return "¡cua, cua, cua!"

#definicion de la clase derivada Pollito que hereda de Animal
class Pollito(Animal):
    #implementacion del metodo para hacer sonar a un pollito
    def hacerSonido(self):
        return "pio, pio, pio"

#funcion para hacer sonar a cualquier animal
def hacerSonar(animal):
    return animal.hacerSonido()

#creacion de instancias de las clases Dinosaurio, Pato y Pollito
dinosaurio = Dinosaurio()
pato = Pato()
pollito = Pollito()

# Llamadas a la función hacerSonar para cada animal
print(hacerSonar(dinosaurio))
print(hacerSonar(pato))
print(hacerSonar(pollito))
