print("\nEjercicio 1 Herencia")

# Definicion de la clase base Vehiculo
class Vehiculo:
    # Constructor que recibe marca y modelo como parametros e inicializa los atributos de la instancia.
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    #metodo para obtener informacion del vehiculo
    def obtenerInformacion(self):
        return f"Vehículo: {self.marca} {self.modelo}"

#definicion de la clase derivada VehiculoElectrico que hereda de la clase base Vehiculo
class VehiculoElectrico(Vehiculo):
    
    #constructor que recibe marca, modelo y capacidad de bateria como parametros
    def __init__(self, marca, modelo, capacidadBateria):
        
        #llamada al constructor de la clase base Vehiculo para inicializar los atributos de marca y modelo
        super().__init__(marca, modelo)
        
        #nuevo atributo especifico de VehiculoElectrico
        #inicializa el atributo especifico de VehiculoElectrico con el valor de capacidadBateria
        self.capacidadBateria = capacidadBateria

    #metodo para obtener informacion del vehiculo electrico
    def obtenerInformacion(self):
        
        #llamada al metodo de la clase base Vehiculo
        informacionBase = super().obtenerInformacion()
        
        #incluir informacion adicional especifica de VehiculoElectrico
        return f"{informacionBase}, Capacidad de Bateria: {self.capacidadBateria} kWh"

# Creacion de instancias de las clases Vehiculo y VehiculoElectrico
vehiculoTradicional = Vehiculo("Toyota", "Corolla")
vehiculoElectrico = VehiculoElectrico("Tesla", "Model S", 75)

# Llamadas al metodo obtenerInformacion para cada vehiculo
print(vehiculoTradicional.obtenerInformacion())
print(vehiculoElectrico.obtenerInformacion())
        