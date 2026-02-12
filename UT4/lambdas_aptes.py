personas = {
"maria": {"edad": 23},
"lope": {"edad": 22}
}
orden_edad = sorted(personas.items(), key=lambda x: x[1]["edad"])
print(orden_edad)