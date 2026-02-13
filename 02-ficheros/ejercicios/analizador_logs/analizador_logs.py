"""
Analiza un archivo 'servidor.log':
2024-01-15 10:30:15 ERROR Database connection failed
2024-01-15 10:31:00 INFO User login successful
2024-01-15 10:32:45 WARNING High memory usage

Genera un reporte en 'reporte.csv':
Fecha,Hora,Nivel,Mensaje,Contador
2024-01-15,10:30:15,ERROR,1
2024-01-15,10:31:00,INFO,1

Extra: Cuenta errores por tipo y muestra estadísticas
"""
import csv
from pathlib import Path

def main():
    log_path = Path("servidor.log")
    if not log_path.exists():
        print("No se encontró 'servidor.log'")
        return

    filas_csv = []
    contadores = {}

    with log_path.open(mode="r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue

            # Formato esperado: YYYY-MM-DD HH:MM:SS NIVEL Mensaje...
            partes = linea.split(maxsplit=3)
            if len(partes) < 4:
                print(f"Línea ignorada (formato inválido): {linea}")
                continue

            fecha, hora, nivel, mensaje = partes
            contadores[nivel] = contadores.get(nivel, 0) + 1
            filas_csv.append([fecha, hora, nivel, mensaje, contadores[nivel]])

    # Escribir en reporte.csv
    with open("reporte.csv", mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Fecha", "Hora", "Nivel", "Mensaje", "Contador"])
        escritor.writerows(filas_csv)

    # Mostrar estadísticas por nivel
    if contadores:
        print("Resumen por nivel:")
        for nivel, total in contadores.items():
            print(f"  {nivel}: {total}")
    else:
        print("No se procesaron líneas válidas.")

if __name__ == '__main__':
    main()

    