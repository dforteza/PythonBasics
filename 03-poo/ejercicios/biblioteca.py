# ============================================================
# EJERCICIO 2: BIBLIOTECA (MÉTODOS DE CLASE)
# ============================================================
# Clase Libro:
#   - Atributos de clase: total_libros, libros_prestados.
#   - Atributos de instancia: titulo, autor, prestado (bool).
#   - Métodos de instancia: prestar(), devolver().
#   - Métodos de clase:
#       * crear_desde_string(cls, "Titulo|Autor") -> devuelve un Libro.
#       * estadisticas(cls) -> imprime total y prestados.
# Crea varios libros, usa prestar/devolver y muestra las estadísticas.

class Libro:
    total_libros = 0
    libros_prestados = 0

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
    
    def prestar(self):
        self.prestado = True
        Libro.libros_prestados += 1
        Libro.total_libros -= 1

    def devolver(self):
        if self.prestado:
            self.prestado = False
            Libro.total_libros += 1
            Libro.libros_prestados -= 1
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")
    
    @classmethod
    def crear_desde_string(cls, cadena : str) -> object:
        titulo, autor = cadena.split("|", 1)
        libro = cls(titulo, autor)
        Libro.total_libros += 1
        return libro

    @classmethod
    def estadisticas(cls):
        print(f"Total libros: {cls.total_libros} | Libros prestados: {cls.libros_prestados}")

libro1 = Libro.crear_desde_string("El Quijote|Cervantes")
libro2 = Libro.crear_desde_string("1984|Orwell")
libro3 = Libro.crear_desde_string("Cien años de soledad|García Márquez")

Libro.estadisticas()
libro1.prestar()
libro2.prestar()
Libro.estadisticas()
libro1.devolver()
Libro.estadisticas()
    