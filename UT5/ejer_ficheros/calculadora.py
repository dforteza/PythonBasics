"""
Crea un script que acepte argumentos por línea de comandos:
python calculadora.py --num1 5 --num2 3 --operacion suma

Operaciones: suma, resta, multiplicacion, division
Usa argparse y maneja errores (división por cero, tipos incorrectos)
"""
import argparse

def validar_int(valor: str) -> int:
	try:
		return int(valor)
	except ValueError:
		raise argparse.ArgumentTypeError(f"'{valor}' no es un número entero válido")

def do_op(n1 : int, n2 : int, op : str) -> int:
	res : int = 0
	print(f'{n1} , {n2} , {op}')
	if (op == "suma"):
		res = n1 + n2
	elif (op == "resta"):
		res = n1 - n2
	elif (op == "multiplicacion"):
		res = n1 * n2
	elif (op == "division"):
		try:
			res = n1 // n2
		except ZeroDivisionError:
			print("Eres tonto")
	return (res)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--num1',
					 required=True,
					 type=int,
					 help="numero 1")
	parser.add_argument('--num2',
					 required=True,
					 type=validar_int,
					 help="numero2")
	parser.add_argument("--operacion",
					 required=True,
					 choices=["suma", "resta", "multiplicacion", "division"],
					 help="operacion"
					 )
	args = parser.parse_args()

	print(args.operacion)
	res = do_op(args.num1, args.num2, args.operacion)
	print(res)

if __name__ == '__main__':
	main()