### === JSON === ###

import json

print("==== JSON =====")

# DUMP Y LOAD TRABAJAN CON FILE OBJECTS -> POR TANTO REALIZAR OPEN

# SERIALIZAR: convertir OBJ -> JSON
dicc = {"first-name" : "Diego", "last-name" : "Forteza"}

with open(file = "myjson.json", mode = "w", newline = '') as f:
	json.dump(obj = dicc, fp = f, indent = 1)

# DESERAILIZAR: convertir JSON -> OBJ
try:
	with open(file = "doc.json", mode = 'r', newline = '') as f:
		datos = json.load(f)
		print(datos)
except FileNotFoundError:
	print("Archivo no encontrado")

### === CSV === #### === JSON === ###

import json

print("==== JSON =====")

# DUMP Y LOAD TRABAJAN CON FILE OBJECTS -> POR TANTO REALIZAR OPEN

# SERIALIZAR: convertir OBJ -> JSON
dicc = {"first-name" : "Diego", "last-name" : "Forteza"}

with open(file = "myjson.json", mode = "w", newline = '') as f:
	json.dump(obj = dicc, fp = f, indent = 1)

# DESERAILIZAR: convertir JSON -> OBJ
try:
	with open(file = "doc.json", mode = 'r', newline = '') as f:
		datos = json.load(f)
		print(datos)
except FileNotFoundError:
	print("Archivo no encontrado")

### === CSV === ###
import csv

print("==== CSV =====")

# LECTURA

# 1. CSV.READER()
# csv.reader(csvfile, delimiter = ',')
import csv

try:
	with open(file = "datos_escritos.csv", mode = "r", newline='') as f:
		# 1. CREAR READER OBJECT
		datos = csv.reader(f, delimiter = ',')

		# 2. CARGAR CABECERA
		cabecera = next(datos)
		print(cabecera)

		# 3. CARGAR REGISTROS
		for fila in datos:
			print(fila)

except FileNotFoundError:
	print("Error")
print()


# 2. DICT READER
try: 
	with open(file = "datos_escritos.csv", mode = "r", newline='') as f:
		# 1. READER OBJECT
		datos = csv.DictReader(f = f, delimiter = ',')

		# Imprimir cabeceras alineadas
		print(f"{'Nombre':<15} {'Edad':<10} {'Ciudad':<15}")
		print("-" * 40)
        
        # 2. Imprimir cada fila alineada
		for fila in datos:
			print(f"{fila['Nombre']:<15} {fila['Edad']:<10} {fila['Ciudad']:<15}")
except FileNotFoundError:
	print("Error")

## ESCRBIR

# CSV.WRITER()
# 1. CSV.WRITER
try:
	with open("datos_escritos.csv", "w", encoding="utf-8", newline="") as f:
		# 1. WRITER OBJECT
		escritor = csv.writer(f, delimiter=",")
		
		# 2, WRITEROW PARA ESCRIBIR
			# Escribir cabeceras
		escritor.writerow(["Nombre", "Edad", "Ciudad"])
		
			# Escribir datos
		escritor.writerow(["Diego", 30, "Madrid"])
		escritor.writerow(["Ana", 25, "Barcelona"])
except Exception as e:
	print(f"Ocurrió un error al escribir en el archivo: {e}")

# 2. DICT WRITER
try:
	with open("datos_escritos_dict.csv", "w", encoding="utf-8", newline="") as f:
		# 1. WRITER OBJECT
		escritor_dict = csv.DictWriter(f, fieldnames=["Nombre", "Edad", "Ciudad"])
		
		# 2. WRITEHEADER Y WRITEROW
			# Escribir cabeceras
		escritor_dict.writeheader()
		
			# Escribir datos
		escritor_dict.writerow({"Nombre": "Diego", "Edad": 30, "Ciudad": "Madrid"})
		escritor_dict.writerow({"Nombre": "Ana", "Edad": 25, "Ciudad": "Barcelona"})
except Exception as e:
	print(f"Ocurrió un error al escribir en el archivo: {e}")##
import csv

print("==== CSV =====")

# LECTURA

# 1. CSV.READER()
# csv.reader(csvfile, delimiter = ',')
import csv

try:
	with open(file = "datos_escritos.csv", mode = "r", newline='') as f:
		# 1. CREAR READER OBJECT
		datos = csv.reader(f, delimiter = ',')

		# 2. CARGAR CABECERA
		cabecera = next(datos)
		print(cabecera)

		# 3. CARGAR REGISTROS
		for fila in datos:
			print(fila)

except FileNotFoundError:
	print("Error")
print()


# 2. DICT READER
try: 
	with open(file = "datos_escritos.csv", mode = "r", newline='') as f:
		# 1. READER OBJECT
		datos = csv.DictReader(f = f, delimiter = ',')

		# Imprimir cabeceras alineadas
		print(f"{'Nombre':<15} {'Edad':<10} {'Ciudad':<15}")
		print("-" * 40)
        
        # 2. Imprimir cada fila alineada
		for fila in datos:
			print(f"{fila['Nombre']:<15} {fila['Edad']:<10} {fila['Ciudad']:<15}")
except FileNotFoundError:
	print("Error")

## ESCRBIR

# CSV.WRITER()
# 1. CSV.WRITER
try:
	with open("datos_escritos.csv", "w", encoding="utf-8", newline="") as f:
		# 1. WRITER OBJECT
		escritor = csv.writer(f, delimiter=",")
		
		# 2, WRITEROW PARA ESCRIBIR
			# Escribir cabeceras
		escritor.writerow(["Nombre", "Edad", "Ciudad"])
		
			# Escribir datos
		escritor.writerow(["Diego", 30, "Madrid"])
		escritor.writerow(["Ana", 25, "Barcelona"])
except Exception as e:
	print(f"Ocurrió un error al escribir en el archivo: {e}")

# 2. DICT WRITER
try:
	with open("datos_escritos_dict.csv", "w", encoding="utf-8", newline="") as f:
		# 1. WRITER OBJECT
		escritor_dict = csv.DictWriter(f, fieldnames=["Nombre", "Edad", "Ciudad"])
		
		# 2. WRITEHEADER Y WRITEROW
			# Escribir cabeceras
		escritor_dict.writeheader()
		
			# Escribir datos
		escritor_dict.writerow({"Nombre": "Diego", "Edad": 30, "Ciudad": "Madrid"})
		escritor_dict.writerow({"Nombre": "Ana", "Edad": 25, "Ciudad": "Barcelona"})
except Exception as e:
	print(f"Ocurrió un error al escribir en el archivo: {e}")
