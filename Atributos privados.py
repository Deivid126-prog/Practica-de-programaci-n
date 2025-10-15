# Los metodos tradicionales para acceder a los datos privaods
# get() Leer omostrar los datos del atributo
# set() Modificar los datos del atributo
# Atributo es privado para poder proteger la informacion que almacena = Encapsulamiento
# Su proposito es evitar que alguien modifique el estado interno de una manera incorrecta
# Atributo publico: se puede acceder desde cualqier parte y no lleva guion bajo

# Ejemplo sin atributos privados
""""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributos publicos
        self.edad = edad
        
# proframa principa
# instancia

pers = Persona ("Maria", 45)
print(pers.edad) #accede directamente a los datos
pers.edad = -5

"""
# trabajamos con get y self atributos privados

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributos privados
        self.__edad = edad

    # Getter
    def get_edad(self):
        return self.__edad

    # Setter modificador
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser positiva")

    # Getter para nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para nombre
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
#Programa principal

pers = Persona ("Maria", 45)
print(pers.get_edad())
pers.set_edad(25)
print(pers.get_edad())
pers.set_edad(-5) # no corresponde
