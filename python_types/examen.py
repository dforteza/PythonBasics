# Ejercicio 1

# n : str = input('Introduce n:')

# if not n.isdigit():
# 	print("Error")

# n = (int)(n)

# while n >= 1:
# 	h = n
# 	while h >= 1:
# 		print(h, end = "")
# 		h -= 1
# 	print()
# 	n -= 1n : str = input('Introduce n:')

# if not n.isdigit():
# 	print("Error")

# n = (int)(n)

# while n >= 1:
# 	h = n
# 	while h >= 1:
# 		print(h, end = "")
# 		h -= 1
# 	print()
# 	n -= 1

# Ejercicio 2

# def isInt(s: str) -> bool:
# 	"""Devuelve True si s representa un entero (opcionalmente con + o -)."""

# 	if s[0] in '+-':
# 		s = s[1:]
# 	return (s.isdigit())

# res = 0
# cont = 0
# while res <= 42:
# 	n = input('> ')
# 	if isInt(n):
# 		n = (int)(n)
# 		print(n)
# 		res += n
# 	cont += 1

# print(f"Necesitaste {cont} para llegar a {res}")

# # # Ejercicio 3
# # Partiendo de palabra = "palabra" y palabra_dict = {"p": 1, "a": 3, "l": 1,
# # "b": 1, "r": 1}, se debe leer por teclado una palabra y decir que le falta, que sobra
# # o que letras no están en la palabra "palabra"

# palabra = "patata"
# palabra_dict = {"p": 1, "a": 3, "l": 1, "b": 1, "r": 1}
# palabra_dict2 = {"p": 0, "a": 0, "l": 0, "b": 0, "r": 0}
# lista = []

# for p in palabra:
# 	if p in palabra_dict:
# 		palabra_dict2[p] += 1
# 	else:
# 		lista.append(p)

# for i in lista:
# 	print(f'La palabra {i} no esta en la lista')

# for p in palabra_dict2:
# 	if palabra_dict2[p] == 0:
# 		print(f'Faltan {palabra_dict[p] - palabra_dict2[p]} palabras {p}')

# Ejercicio 4

