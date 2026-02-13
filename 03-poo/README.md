# 03 - Programación Orientada a Objetos

Conceptos de POO en Python basados en el paradigma orientado a objetos.

## Contenido

### Apuntes
- `apuntes_poo.py` - Resumen completo de POO con ejemplos:
  - Clases y objetos
  - Métodos de instancia, clase y estáticos
  - Herencia y polimorfismo
  - Encapsulación
  - Clases abstractas
  - Dunder methods

### Ejercicios
- `poo_orientado_musica.py` - Sistema de gestión musical con POO

## Conceptos clave
```python
# Clase básica
class Animal:
    def __init__(self, especie):
        self.especie = especie

# Herencia
class Gato(Animal):
    def hablar(self):
        return "Miau"
```

## Recursos
- [PDF: POO en Python](../recursos/pdfs/POO_Python.pdf)