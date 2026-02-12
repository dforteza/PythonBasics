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
		return (None, False)
	left, right = parts
	if left == '' and right == '':
		return (None, False)
	# Al menos un lado debe tener dígitos:
	# .5 -> Valido
	# 5. -> Valido
	# .  -> No valido
	if (left == '' or left.isdigit()) and (right == '' or right.isdigit()):
		return (s, True)
	return (None, False)

def is_bool(s: str) -> bool:
	return (s.lower() in ('true', 'false'))

def split_top_level(s: str) -> list:
    """
    Divide un string por comas, ignorando aquellas dentro de strings o listas anidadas.
    items:  Contiene TODOS LOS ITEMS SEPARADOS del string
            lista que devolvemos
    current_item:   Sirve para almacenar el item actual de la string
                    APPEND a items si CURRENT_ITEM es VALIDO
    jollyroger: Bandera que sirve para comprobar si se cierran correctamente los corchetes
                [ = +1
                ] = -1
    
                EJs.
                    [] = 0 
                    []] = 1 - 1 - 1 = -1 -> Lista no valida
                    [[[ = 3              -> Lista no valida
                    
    in_string: Bandera que nos indica si estamos en un item string
                Ej. ['Hola , ' , "Mundo"]
                Sirve para DIFERECIAR COMAS(,) INTERNAS que deben ser TRATADAS COMO un CARACTER de
                COMAS EXTERNAS que sirven como DELIMITADOR DE LA LISTA
    string_delimiter:   Almacena delimitador usado en un string interno para saber con
                        delimitador de entrada y cierre de un string
                        ["Hola ' "] -> string_delimiter = "
                        ['Hola " '] -> string_delimiter = '
    """
    items           :   list = []
    current_item    :   list = []
    jollyroger      :   int = 0
    in_string       :   bool = False
    string_delimiter:   str = None
    
    for c in s:
        if in_string:
            # DENTRO de un LITERAL STRING
            current_item.append(c)
            if c == string_delimiter:
                # fin del literal
                in_string = False       # salir de in_string
                string_delimiter = None # limpiar string_delimiter 
        else:
            if c in ('\'', '\"'):
                in_string = True        # entar en in_string
                string_delimiter = c    # actualizar string_delimiter
                current_item.append(c)
            elif c in '([{':            # tupla - lista - diccionario
                jollyroger += 1
                current_item.append(c)
            elif c in ')]}':
                jollyroger -= 1
                if jollyroger < 0:
                     # caso especial: En el momento en el que encuentro 2 ]] Se que esta lista YA NO ES VALIDA
                     return (None);
                current_item.append(c)
            elif c == ',' and jollyroger == 0:  # COMA EXTERNA Y JOLLYROGER = 0 = []
                items.append(''.join(current_item).strip())
                current_item = []       # limpiar current_item
            else:
                current_item.append(c)
    
    # Comprobaciones finales: string sin cerrar o anidamiento no balanceado
    if in_string or jollyroger != 0:
        return (None)
    # Añadir el último elemento si existe
    if current_item:
        items.append(''.join(current_item).strip())
    return (items)

def is_valid_string(item: str) -> bool:
    """
    Verifica si un token es un string literal válido
    Se comprueba:
        - longitud >= 2
            "" => valido
        - mismo delimitador de entrada y cierre 
        - empezar por delimitador correcto

        NOTA:   Estas 2 ultimas comprobaciones ya estan comprobadas 
                gracias a string_delimiter (nos curamos en salud)
    """
    return (len(item) >= 2 and 
            item[0] == item[-1] and # '' o ""
            item[0] in ("\'", "\"")) # empieza por ' o "

def is_valid_element(element: str) -> bool:
    """Verifica si un elemento es válido dentro de una lista, tupla."""
    if not element:
        return True  # Elementos vacíos son válidos
    # String literal
    if is_valid_string(element):
        return (True) 
    # Booleano
    if element.lower() in ('true', 'false'):
        return (True)
    # Número entero
    if is_int(element):
        return (True)
    # Número decimal
    if is_float(element):
        return (True) 
    # Lista anidada
    if element.startswith('[') and element.endswith(']'):
        return (is_list(element)[0])
    return (False)

def is_list(s: str) -> bool:
    """
    Verifica si un string representa una lista válida.

    elements: lista con el str original tal como
    aparecen en el input (no convertidas). Se aceptan claves como literales de string
    ("..." o '...') y valores que `is_valid_element` considere válidos.
    """
    # Verificar delimitadores lista
    if not (s.startswith('[') and s.endswith(']')):
        return (False, None)
    inner_content = s[1:-1].strip() # solo el contenido de la lista
    # Lista vacía: l = []
    if (not inner_content):
        return (True, [])
    # Verificar cada elemento
    elements = split_top_level(inner_content)
    if elements is None:
        return (False, None)
    for element in elements:
        if not is_valid_element(element.strip()):
            return (False, None)
    return (True, elements)

def is_tuple(s: str) -> tuple:
    """
    Verifica si un string representa una tupla válida y devuelve (bool, elements)
    """
    # Verificar delimitadores tupla
    if not (s.startswith('(') and s.endswith(')')):
        return (False, None)
    inner_content = s[1:-1].strip()
    # Tupla vacía: t = ()
    if not inner_content:
        return (True, [])
    elements = split_top_level(inner_content)
    # Verificar cada elemento
    for element in elements:
        if not is_valid_element(element.strip()):
            return (False, None)
    return (True, elements)

def is_dict(s: str) -> tuple:
    """
    Verifica si un string representa un diccionario válido y devuelve (bool, elements)

    elements: lista de tuplas (clave, valor) con las cadenas originales tal como
    aparecen en el input (no convertidas). Se aceptan claves como literales de string
    ("..." o '...') y valores que `is_valid_element` considere válidos.

    pairs:  lista que almacenara todos los item (clave - valor) del diccionario
            si clave y valor son correctos pair.append((key, value))
    """
    pairs: list = [] 

    if not (s.startswith('{') and s.endswith('}')):
        return (False, None)
    inner_content = s[1:-1].strip()
    # Diccionario vacío
    if not inner_content:
        return (True, [])
    # Separar por comas al nivel superior
    items :str = split_top_level(inner_content)
    
    for item in items:
        # Esperamos un par "clave : valor"
        if ':' not in item:
            return (False, None)
        key, value = item.split(':', 1) # el 1 indica que solo se hace 1 split
        # Clave SOLO PUEDE SER literal de string
        if not is_valid_string(key.strip()):
            return (False, None)
        # Valor debe ser un elemento válido según is_valid_element
        if not is_valid_element(value.strip()):
            return (False, None)
        pairs.append((key, value))
    return (True, pairs)

def main():
    print("Introduce valores por teclado. Escribe 'salir' para terminar.")
    counts : dict = {'int' : 0, 'float' : 0, 'str': 0, 'bool' : 0, 'list' : 0, 'tuple' : 0, 'dict' : 0}
    
    while (True): 
        s = input('> ').strip()
        # Condicion de salida
        if s.lower() == 'salir':
            break 
        if s:
            print(f"Entrada: {s}")
            if is_bool(s):
                if s.lower() == 'true':
                    val = True
                else: 
                    val = False
                t = 'bool'
            elif is_int(s):
                val = int(s)
                t = 'int'
            elif is_float(s)[1]:
                val = float(is_float(s)[0])
                t = 'float'
            elif is_list(s)[0]: # is_list[0] = true
                val = is_list(s)[1]
                t = 'list'
            elif is_tuple(s)[0]: # is_tuple[0] = true
                val = tuple(is_tuple(s)[1])
                t = 'tuple'
            elif is_dict(s)[0]: #is_dict[0] = True
                val = dict(is_dict(s)[1])
                t = 'dict'
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
    print(f"list: {counts['list']}")
    print(f"tuple: {counts['tuple']}")
    print(f"dict: {counts['dict']}")
        
if __name__ == '__main__':
	main()


