from sys import argv

# 1 FACTORIAL DE UN NUMERO

def recursive_factorial(n : int) -> int:
	if n == 0:
		return (1)
	return (n * recursive_factorial(n - 1))

# 2 SUMA DE LOS PRIMEROS N NUMEROS

def recursive_suma_gauss(n : int) -> int:
	if n == 1:
		return (1)
	return (n + recursive_suma_gauss(n - 1))

# 3 CONTAR DIGITOS DE UN NUMERO

def recursive_count_digits_simple(n : int) -> int:
	"""Recursión directa: cada nivel suma 1.

	Base: si abs(n) < 10 -> 1 (tratamos 0 como 1 dígito).
	Paso: 1 + recursive_count_digits_simple(n // 10)
	"""
	n = abs(int(n))
	if n < 10: return 1
	return (1 + recursive_count_digits_simple(n // 10))

# print(recursive_count_digits_simple(argv[1]))


def recursive_count_digits_tail(n : int, cont: int = 0) -> int:
	"""Recursión estilo 'tail' usando un acumulador cont.

	Llamar con cont=0 normalmente. Devuelve cont+1 para n==0.
	"""
	n = abs(int(n))
	if n < 10:
		return cont + 1
	return recursive_count_digits_tail(n // 10, cont + 1)

# 4 POTENCIA

def recursive_power(x : int, y : int) -> int:
	if y == 0:
		return (1)
	return (x * recursive_power(x, y - 1))


# 5 IMPRIMIR LOS NUMEROS DEL 1 AL N

def	recursive_print_n_numbers(n : int) -> int:
	if n <= 0:
		return

	def asc(k: int) -> None:
		if k == 0:
			return
		asc(k - 1)
		print(k, end=" ")

	def desc(k: int) -> None:
		if k == 0:
			return
		print(k, end=" ")
		desc(k - 1)

	asc(n)       
	desc(n - 1)  
	print()  


# 6 INVERTIR UNA CADENA

def recursive_invert_s_simple(s: str) -> str:
	"""Opción A: recursión directa.

	Base: si len(s) <= 1 -> devolver s.
	Paso: devolver last_char + recursive_invert_s_simple(s[:-1]).
	Coste: tiempo O(n^2) debido a concatenaciones sucesivas, memoria O(n) por la profundidad de la pila.
	"""
	s = str(s)
	if len(s) <= 1:
		return s
	return (s[-1] + recursive_invert_s_simple(s[:-1]))


def recursive_invert_s_tail(s: str, acc: list = None) -> str:
	"""Opción B: tail-recursive con acumulador (lista) para evitar concatenaciones.

	Se extrae el último carácter y se añade a acc; al final se hace join.
	Coste: tiempo O(n), memoria O(n) (lista + profundidad de pila).
	"""
	s = str(s)
	# Primera llamada
	if acc is None:
		acc = []
	# Ultima llamada
	if s == "":
		return (''.join(acc))
	# añadir el último carácter al acumulador
	acc.append(s[-1])
	return recursive_invert_s_tail(s[:-1], acc)


# 7 COMPROBAR SI UNA CADENA ES PALINDROMO

def recursive_palindromo(s : str) -> bool:
	s = s.lower()
	if (len(s) < 2):
		return (True)
	if not (s[0] == s[-1]):
		return (False)
	return (recursive_palindromo(s[1:-1]))

# 8 SUMA DE ELEMENTOS EN UNA ESTRUCTURA ANIDADA
# f([1, [2, [3], 2], 1]) -> 37 => 1 + 4 + 27 + 4 + 1
# 1
# 2 

lista = [1, [2, [3], 2], 1]

def nesting_sum(lista: list, nesting: int = 1) -> int:
	suma : int = 0

	if len(lista) == 0:
		return (0)
	
	for e in lista:
		if type(e) == int:
			# print(f'Entro con {e} con nesting {nesting} = {e ** nesting}')
			suma += e ** nesting
		else:
			suma += nesting_sum(e, nesting + 1)
	return (suma)

print(nesting_sum(lista))

# 9 FILTRAR NUMEROS PARES

def es_divisor(x : int, lista: list) -> bool:
	suma = sum(lista)
	if suma % x == 0:
		return (True)
	else:
		return (False)

# lista = [1, 2, 3, 4]
# print(list(filter(lambda x : es_divisor(x, lista), lista)))

# 10 ORDENAR UNA LISTA DE DICCIONARIOS
personas = [
{"nombre": "Ana", "edad": 25},
{"nombre": "Luis", "edad": 30},
{"nombre": "Marta", "edad": 20}
]

# personas_sorted = sorted(personas,
# 						 key= lambda x : x.get("edad"),
# 						 reverse= False)

# for persona in personas_sorted:
# 	print(persona.get("nombre"))
