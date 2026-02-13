"""
Módulo de utilidades varias dentro de mi_paquete
"""

print("[mi_paquete/utilidades.py] Cargando módulo utilidades...")


def limpiar_texto(texto):
    """Elimina espacios extra y convierte a minúsculas"""
    return " ".join(texto.lower().split())


def contar_palabras(texto):
    """Cuenta el número de palabras en un texto"""
    return len(texto.split())


def invertir_texto(texto):
    """Invierte un texto"""
    return texto[::-1]


def es_palindromo(texto):
    """Verifica si un texto es palíndromo"""
    limpio = limpiar_texto(texto).replace(" ", "")
    return limpio == limpio[::-1]


class Validador:
    """Clase para validar diferentes tipos de datos"""
    
    @staticmethod
    def es_email_valido(email):
        """Validación simple de email"""
        return "@" in email and "." in email.split("@")[1]
    
    @staticmethod
    def es_longitud_valida(texto, min_len=3, max_len=50):
        """Verifica si la longitud del texto está en el rango"""
        return min_len <= len(texto) <= max_len


if __name__ == "__main__":
    print("Probando utilidades.py:")
    print(limpiar_texto("  HOLA   Mundo  "))
    print(f"Palabras en 'hola mundo': {contar_palabras('hola mundo')}")
    print(f"¿'anilina' es palíndromo? {es_palindromo('anilina')}")