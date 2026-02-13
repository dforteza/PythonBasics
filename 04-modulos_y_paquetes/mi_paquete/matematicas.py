"""
Módulo de operaciones matemáticas dentro de mi_paquete
"""

print("[mi_paquete/matematicas.py] Cargando módulo matematicas...")

PI = 3.14159265359
E = 2.71828182846


def suma(a, b):
    """Suma dos números"""
    return a + b


def resta(a, b):
    """Resta dos números"""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b


def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def potencia(base, exponente):
    """Calcula base elevado a exponente"""
    return base ** exponente


if __name__ == "__main__":
    print("Probando matematicas.py:")
    print(f"PI = {PI}")
    print(f"5 + 3 = {suma(5, 3)}")
    print(f"10 / 2 = {dividir(10, 2)}")