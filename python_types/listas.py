### ================= LISTAS EN PYTHON ================= ###

# ============ DECLARACIÓN DE LISTAS ============
# 1. Con corchetes []
lista1 = [1, 2, 3, "hola", True]
print(f"Lista con []: {lista1}")

# 2. Con list() - convierte iterable a lista
lista2 = list("hola")  # ['h', 'o', 'l', 'a']
print(f"list('hola'): {lista2}")

# 3. Lista vacía
lista_vacia = []
lista_vacia2 = list()

# ============ MÉTODOS DE LISTAS ============

# --- APPEND ---
# Añade un elemento al final de la lista
# Sintaxis: lista.append(elemento)
l = [1, 2, 3]
l.append(4)
print(f"Después de append(4): {l}")  # [1, 2, 3, 4]

l.append([5, 6])  # Añade la lista entera como un solo elemento
print(f"Después de append([5,6]): {l}")  # [1, 2, 3, 4, [5, 6]]

# --- EXTEND ---
# Añade los elementos de un iterable al final de la lista
# Sintaxis: lista.extend(iterable)
l = [1, 2, 3]
l.extend([4, 5, 6])
print(f"Después de extend([4,5,6]): {l}")  # [1, 2, 3, 4, 5, 6]

l.extend("abc")  # Añade cada carácter
print(f"Después de extend('abc'): {l}")  # [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

# --- INSERT ---
# Inserta un elemento en una posición específica
# Sintaxis: lista.insert(índice, elemento)
l = [1, 2, 3, 4]
l.insert(0, "inicio")  # Inserta al principio
print(f"Después de insert(0, 'inicio'): {l}")  # ['inicio', 1, 2, 3, 4]

l.insert(2, "medio")  # Inserta en posición 2
print(f"Después de insert(2, 'medio'): {l}")  # ['inicio', 1, 'medio', 2, 3, 4]

# --- POP ---
# Elimina y devuelve el elemento en la posición indicada
# Sintaxis: lista.pop([índice])  # Por defecto elimina el último
l = [1, 2, 3, 4, 5]
ultimo = l.pop()  # Sin argumento, elimina el último
print(f"pop() devuelve: {ultimo}, lista: {l}")  # 5, [1, 2, 3, 4]

elemento = l.pop(1)  # Elimina el elemento en índice 1
print(f"pop(1) devuelve: {elemento}, lista: {l}")  # 2, [1, 3, 4]

# --- REMOVE ---
# Elimina la primera aparición del valor especificado
# Sintaxis: lista.remove(valor)
l = ['a', 'b', 'c', 'b', 'd']
l.remove('b')  # Elimina la primera 'b'
print(f"Después de remove('b'): {l}")  # ['a', 'c', 'b', 'd']

# --- CLEAR ---
# Elimina todos los elementos de la lista
# Sintaxis: lista.clear()
l = [1, 2, 3]
l.clear()
print(f"Después de clear(): {l}")  # []

# --- INDEX ---
# Devuelve el índice de la primera aparición de un valor
# Sintaxis: lista.index(valor[, inicio, fin])
l = ['a', 'b', 'c', 'd', 'b']
indice = l.index('b')
print(f"Índice de 'b': {indice}")  # 1

indice2 = l.index('b', 2)  # Busca desde índice 2
print(f"Índice de 'b' desde posición 2: {indice2}")  # 4

# --- COUNT ---
# Cuenta las apariciones de un valor en la lista
# Sintaxis: lista.count(valor)
l = [1, 2, 3, 2, 4, 2, 5]
apariciones = l.count(2)
print(f"Apariciones de 2: {apariciones}")  # 3

# --- SORT ---
# Ordena la lista in-place (modifica la lista original)
# Sintaxis: lista.sort(key=None, reverse=False)
l = [3, 1, 4, 1, 5, 9, 2]
l.sort()
print(f"Después de sort(): {l}")  # [1, 1, 2, 3, 4, 5, 9]

l.sort(reverse=True)  # Orden descendente
print(f"Después de sort(reverse=True): {l}")  # [9, 5, 4, 3, 2, 1, 1]

palabras = ["python", "java", "c", "javascript"]
palabras.sort(key=len)  # Ordena por longitud
print(f"Ordenado por longitud: {palabras}")  # ['c', 'java', 'python', 'javascript']

# --- REVERSE ---
# Invierte el orden de los elementos in-place
# Sintaxis: lista.reverse()
l = [1, 2, 3, 4, 5]
l.reverse()
print(f"Después de reverse(): {l}")  # [5, 4, 3, 2, 1]

# --- COPY ---
# Crea una copia superficial de la lista
# Sintaxis: lista.copy()
l1 = [1, 2, 3]
l2 = l1.copy()  # Crea una nueva lista con los mismos elementos
l2.append(4)
print(f"Original l1: {l1}")  # [1, 2, 3]
print(f"Copia l2: {l2}")    # [1, 2, 3, 4]

# ============ OPERACIONES ADICIONALES ============

# --- CONCATENACIÓN ---
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(f"Concatenación: {lista_c}")  # [1, 2, 3, 4, 5, 6]

# --- REPETICIÓN ---
lista_rep = [1, 2] * 3
print(f"Repetición: {lista_rep}")  # [1, 2, 1, 2, 1, 2]

# --- SLICE (REBANADO) ---
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"l[2:5]: {l[2:5]}")     # [2, 3, 4]
print(f"l[:3]: {l[:3]}")       # [0, 1, 2]
print(f"l[7:]: {l[7:]}")       # [7, 8, 9]
print(f"l[::2]: {l[::2]}")     # [0, 2, 4, 6, 8] (paso 2)
print(f"l[::-1]: {l[::-1]}")   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (invertida)

# --- LONGITUD ---
l = [1, 2, 3, 4, 5]
longitud = len(l)
print(f"Longitud de la lista: {longitud}")  # 5

# --- VERIFICAR EXISTENCIA ---
l = [1, 2, 3, 4, 5]
print(f"3 in l: {3 in l}")         # True
print(f"10 in l: {10 in l}")       # False
print(f"10 not in l: {10 not in l}")  # True

# --- MIN, MAX, SUM ---
numeros = [3, 1, 4, 1, 5, 9, 2]
print(f"min: {min(numeros)}")      # 1
print(f"max: {max(numeros)}")      # 9
print(f"sum: {sum(numeros)}")      # 25

# ============ FUNCIONES ÚTILES ============

# --- SORTED (no modifica la original) ---
l = [3, 1, 4, 1, 5]
l_ordenada = sorted(l)  # Devuelve una nueva lista ordenada
print(f"Original: {l}")           # [3, 1, 4, 1, 5]
print(f"Ordenada: {l_ordenada}")  # [1, 1, 3, 4, 5]

# --- LIST COMPREHENSION ---
# Forma compacta de crear listas
cuadrados = [x**2 for x in range(10)]
print(f"Cuadrados: {cuadrados}")  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

pares = [x for x in range(20) if x % 2 == 0]
print(f"Pares: {pares}")  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# ============ NOTAS IMPORTANTES ============
# - Las listas son mutables (se pueden modificar)
# - Los índices empiezan en 0
# - Índices negativos cuentan desde el final: l[-1] es el último elemento
# - Muchos métodos modifican la lista in-place (no devuelven una nueva lista)
# - append() vs extend(): append añade como un elemento, extend añade cada elemento
# - remove() lanza ValueError si el elemento no existe
# - index() lanza ValueError si el elemento no existe
# - pop() lanza IndexError si el índice está fuera de rango



