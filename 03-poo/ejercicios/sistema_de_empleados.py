# ============================================================
# EJERCICIO 6: SISTEMA DE EMPLEADOS (INTEGRADOR)
# ============================================================
# Clase Empleado:
#   - Atributos de clase: cantidad_empleados, salario_minimo.
#   - Atributos de instancia: nombre, __salario (privado), fecha_ingreso.
#   - Property salario (valida salario >= salario_minimo).
#   - Métodos de clase: desde_datos(cls, "nombre,salario,fecha").
#   - Dunder: __str__, __repr__, __eq__ (por nombre), __lt__ (por salario).
# Subclases:
#   - Programador: atributo lenguajes (lista) y método programar().
#   - Gerente: atributo equipo (lista de empleados) y método gestionar_equipo().
# Clase Empresa:
#   - Mantiene una lista de empleados.
#   - Dunder: __len__, __contains__, __getitem__.
#   - Métodos: contratar(), despedir(nombre), empleados_por_salario(), presupuesto_total().
# Implementa la empresa, agrega empleados variados y prueba todas las operaciones.

class Empleado():
    cantidad_empleados = 0
    salario_minimo = 1000
    def __init__(self, nombre: str, salario: int, fecha_ingreso : str):
        self._nombre = nombre
        self.__salario = salario
        self.fecha_ingreso = fecha_ingreso
        Empleado.cantidad_empleados += 1

    @classmethod
    def desde_datos(cls, datos : str):
        nb, salario, fecha = datos.split(",", 2)
        return (cls(nb, int(salario), fecha))
    
    @property
    def nombre(self):
        return (self._nombre)
    
    @property
    def salario(self):
        return (self.__salario)
    
    @salario.setter
    def salario(self, value):
        if value < Empleado.salario_minimo:
            raise ValueError(f"Salario debe ser >= {Empleado.salario_minimo}")
        self.__salario = value

    def __str__(self):
        return f"{self.nombre} - Salario: {self.salario}€ - Ingreso: {self.fecha_ingreso}"

    def __repr__(self):
        return f"Empleado('{self.nombre}', {self.salario}, '{self.fecha_ingreso}')"

    def __eq__(self, value):
        return self.nombre == value.nombre

    def __lt__(self, value):
        return self.salario < value.salario


class Programador(Empleado):
    def __init__(self, nombre, salario, fecha_ingreso):
        super().__init__(nombre, salario, fecha_ingreso)
        self.lenguajes = []

    def programar(self):
        langs = ", ".join(self.lenguajes) if self.lenguajes else "ningún lenguaje"
        return f"{self.nombre} está programando en {langs}"

    def add_lenguajes(self, l):
        self.lenguajes.extend(l)

    def __repr__(self):
        return f"Programador('{self.nombre}', {self.salario}, '{self.fecha_ingreso}')"


class Gerente(Empleado):
    def __init__(self, nombre, salario, fecha_ingreso):
        super().__init__(nombre, salario, fecha_ingreso)
        self.equipo = []

    def gestionar_equipo(self):
        if not self.equipo:
            return f"{self.nombre} no tiene equipo asignado"
        nombres = ", ".join(e.nombre for e in self.equipo)
        return f"{self.nombre} gestiona a: {nombres}"

    def agregar_al_equipo(self, empleado):
        self.equipo.append(empleado)

    def __repr__(self):
        return f"Gerente('{self.nombre}', {self.salario}, '{self.fecha_ingreso}')"


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar(self, empleado):
        self.empleados.append(empleado)

    def despedir(self, nombre):
        for e in self.empleados:
            if e.nombre == nombre:
                self.empleados.remove(e)
                return True
        return False

    def empleados_por_salario(self):
        return sorted(self.empleados, key = (lambda e : e.salario))

    def presupuesto_total(self):
        return sum(e.salario for e in self.empleados)

    def __len__(self):
        return len(self.empleados)

    def __contains__(self, empleado):
        return empleado in self.empleados

    def __getitem__(self, index):
        return self.empleados[index]

    def __repr__(self):
        return f"Empresa('{self.nombre}', empleados={len(self)})"


# ============== PRUEBAS ==============
if __name__ == "__main__":
    # Crear empresa
    empresa = Empresa("TechCorp")

    # Crear empleados
    prog1 = Programador("Ana", 2500, "2023-01-15")
    prog1.add_lenguajes(["Python", "JavaScript"])

    prog2 = Programador("Luis", 2200, "2024-03-01")
    prog2.add_lenguajes(["Java"])

    gerente = Gerente("Carlos", 4000, "2020-06-10")
    gerente.agregar_al_equipo(prog1)
    gerente.agregar_al_equipo(prog2)

    # Contratar
    empresa.contratar(prog1)
    empresa.contratar(prog2)
    empresa.contratar(gerente)

    # Probar dunder methods
    print(f"Total empleados: {len(empresa)}")          # __len__
    print(f"Ana en empresa: {prog1 in empresa}")       # __contains__
    print(f"Primer empleado: {empresa[0]}")            # __getitem__
    print(repr(empresa))                                # __repr__

    # Métodos de negocio
    print(f"\nPresupuesto total: {empresa.presupuesto_total()}€")
    print("\nEmpleados por salario:")
    for e in empresa.empleados_por_salario():
        print(f"  {e}")

    # Métodos específicos
    print(f"\n{prog1.programar()}")
    print(gerente.gestionar_equipo())


