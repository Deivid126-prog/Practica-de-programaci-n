from abc import ABC, abstractmethod
import math

class Operacion(ABC):
    def __init__(self, numero1, numero2=None):
        self.set_numero1(numero1)
        self.set_numero2(numero2)

    @abstractmethod
    def calcular(self):
        pass

    def get_numero1(self):
        return self.__numero1

    def set_numero1(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("El valor debe ser numerico")
        self.__numero1 = valor

    def get_numero2(self):
        return self.__numero2

    def set_numero2(self, valor):
        if valor is not None and not isinstance(valor, (int, float)):
            raise TypeError("El valor debe ser numerico")
        self.__numero2 = valor
    

#Clase Hija
class Suma(Operacion):
    def calcular(self):
        return self.get_numero1() + self.get_numero2() 
class Resta(Operacion):
    def calcular(self):
        return self.get_numero1() - self.get_numero2()
class Multiplicacion(Operacion):
    def calcular(self):
        return self.get_numero1() * self.get_numero2()
class Division(Operacion):
    def calcular(self):
        if self.get_numero2 == 0:
            raise ValueError("El numero debe ser distinto de cero")
        return self.get_numero1() / self.get_numero2()
    
class Calculadora:
    def __init__(self):
        self.operaciones_realizadas = []
    
    def realizar_operaciones(self, tipo, n1, n2=None):
        try:
            if tipo == "Suma":
                op = Suma(n1, n2)
            elif tipo == "Resta":
                op = Resta(n1, n2)
            elif tipo == "Multiplicacion":
                op = Multiplicacion(n1, n2)
            elif tipo == "Division":
                op = Division(n1,n2)
            else:
                raise ValueError("Tipo de operacion no validad")
            
            resultado = op.calcular()
            self.operaciones_realizadas.append(f"{tipo} ({n1}, {n2})= {resultado}")
            print(f"Resultado: {resultado}")
        except (ValueError, TypeError) as e:
            print(e)
            
    def historial(self):
        print("\n HISTORIAL DE OPERACIONES")
        if not self.operaciones_realizadas:
            print("EL HISTORIAL ESTA VACIO")
        else:
            for op in self.operaciones_realizadas:
                print(op)

class CalculadoraCientifica(Calculadora):
    def realizar_operaciones_cientifica(self, tipo, n1):
        try:
            if tipo == "Potencia":
                potencia = n1 ** 2
                self.operaciones_realizadas.append(f"Potencia ({n1}) = ({potencia})")
                print(f"Resultado: {potencia}")
            elif tipo == "Raiz Cuadrada":
                if n1 == 0:
                    raise ValueError("EL NUMERO DEBE DISTINTO DE CERO")
                raiz = math.sqrt(n1)
                self.operaciones_realizadas.append(f"Raiz Cuadrada ({n1}) = {raiz}")
                print(f"Resultado: {raiz}")
            else:
                raise ValueError("NO SE PUEDE CALCULAR LA RAZ CUADRADA")
        except (ValueError, TypeError) as e:
            print(e)
            
def menu_interativo():
    calc = CalculadoraCientifica()
    while True:
        print("\n MENU DE LA CALCULADORA")
        print("1- Suma")
        print("2- Resta")
        print("3- Multiplicacion")
        print("4- Divicion")
        print("5- Potencia")
        print("6- Raiz Cuadrada")
        print("7- Ver Historial")
        print("8- Salir")
        
        opcion = input("\nSeleccione uan opcion:")
        
        if opcion == "8":
            print( "¡Adios!")
            break
        elif opcion == "7":
            calc.historial()
        elif opcion in ["1", "2", "3", "4", "5", "6"]:
            try:
                if opcion in ["1", "2", "3", "4"]:
                    n1 = float(input("Ingrese el primer Numero: "))  
                    n2 = float(input("Ingrese el segundo Numero: ")) 
                    if opcion == "1":
                        calc.realizar_operaciones("Suma", n1, n2)
                    elif opcion == "2":
                        calc.realizar_operaciones("Resta", n1, n2)
                    elif opcion == "3":
                        calc.realizar_operaciones("Multiplicacion", n1, n2)
                    elif opcion == "4":
                        calc.realizar_operaciones("Division", n1, n2)
                elif opcion in ["5", "6"]:
                    n1 = float(input("Ingrese numero: "))
                    if opcion == "5":
                        calc.realizar_operaciones_cientifica("Potencia", n1)
                    elif opcion == "6":
                        calc.realizar_operaciones_cientifica("Raiz Cuadrada", n1)
            except ValueError:
                print("Entrada no valida. Por favor ingrese un numero")
        else:
            print("Opcion no valida")
                
if __name__ == "__main__":
    menu_interativo()