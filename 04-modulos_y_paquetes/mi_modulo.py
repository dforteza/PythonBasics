"""
Módulo de ejemplo para practicar importaciones.
Este archivo demuestra cómo funciona __name__
"""

print(f"[mi_modulo.py] Se está importando/ejecutando mi_modulo")
print(f"[mi_modulo.py] __name__ = {__name__}")


def saludar(nombre):
    """Función simple para saludar"""
    return f"Hola, {nombre}!"


def despedir(nombre):
    """Función simple para despedir"""
    return f"Adiós, {nombre}!"


PI = 3.14159
VERSION = "1.0.0"


# Este bloque SOLO se ejecuta si ejecutas este archivo directamente
if __name__ == "__main__":
    print("\n=== EJECUTANDO mi_modulo.py DIRECTAMENTE ===")
    print(saludar("Ana"))
    print(despedir("Luis"))
    print(f"Valor de PI: {PI}")