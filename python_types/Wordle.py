import secrets

# Emojis
VERDE = "🟩"
NEGRO = "⬛"
NARANJA = "🟨"

# Lista de palabras de 5 letras
PALABRAS = ["casas", "caldo", "cabra", "salud", "perro", "limon", "raton", "bolas", "campe", "carta"]

# Selecciona una palabra aleatoria
palabra_secreta = secrets.choice(PALABRAS).upper()

#Variables del juego
INTENTOS = 5
LONGITUD=5
intentos_realizados = []          

print("Palabra secreta:", palabra_secreta)
print(f"Adivina la palabra secreta. Tienes {INTENTOS} intentos.\n")

# Bucle de intentos
for intento in range(1, INTENTOS + 1):
    FIN=1
    while(FIN!=0):
        palabra = input(f"Intento {intento}: ").strip().upper()
        if len(palabra) != LONGITUD or not palabra.isalpha():
            print(f"La palabra debe tener {LONGITUD} letras y solo letras.\n")
        else:
            FIN=0
   
    resultado = ""
    # Letras para mostrar colores
    for i in range(LONGITUD):
        if palabra[i] == palabra_secreta[i]:
            resultado += VERDE
        elif palabra[i] in palabra_secreta:
            resultado += NARANJA
        else:
            resultado += NEGRO
    print("Resultado:", resultado)
    intentos_realizados.append(resultado)

    if palabra == palabra_secreta:
        print(f"Correcto. Has adivinado la palabra en {intento} intentos.")
        break
else:
    print(f"No lo lograste. La palabra secreta era: {palabra_secreta}")

# Dibujo final con los intentos
print("Dibujo de la partida:\n")
for linea in range(intento):
    print(intentos_realizados[linea])