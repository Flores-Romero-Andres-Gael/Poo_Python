#Flores Romero Andres Gael 
# 16/04/2023

# Clase: definición de la clase Animal
class Animal:
    # Atributos
    nombre = ""
    edad = 0
    especie = ""
    # Métodos
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
    def sonido(self):
        pass # Método abstracto
    def info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Especie:", self.especie)

# Clase hija: definición de la clase Perro, que hereda de la clase Animal
class Perro(Animal):
    # Atributos
    raza = ""
    # Métodos
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza
    def sonido(self):
        print("Guau guau!")
    def info(self):
        super().info()
        print("Raza:", self.raza)

# Clase hija: definición de la clase Gato, que hereda de la clase Animal
class Gato(Animal):
    # Atributos
    raza = ""
    # Métodos
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Gato")
        self.raza = raza
    def sonido(self):
        print("Miau miau!")
    def info(self):
        super().info()
        print("Raza:", self.raza)

# Creación de instancias de objetos
perro1 = Perro("Fido", 3, "Labrador")
gato1 = Gato("Mimi", 2, "Persa")

# Uso de los métodos y atributos de las instancias de objetos
perro1.sonido() # Salida: Guau guau!
gato1.sonido() # Salida: Miau miau!
perro1.info() # Salida: Nombre: Fido, Edad: 3, Especie: Perro, Raza: Labrador
gato1.info() # Salida: Nombre: Mimi, Edad: 2, Especie: Gato, Raza: Persa
