def is_int(s: str) -> bool:
	"""Devuelve True si s representa un entero (opcionalmente con + o -)."""

	if s[0] in '+-':
		s = s[1:]
	return (s.isdigit())


def is_float(s: str) -> bool:
	"""Devuelve True si s representa un float simple (una sola coma decimal)."""
	# Signo
	if s[0] in '+-':
		s = s[1:]
	# Parte Entera y Decimal
	s = s.replace(',', '.')
	parts = s.split('.')
	if len(parts) != 2:
		return (False)
	left, right = parts
	if left == '' and right == '':
		return (False)
	# Al menos un lado debe tener dígitos:
	# .5 -> Valido
	# 5. -> Valido
	# .  -> No valido
	if (left == '' or left.isdigit()) and (right == '' or right.isdigit()):
		return (True)
	return (False)



def is_bool(s: str) -> bool:
	return (s.lower() in ('true', 'false'))


def main():
	print("Introduce valores por teclado. Escribe 'salir' para terminar.")
	# count: diccionario donde 
	# 			- key representa el tipo de dato a comprobar y parsear
	# 			- value: contador con el num. de veces que ese dato ha sido introducido
	counts : dict = {'int': 0, 'float': 0, 'bool': 0, 'str': 0}

	while (True):
		s : str = input('> ').strip()
		if s.lower() == 'salir':
			break
		if s:
			print(f"Entrada: {s}")

			# MODUS
			# is_TdD(s)		-> Comprobar
			# val = TdD(s)	-> Parsear
			# t = 'clave'	-> guardamos key del TdD para acceder a su value
			if is_bool(s):
				if s.lower() == 'true':
					val = True
				else: 
					val = False
				t = 'bool'
			elif is_int(s): 
				val = int(s)
				t = 'int'
			elif is_float(s):
				val = float(s.replace(',', '.'))
				t = 'float'
			else:
				val = s
				t = 'str'

			counts[t] += 1
			print(f"Tipo detectado: {t}")
			print(f"Valor convertido: {val}")

	# Formato de Salida
	print("Has utilizado:")
	print(f"int: {counts['int']}")
	print(f"float: {counts['float']}")
	print(f"bool: {counts['bool']}")
	print(f"str: {counts['str']}")


if __name__ == '__main__':
	main()

