"""
Crea un gestor de contactos que:
1. Cargue contactos desde 'contactos.json' si existe
2. Permita añadir nuevo contacto (nombre, teléfono, email)
3. Permita buscar por nombre
4. Guarde automáticamente en JSON

Estructura JSON:
[
  {"nombre": "Ana", "telefono": "123456", "email": "ana@email.com"},
  ...
]

Usa argparse para comandos:
python contactos.py --añadir --nombre Ana --telefono 123
python contactos.py --buscar --nombre Ana
"""
import json
import argparse
import os

def cargar_contactos():
    """Carga contactos desde el archivo JSON si existe"""
    if os.path.exists("contactos.json"):
        with open("contactos.json", "r", encoding="utf-8", newline="") as f:
            return (json.load(f))
    return []

def guardar_contactos(contactos):
    """Guarda contactos en el archivo JSON"""
    with open("contactos.json", "w", encoding="utf-8") as f:
        json.dump(contactos, f, indent=2, ensure_ascii=False)
def añadir_contacto(contactos, nombre, telefono, email):
    """Añade un nuevo contacto"""
    nuevo_contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    contactos.append(nuevo_contacto)
    guardar_contactos(contactos)
    print(f"✓ Contacto '{nombre}' añadido correctamente")

def buscar_contacto(contactos, nombre):
    """Busca contactos por nombre"""
    encontrados = [c for c in contactos if nombre.lower() in c["nombre"].lower()]
    
    if encontrados:
        print(f"\nContactos encontrados ({len(encontrados)}):")
        for c in encontrados:
            print(f"  - Nombre: {c['nombre']}")
            print(f"    Teléfono: {c['telefono']}")
            print(f"    Email: {c['email']}")
            print()
    else:
        print(f"No se encontraron contactos con el nombre '{nombre}'")

def main():
    parser = argparse.ArgumentParser(description="Gestor de contactos")
    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponibles")
    
    # Subcomando: añadir
    parser_add = subparsers.add_parser("añadir", help="Añadir un nuevo contacto")
    parser_add.add_argument("--nombre", required=True, help="Nombre del contacto")
    parser_add.add_argument("--telefono", required=True, help="Teléfono del contacto")
    parser_add.add_argument("--email", required=True, help="Email del contacto")
    
    # Subcomando: buscar
    parser_search = subparsers.add_parser("buscar", help="Buscar contacto por nombre")
    parser_search.add_argument("--nombre", required=True, help="Nombre a buscar")
    
    args = parser.parse_args()
    
    # Cargar contactos
    contactos = cargar_contactos()
    
    # Ejecutar comando
    if args.comando == "añadir":
        añadir_contacto(contactos, args.nombre, args.telefono, args.email)
    elif args.comando == "buscar":
        buscar_contacto(contactos, args.nombre)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()