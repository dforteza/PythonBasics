"""
Archivo __init__.py del paquete mi_paquete

Este archivo se ejecuta cuando importas el paquete.
Define qué es público y qué está disponible.
"""

print("[mi_paquete/__init__.py] Inicializando paquete mi_paquete...")

# Importar módulos internos usando imports relativos
from .matematicas import suma, resta, PI
from .utilidades import limpiar_texto, contar_palabras

# Definir qué se exporta con "from mi_paquete import *"
__all__ = [
    "suma",
    "resta",
    "PI",
    "limpiar_texto",
    "contar_palabras"
]

# Puedes inicializar configuración del paquete aquí
VERSION = "1.0.0"

print(f"[mi_paquete/__init__.py] Paquete mi_paquete v{VERSION} listo")