# 04 - Manejo de Ficheros

Lectura, escritura y manipulación de archivos en Python.

## Contenido

### Ejercicios
- `buscador_ficheros/` - Buscador de archivos en el sistema
- `apts_ficheros.py` - Ejercicios varios con ficheros

## Ejemplos
```python
# Lectura de archivo
with open('archivo.txt', 'r') as f:
    contenido = f.read()

# Escritura
with open('salida.txt', 'w') as f:
    f.write("Hola mundo")
```