"""
Crea un script que:
1. Pida al usuario una frase
2. Cuente cuántas palabras tiene
3. Muestre cada palabra en una línea diferente
4. Guarde las palabras en un archivo 'palabras.txt'

Ejemplo entrada: "Hola mundo Python"
Salida consola: "Tiene 3 palabras:"
                 "Hola"
                 "mundo"  
                 "Python"
Archivo: cada palabra en línea separada
"""
import argparse

def count_words(s : str):
	words = s.split(' ')
	return (words, len(words))

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument("str", 
					 help="Frase",
					 type=str)
	args = parser.parse_args()

	print(type(args.str))
	words, count = count_words(args.str)
	if (words):
		print(f"Tiene {count} palabras")
		for w in words:
			print(w)
		with open(file="words.txt", mode="w", encoding="utf-8") as f:
			for w in words:
				f.write(w + '\n')

if __name__ == '__main__':
	main()

