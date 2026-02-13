# ============================================
# 1. CLASES Y OBJETOS
# ============================================

class Gato:
    """Modelo sencillo de un gato domestico."""

    def __init__(self, nombre, raza, color_pelaje, sexo):
        self.nombre = nombre
        self.raza = raza
        self.color_pelaje = color_pelaje
        self.sexo = sexo

    def maullar(self):
        print(f"{self.nombre} dice: miau")

    def ronronear(self):
        print(f"{self.nombre} ronronea contento")

    def cambiar_pelaje(self, nuevo_color):
        self.color_pelaje = nuevo_color

    def describir(self):
        return (
            f"Gato(nombre={self.nombre}, raza={self.raza}, pelaje={self.color_pelaje}, "
            f"sexo={self.sexo})"
        )


misifu = Gato("Misifu", "comun europeo", "negro", "macho")
misifu.maullar()
misifu.ronronear()
misifu.cambiar_pelaje("atigrado")
print(misifu.describir())


# ============================================
# 2. METODOS DE INSTANCIA VS CLASE
# ============================================

class Calculadora:
    total_calculos = 0

    def __init__(self):
        self.calculos_instancia = 0

    def sumar(self, a, b):
        Calculadora.total_calculos += 1
        self.calculos_instancia += 1
        return a + b

    @classmethod
    def sumar_como_clase(cls, a, b):
        cls.total_calculos += 1
        return a + b

    @staticmethod
    def sumar_estatico(a, b):
        return a + b


calc = Calculadora()
print(Calculadora.sumar_como_clase(2, 3))
print(calc.sumar(5, 7))
print(Calculadora.sumar_estatico(10, 4))
print(f"Total global: {Calculadora.total_calculos} | Instancia: {calc.calculos_instancia}")


# ============================================
# 3. ATRIBUTOS DE CLASE VS INSTANCIA
# ============================================

class Contador:
    cantidad_global = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad_individual = 0

    def incrementar(self):
        Contador.cantidad_global += 1
        self.cantidad_individual += 1


a = Contador("A")
b = Contador("B")
for _ in range(2):
    a.incrementar()
for _ in range(3):
    b.incrementar()
print(
    f"Global={Contador.cantidad_global} | A={a.cantidad_individual} | B={b.cantidad_individual}"
)


# ============================================
# 4. HERENCIA Y POLIMORFISMO
# ============================================


class Animal:
    def __init__(self, especie):
        self.especie = especie

    def hablar(self):
        print(f"Ruido generico de {self.especie}")


class GatoDomestico(Animal):
    def __init__(self, pelaje):
        super().__init__("gato")
        self.pelaje = pelaje

    def hablar(self):
        print("miau")


class Perro(Animal):
    def __init__(self, pelaje):
        super().__init__("perro")
        self.pelaje = pelaje

    def hablar(self):
        print("guau")


animales = [GatoDomestico("blanco"), Perro("negro"), Animal("vaca")]
for animal in animales:
    animal.hablar()


# ============================================
# 5. ENCAPSULACION
# ============================================


class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacio")
        self.__nombre = nuevo_nombre


persona = Persona("Alicia")
print(persona.nombre)
persona.nombre = "Ada"
print(persona.nombre)


# ============================================
# 6. CLASES ABSTRACTAS
# ============================================

from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2


figuras = [Rectangulo(2, 5), Circulo(3)]
for figura in figuras:
    print(f"Area: {figura.area():.2f}")


# ============================================
# 7. DUNDER METHODS
# ============================================


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1)
print(v1 + v2)
print(v1 == Vector(1, 2))
