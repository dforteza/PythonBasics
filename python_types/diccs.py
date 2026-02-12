### ================= DICCIONARIOS EN PYTHON ================= ###

# ============ DECLARACIÓN DE DICCIONARIOS ============
# 1. Con llaves {} y dos puntos :
dicc1 = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
dicc2 = {1: "uno", 2: "dos", 3: "tres"}  # Las claves pueden ser números
dicc3 = {"a": 1, "b": 2, "c": 3}
print(f"Diccionario con {{}}: {dicc1}")

# 2. Con dict() y signos igual =
dicc4 = dict(nombre="Ana", edad=30, ciudad="Barcelona")
print(f"Diccionario con dict(): {dicc4}")

# 3. Con dict() desde lista de tuplas
dicc5 = dict([("x", 1), ("y", 2), ("z", 3)])
print(f"Desde tuplas: {dicc5}")

# 4. Diccionario vacío
dicc_vacio = {}
dicc_vacio2 = dict()

# 5. Con valores por defecto usando dict.fromkeys()
dicc6 = dict.fromkeys(["a", "b", "c"], 0)
print(f"Con fromkeys(): {dicc6}")  # {'a': 0, 'b': 0, 'c': 0}

# ============ ACCESO A VALORES ============

# --- ACCESO CON [] ---
# Lanza KeyError si la clave no existe
d = {"nombre": "Pedro", "edad": 28}
print(f"d['nombre']: {d['nombre']}")  # 'Pedro'

try:
    valor = d["ciudad"]  # Esta clave no existe
except KeyError:
    print("Error: La clave 'ciudad' no existe")

# --- ACCESO CON GET ---
# ¡¡¡ MÁS SEGURO !!! Devuelve None si la clave no existe
d = {"nombre": "María", "edad": 22}
print(f"get('nombre'): {d.get('nombre')}")  # 'María'
print(f"get('ciudad'): {d.get('ciudad')}")  # None

# Puedes especificar un valor por defecto
print(f"get('ciudad', 'Desconocida'): {d.get('ciudad', 'Desconocida')}")  # 'Desconocida'

# Verificar si existe antes de acceder
if d.get("edad") is not None:
    print(f"La edad existe: {d.get('edad')}")

# ============ AÑADIR Y MODIFICAR VALORES ============

# --- AÑADIR/MODIFICAR CON [] ---
d = {"nombre": "Luis"}
d["edad"] = 35  # Añade nueva clave-valor
print(f"Después de añadir 'edad': {d}")  # {'nombre': 'Luis', 'edad': 35}

d["nombre"] = "Luis García"  # Modifica valor existente
print(f"Después de modificar 'nombre': {d}")  # {'nombre': 'Luis García', 'edad': 35}

# --- UPDATE ---
# Actualiza el diccionario con pares clave-valor de otro diccionario
# Sintaxis: diccionario.update(otro_diccionario)
d = {"a": 1, "b": 2}
d.update({"b": 20, "c": 3})  # Modifica 'b' y añade 'c'
print(f"Después de update(): {d}")  # {'a': 1, 'b': 20, 'c': 3}

# También acepta argumentos con nombre
d.update(d=4, e=5)
print(f"update con kwargs: {d}")  # {'a': 1, 'b': 20, 'c': 3, 'd': 4, 'e': 5}

# --- SETDEFAULT ---
# Devuelve el valor de una clave. Si no existe, la añade con un valor por defecto
# Sintaxis: diccionario.setdefault(clave, valor_por_defecto)
d = {"nombre": "Ana"}
edad = d.setdefault("edad", 25)  # 'edad' no existe, se añade con valor 25
print(f"setdefault('edad', 25): {edad}, diccionario: {d}")  # 25, {'nombre': 'Ana', 'edad': 25}

nombre = d.setdefault("nombre", "Desconocido")  # 'nombre' existe, devuelve su valor
print(f"setdefault('nombre', 'Desconocido'): {nombre}")  # 'Ana'

# ============ ELIMINAR VALORES ============

# --- DEL ---
# Elimina una clave-valor. Lanza KeyError si no existe
d = {"a": 1, "b": 2, "c": 3}
del d["b"]
print(f"Después de del d['b']: {d}")  # {'a': 1, 'c': 3}

try:
    del d["z"]  # Esta clave no existe
except KeyError:
    print("Error: No se puede eliminar 'z', no existe")

# --- POP ---
# Elimina una clave y devuelve su valor. Lanza KeyError si no existe (sin valor por defecto)
# Sintaxis: diccionario.pop(clave[, valor_por_defecto])
d = {"x": 10, "y": 20, "z": 30}
valor = d.pop("y")
print(f"pop('y') devuelve: {valor}, diccionario: {d}")  # 20, {'x': 10, 'z': 30}

# Con valor por defecto (no lanza error si no existe)
valor = d.pop("w", "No existe")
print(f"pop('w', 'No existe') devuelve: {valor}")  # 'No existe'

# --- POPITEM ---
# Elimina y devuelve el último par clave-valor insertado (desde Python 3.7+)
# Sintaxis: diccionario.popitem()
d = {"a": 1, "b": 2, "c": 3}
par = d.popitem()
print(f"popitem() devuelve: {par}, diccionario: {d}")  # ('c', 3), {'a': 1, 'b': 2}

# --- CLEAR ---
# Elimina todos los elementos del diccionario
# Sintaxis: diccionario.clear()
d = {"a": 1, "b": 2}
d.clear()
print(f"Después de clear(): {d}")  # {}

# ============ MÉTODOS DE CONSULTA ============

# --- KEYS ---
# Devuelve una vista de todas las claves
# Sintaxis: diccionario.keys()
d = {"nombre": "Carlos", "edad": 30, "ciudad": "Valencia"}
claves = d.keys()
print(f"keys(): {claves}")  # dict_keys(['nombre', 'edad', 'ciudad'])
print(f"Lista de claves: {list(claves)}")  # ['nombre', 'edad', 'ciudad']

# --- VALUES ---
# Devuelve una vista de todos los valores
# Sintaxis: diccionario.values()
valores = d.values()
print(f"values(): {valores}")  # dict_values(['Carlos', 30, 'Valencia'])
print(f"Lista de valores: {list(valores)}")  # ['Carlos', 30, 'Valencia']

# --- ITEMS ---
# Devuelve una vista de todos los pares clave-valor como tuplas
# Sintaxis: diccionario.items()
items = d.items()
print(f"items(): {items}")  # dict_items([('nombre', 'Carlos'), ('edad', 30), ('ciudad', 'Valencia')])
print(f"Lista de items: {list(items)}")  # [('nombre', 'Carlos'), ('edad', 30), ('ciudad', 'Valencia')]

# ============ RECORRER DICCIONARIOS ============

d = {"a": 1, "b": 2, "c": 3}

# --- RECORRER SOLO CLAVES ---
print("Recorriendo claves:")
for clave in d:  # Por defecto itera sobre las claves
    print(f"  Clave: {clave}")

# Equivalente explícito:
for clave in d.keys():
    print(f"  Clave: {clave}")

# --- RECORRER SOLO VALORES ---
print("Recorriendo valores:")
for valor in d.values():
    print(f"  Valor: {valor}")

# --- RECORRER CLAVES Y VALORES ---
print("Recorriendo claves y valores:")
for clave, valor in d.items():
    print(f"  {clave}: {valor}")

# ============ OPERACIONES ADICIONALES ============

# --- VERIFICAR EXISTENCIA DE CLAVE ---
d = {"nombre": "Elena", "edad": 27}
print(f"'nombre' in d: {'nombre' in d}")  # True
print(f"'ciudad' in d: {'ciudad' in d}")  # False
print(f"'ciudad' not in d: {'ciudad' not in d}")  # True

# --- LONGITUD ---
d = {"a": 1, "b": 2, "c": 3}
print(f"len(d): {len(d)}")  # 3

# --- COPY ---
# Crea una copia superficial del diccionario
# Sintaxis: diccionario.copy()
d1 = {"a": 1, "b": 2}
d2 = d1.copy()
d2["c"] = 3
print(f"Original d1: {d1}")  # {'a': 1, 'b': 2}
print(f"Copia d2: {d2}")     # {'a': 1, 'b': 2, 'c': 3}

# --- FUSIONAR DICCIONARIOS (Python 3.9+) ---
# Usando el operador |
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = d1 | d2
print(f"d1 | d2: {d3}")  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# --- COMPRENSIÓN DE DICCIONARIOS ---
# Forma compacta de crear diccionarios
cuadrados = {x: x**2 for x in range(5)}
print(f"Cuadrados: {cuadrados}")  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Con condición
pares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Cuadrados de pares: {pares}")  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Invertir claves y valores
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print(f"Invertido: {invertido}")  # {1: 'a', 2: 'b', 3: 'c'}

# ============ DICCIONARIOS ANIDADOS ============

# Diccionarios dentro de diccionarios
estudiantes = {
    "estudiante1": {"nombre": "Ana", "edad": 20, "notas": [8, 9, 7]},
    "estudiante2": {"nombre": "Luis", "edad": 22, "notas": [7, 8, 8]},
    "estudiante3": {"nombre": "María", "edad": 21, "notas": [9, 9, 10]}
}

# Acceso a valores anidados
print(f"Nombre del estudiante1: {estudiantes['estudiante1']['nombre']}")  # 'Ana'
print(f"Primera nota de estudiante2: {estudiantes['estudiante2']['notas'][0]}")  # 7

# Recorrer diccionario anidado
for id_estudiante, datos in estudiantes.items():
    print(f"{id_estudiante}: {datos['nombre']}, Edad: {datos['edad']}")

# ============ FUNCIONES ÚTILES ============

# --- SORTED ---
# Ordenar claves o valores
d = {"c": 3, "a": 1, "b": 2}
claves_ordenadas = sorted(d.keys())
print(f"Claves ordenadas: {claves_ordenadas}")  # ['a', 'b', 'c']

# Crear nuevo diccionario ordenado por claves
d_ordenado = {k: d[k] for k in sorted(d.keys())}
print(f"Diccionario ordenado: {d_ordenado}")  # {'a': 1, 'b': 2, 'c': 3}

# Ordenar por valores
d = {"a": 3, "b": 1, "c": 2}
ordenado_por_valor = dict(sorted(d.items(), key=lambda item: item[1]))
print(f"Ordenado por valor: {ordenado_por_valor}")  # {'b': 1, 'c': 2, 'a': 3}

# --- MAX, MIN ---
d = {"a": 10, "b": 5, "c": 15}
clave_max = max(d, key=d.get)  # Clave con valor máximo
clave_min = min(d, key=d.get)  # Clave con valor mínimo
print(f"Clave con valor máximo: {clave_max}")  # 'c'
print(f"Clave con valor mínimo: {clave_min}")  # 'b'

# ============ NOTAS IMPORTANTES ============
# - Los diccionarios son mutables (se pueden modificar)
# - Las claves deben ser inmutables (strings, números, tuplas)
# - Las claves son únicas (no puede haber claves duplicadas)
# - Desde Python 3.7+, los diccionarios mantienen el orden de inserción
# - get() es más seguro que [] para acceder a claves que pueden no existir
# - Las vistas (keys(), values(), items()) se actualizan dinámicamente
# - setdefault() es útil para inicializar valores la primera vez
# - update() modifica el diccionario original (no devuelve uno nuevo)
# - pop() requiere al menos un argumento (la clave); popitem() no requiere argumentos
# - in verifica existencia de CLAVES, no de valores
# - Para verificar si existe un valor: valor in diccionario.values()