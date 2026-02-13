"""
Otro módulo para demostrar múltiples importaciones
"""

print(f"[otro_modulo.py] Cargando otro_modulo...")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


class Calculadora:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def operar(self, a, b, operacion):
        if operacion == "+":
            return sumar(a, b)
        elif operacion == "-":
            return restar(a, b)
        elif operacion == "*":
            return multiplicar(a, b)
        return "Operación no válida"


if __name__ == "__main__":
    print("Probando otro_modulo directamente:")
    print(f"5 + 3 = {sumar(5, 3)}")
    calc = Calculadora("MiCalc")
    print(f"10 * 2 = {calc.operar(10, 2, '*')}")