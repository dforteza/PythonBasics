import argparse
import os
from pathlib import Path
from datetime import datetime

def validate_directory(directory_str: str) -> Path:
    """ Valida que el argumento sea un directorio válido.

	Args:
		directory_str (str): Ruta del directorio

	Raises:
		argparse.ArgumentTypeError: Si no es directorio valido

	Returns:
		Path: Directorio validado
	"""
    path = Path(directory_str)

    if not path.exists():
        raise argparse.ArgumentTypeError(f"El directorio '{directory_str}' no existe")
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"'{directory_str}' no es un directorio")
    return path

def log(path: Path, message: str) -> None:
    """Mnesaje para guardar en buscador.log

	Args:
		path (Path): Ruta del archivo a guardar
		message (str): Mensaje a introducir
	"""
    timestamp = datetime.now().isoformat()
    with open(file="buscador.logs", mode="a", encoding="utf-8") as f:
        f.write(f"{timestamp} - {path} - {message}\n")

def buscar(directory: Path, search_arg: str, search_value: str, verbose: bool) -> list:
    """Busca archivos coincidentes con filtro

	Args:
		directory (Path): Ruta del directorio donde comenzar la busqueda
		search_arg (str): Filtro a utilizar || valores: (tipo, nombre, contiene)
		search_value (str): Valor a buscar segun el filtro
		verbose (bool): Si True guardar contenido en buscador.log

	Returns:
		list: Lista con archivos que pasan el filtro
	"""
    results: list = []

    # Ruta absoluta
    path = directory.resolve()

    # Log inicial
    if search_arg and search_value:
        log(path, f"comienza la busqueda de los ficheros {search_value} en {directory}")
    
    # Búsqueda recursiva
    for root, dirs, files in os.walk(directory):
        if verbose:
            log(root, "se accede al directorio")

        for filename in files:
            # Ruta archivo
            file_path = Path(root) / filename

            # Comparar archivo
            encontrado = False
            if search_arg == "tipo":
                if file_path.suffix.lower() == search_value.lower():
                    encontrado = True
            elif search_arg == "nombre":
                if (file_path.name.lower() == search_value.lower() or
                    file_path.stem.lower() == Path(search_value).stem.lower()):
                    encontrado = True
            elif search_arg == "contiene":
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        if search_value.lower() in f.read().lower():
                            encontrado = True
                except (PermissionError, FileNotFoundError, OSError):
                    pass  # Archivo no accesible
            
            if encontrado:
                results.append(file_path)
                log(file_path, f"se ha encontrado {search_value}")
    
    # Log de sin resultados
    if not results:
        log(directory, f"no hay coincidencias {search_value}")

    return results



def main():
    # ArgumentParser
    parser = argparse.ArgumentParser(
        description="Busca ficheros según nombre, extensión o contenido en una ruta especificada"
    )

    # Directorio
    parser.add_argument(
        "directorio",
        type=validate_directory,
        nargs="?",
        default=".",
        help="Directorio donde buscar (por defecto: actual)"
    )
    
    # Argumentos mutuamente excluyentes
    filter_group = parser.add_mutually_exclusive_group(required=True)
    filter_group.add_argument("--tipo", help="Extensión a buscar (ej: .py)")
    filter_group.add_argument("--nombre", help="Nombre del fichero a buscar")
    filter_group.add_argument("--contiene", help="Texto a buscar en ficheros")

    # Verbose
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Registrar recorrido de la búsqueda en fichero logs"
    )
    
    args = parser.parse_args()

    # Determinar tipo de búsqueda
    if args.tipo:
        search_arg, search_value = "tipo", args.tipo
    elif args.nombre:
        search_arg, search_value = "nombre", args.nombre
    else:
        search_arg, search_value = "contiene", args.contiene
    
    results = buscar(args.directorio, search_arg, search_value, args.verbose)
    
    # Mostrar resultados
    if results:
        print(f"\nEncontrados {len(results)} resultado(s):\n")
        for path in results:
            print(path)
    else:
        print("No se encontraron ficheros")




if __name__ == "__main__":
    main()