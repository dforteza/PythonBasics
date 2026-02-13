from collections import Counter
import re

# txt = (int)(input("NUMERO : "))

# # if (n % 2 == 0):
# # 	print(f"{n} ES PAR")
# # else:
# # 	print(f"{n} ES IMPAR")

# txt = input("CADENA DE TXT : ")

# if len(txt) in {5, 9, 16}:
# 	print(f"{txt} no se si lo sabes pero ¡ERES MUYYYYYY GUAPO!")

# for i in range(0, 10):
# 	print(f"TABLA DEL {i}")
# 	for j in range(0, 10):
# 		print(f"{j} x {i} = ", end = "")
# 		res = i * j
# 		print(res)
# 	print()

# n = int(input("NUMERO: "))
# res = 1
# for i in range(1, n + 1):
# 	res *= i
# print("EL FACTORIAL DE", n, "ES ", res)

# start = (int)(input("N1 : "))
# end = (int)(input("N2 : "))

# for i in range(start + 1, end):
# 	print(i, end = " ")
# print("\n");

# CUADRADO
# n = (int)(input("N: "))
# cont = 1;
# for i in range(n):
# 	for j in range(n):
# 		print("*", end = " ")
# 	print("\n")

# # PIRÁMIDE EN FORMA DE TRIÁNGULO EQUILÁTERO
# def piramide_triangulo():
#     altura = int(input("Altura de la pirámide: "))
    
#     for i in range(1, altura + 1):
#         espacios = " " * (altura - i)
#         asteriscos = "*" * (2 * i - 1)
        
#         print(espacios + asteriscos)

# # PIRÁMIDE ANGULO RECTO
# def piramide_simple():
#     altura = int(input("Altura de la pirámide simple: "))
    
#     for i in range(1, altura + 1):
#         print("*" * i)

# # Ejecutar las funciones
# print("=== PIRÁMIDE TRIANGULAR ===")
# piramide_triangulo()

# print("\n=== PIRÁMIDE SIMPLE ===")
# piramide_simple()

#leida una lista por teclado di cual es la letra mas repetida

# def count(cadena, letra):
#     cont = 0
#     for i in cadena:
#         if i == letra:
#             cont += 1
#     return (cont)


# cadena = input("cadena: ")
# if cadena:
#     max_letra = ''
#     max_veces = 0
#     for letra in cadena:
#         veces = count(cadena, letra)
#         # print("letra "+letra+" aparece",veces)
#         if veces > max_veces:
#             max_letra = letra
#             max_veces = veces
#     print(f"La letra más repetida es '{max_letra}' ({max_veces} veces)")
# else:
#     print("No se ha introducido ninguna cadena.")

# cadena tiene vocales

# cadena = input("cadena: ")

# def isVocal(i):
#     if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
#         return (1);
#     return (0);

# if cadena:
#     for i in cadena:
#         if isVocal(i) == 1:
#             print("True")
#             break ;

# leer por teclado y añadirlo como clave a un diccionario y lo mismo para valor
# d = {}
# while True:
#     clave = input("Introduzca clave (Enter para terminar): ").strip()
#     if clave == "":
#         break
#     valor = input("Introduce valor: ").strip()
#     d[clave] = valor
#     print(f"Clave '{clave}' añadida con valor '{valor}'\n")
# 1
# print("Diccionario final:", d)

# leer una frase por teclado y cuente cuantas veces aparece cada vocal

# vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
# frase = input("Introducemela: ").lower()
# for c in frase:
#     if c in vocales:
#         vocales[c] += 1
# print("ReEncuento:", vocales)

# num = input("Introducemelo: ")

# d = {
#     "6l": [],
#     "3v": []
# }

# def isVocal(c):
#     if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
#         return (1);
#     return (0);

# def countVocal(word):
#     cont = 0
#     for i in word:
#         if isVocal(i) == 1:
#             cont += 1
#     return (cont)


# print("Introduce palabras")
# while True:
#     word = input("> ").strip()
#     if word == "":
#         break
#     if len(word) == 6 and word not in d["6l"]:
#         d["6l"].append(word)
#     elif countVocal(word) == 3 and word not in d["3v"]:
#         d["3v"].append(word)
# print("Resultado:", d)

colores = ["rojo", "cian", "morado", "verde", "amarillo", "negro"]
for i in range(len(colores)):
	print(i, colores[i])

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
for clave in dict1:
	if clave in dict2:
		dict2[clave] += dict1[clave]
	else:
		dict2[clave] = dict1[clave]
print(dict2)