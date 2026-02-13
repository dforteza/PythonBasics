"""
APUNTES: MÓDULOS Y PAQUETES EN PYTHON
======================================

Este archivo demuestra todas las formas de importar módulos y paquetes.

Estructura del proyecto:
proyecto/
├── apuntes_modulos.py (este archivo)
├── mi_modulo.py
├── otro_modulo.py
└── mi_paquete/
    ├── __init__.py
    ├── matematicas.py
    └── utilidades.py
"""

import sys

print("="*60)
print("INICIANDO APUNTES DE MÓDULOS Y PAQUETES")
print("="*60)

# ============================================
# 1. IMPORTAR MÓDULO COMPLETO
# ============================================

print("\n" + "="*60)
print("1. IMPORTAR MÓDULO COMPLETO")
print("="*60)

import mi_modulo

# Ahora usas: nombre_modulo.funcion()
print(mi_modulo.saludar("Carlos"))
print(mi_modulo.despedir("María"))
print(f"PI desde mi_modulo: {mi_modulo.PI}")

# ============================================
# 2. IMPORTAR ELEMENTOS ESPECÍFICOS
# ============================================

print("\n" + "="*60)
print("2. IMPORTAR ELEMENTOS ESPECÍFICOS")
print("="*60)

from otro_modulo import sumar, restar, Calculadora

# Ahora usas directamente: funcion()
print(f"10 + 5 = {sumar(10, 5)}")
print(f"10 - 5 = {restar(10, 5)}")

calc = Calculadora("Calculadora Pro")
print(f"Calculadora: {calc.nombre}")

# ============================================
# 3. IMPORTAR CON ALIAS
# ============================================

print("\n" + "="*60)
print("3. IMPORTAR CON ALIAS")
print("="*60)

import otro_modulo as om

# Ahora usas: alias.funcion()
print(f"7 * 6 = {om.multiplicar(7, 6)}")

# También puedes alias individuales
from mi_modulo import saludar as hola

print(hola("Alias"))

# ============================================
# 4. IMPORTAR DESDE PAQUETES
# ============================================

print("\n" + "="*60)
print("4. IMPORTAR DESDE PAQUETES")
print("="*60)

# Forma 1: Importar del paquete (usa __init__.py)
from mi_paquete import suma, resta, PI

print(f"15 + 8 = {suma(15, 8)}")
print(f"15 - 8 = {resta(15, 8)}")
print(f"PI desde paquete: {PI}")

# Forma 2: Importar módulo específico del paquete
from mi_paquete import matematicas

print(f"4 * 3 = {matematicas.multiplicar(4, 3)}")
print(f"2^8 = {matematicas.potencia(2, 8)}")

# Forma 3: Importar función específica de módulo específico
from mi_paquete.utilidades import limpiar_texto, es_palindromo, Validador

print(limpiar_texto("  PyThOn   Es   GeNiAl  "))
print(f"¿'reconocer' es palíndromo? {es_palindromo('reconocer')}")
print(f"¿Email válido? {Validador.es_email_valido('test@example.com')}")

# ============================================
# 5. VER LA RUTA DE BÚSQUEDA DE PYTHON
# ============================================

print("\n" + "="*60)
print("5. SISTEMA DE IMPORTACIÓN - sys.path")
print("="*60)

print("Python busca módulos en estos directorios (en orden):")
for i, ruta in enumerate(sys.path, 1):
    print(f"{i}. {ruta}")

# ============================================
# 6. IMPORTAR TODO (*)
# ============================================

print("\n" + "="*60)
print("6. IMPORTAR TODO CON * (no recomendado)")
print("="*60)

# Esto importa todo lo que esté en __all__ del __init__.py
# ADVERTENCIA: Importar con * puede causar conflictos de nombres
from mi_paquete import *

# Ahora puedes usar todo lo exportado
print(f"Suma: {suma(100, 50)}")  # Ya está importado
print(f"Contar palabras: {contar_palabras('uno dos tres')}")


# ============================================
# 7. VERIFICAR __name__
# ============================================

print("\n" + "="*60)
print("7. VERIFICANDO __name__")
print("="*60)

print(f"__name__ de este archivo: {__name__}")
print(f"__name__ de mi_modulo: {mi_modulo.__name__}")
print(f"__name__ de matematicas: {matematicas.__name__}")

print("\nNota: __name__ == '__main__' solo cuando ejecutas el archivo directamente")

# ============================================
# 8. RESUMEN DE BUENAS PRÁCTICAS
# ============================================

print("\n" + "="*60)
print("8. RESUMEN DE BUENAS PRÁCTICAS")
print("="*60)

resumen = """
✅ RECOMENDADO:
   - import modulo
   - from modulo import funcion_especifica
   - import modulo as alias_corto
   
⚠️  USAR CON CUIDADO:
   - from modulo import *  (puede causar conflictos)
   
📝 RECUERDA:
   - Los módulos son archivos .py
   - Los paquetes son carpetas con __init__.py
   - __name__ == "__main__" para detectar ejecución directa
   - sys.path muestra dónde busca Python los módulos
"""

print(resumen)

# ============================================
# PUNTO DE ENTRADA PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("FIN DE LOS APUNTES")
    print("="*60)
    print("\n💡 Ahora prueba ejecutar los otros archivos directamente:")
    print("   python mi_modulo.py")
    print("   python otro_modulo.py")
    print("   python mi_paquete/matematicas.py")