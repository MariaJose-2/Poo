print("\nEjercicio 2 Herencia")

#definicion de la clase base Empleado
class Empleado:
    #se define el constructor que recibe nombre, edad y salario como parametros e inicializa los atributos de la instancia
    def __init__(self, nombre, edad, salario):
        
        #Asigna los valores de nombre, edad y salario a los atributos de la instancia.
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    #metodo para calcular salario y devuelve el salario sin ajustes
    def calcularSalario(self):
        return self.salario

#definicion de la clase derivada EmpleadoContratista que hereda de la clase base Empleado
class EmpleadoContratista(Empleado):
    
    #constructor que recibe nombre, edad, salario y duracion del contrato como parametros
    def __init__(self, nombre, edad, salario, duracionContrato):
        
        #llamada al constructor de la clase base Empleado para inicializar los atributos de nombre, edad y salario.
        super().__init__(nombre, edad, salario)
        
        #nuevo atributo especifico de EmpleadoContratista con el valor de duracionContrato.
        self.duracionContrato = duracionContrato

    #metodo para calcular salario que ajusta el salario segun la duracion del contrato
    def calcularSalario(self):
        
        #realiza un ajuste ficticio del salario multiplicando la duracion del contrato por 100 y sumandolo al salario existente.
        salarioAjustado = self.salario + (self.salario * (self.duracionContrato * 0.01))

        #devuelve el salario ajustado como resultado del metodo calcularSalario
        return salarioAjustado

#creacion de instancias de las clases Empleado y EmpleadoContratista
empleadoRegular = Empleado("Jose", 31, 1500000)
empleadoContratista = EmpleadoContratista("Carolina", 25, 1950000, 6)

#llamadas al metodo calcularSalario para cada empleado
print(f"Salario del empleado regular: {empleadoRegular.calcularSalario()}")
print(f"Salario del empleado contratista: {empleadoContratista.calcularSalario()}")
