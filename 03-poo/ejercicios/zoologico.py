# ============================================================
# EJERCICIO 5: ZOOLÓGICO (CLASES ABSTRACTAS + HERENCIA MÚLTIPLE)
# ============================================================
# Clase abstracta Animal con métodos abstractos hacer_sonido() y moverse(), más presentarse().
# Clases intermedias:
#   - Mamifero(Animal) con atributo tipo_pelaje.
#   - Ave(Animal) con atributo puede_volar.
# Clases concretas: Leon, Aguila, Pinguino (este último no vuela).
# Crea una lista con distintos animales y haz que todos se presenten (polimorfismo).

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    @abstractmethod
    def moverse(self):
        pass
    
    @abstractmethod
    def presentarse(self):
        pass

class Mamifero(Animal):
    def __init__(self, pelaje : str):
        super().__init__()
        self.pelaje = pelaje 

class Ave(Animal):
    def __init__(self, puede_volar : bool):
        super().__init__()
        self.puede_volar = puede_volar 

class Leon(Mamifero):
    def __init__(self, pelaje):
        super().__init__(pelaje)
    
    def hacer_sonido(self):
        return f'El leon hace RAURRRRRRRRR'
    
    def moverse(self):
        return f'El leon se mueve en la sabana'
    
    def presentarse(self):
        return f'Hola soy un Leon y tengo un pelaje {self.pelaje}'

class Aguila(Ave):
    def __init__(self, puede_volar):
        super().__init__(puede_volar)

    def hacer_sonido(self):
        return f'El Aguila hace Iiiiiii'
    
    def moverse(self):
        return f'El aguila se mueve en las montanhas'
    
    def presentarse(self):
        return f'Hola soy un Aguila y {"si" if self.puede_volar else "no"} puedo volar'

class Pinguino(Ave):
    def __init__(self, puede_volar):
        super().__init__(puede_volar)

    def hacer_sonido(self):
        return f'El Pinguino hace AaAaAaAaAaAaAAaA'
    
    def moverse(self):
        return f'El pinguino se mueve en zonas articas'
    
    def presentarse(self):
        return f'Hola soy un Pinguino y {"si" if self.puede_volar else "no"} puedo volar'

# Crear instancias
leon = Leon("dorado")
aguila = Aguila(True)
pinguino = Pinguino(False)

# Lista de animales (polimorfismo)
animales = [leon, aguila, pinguino]

print("=" * 40)
print("ZOOLÓGICO - PRESENTACIONES")
print("=" * 40)

for animal in animales:
    print(animal.presentarse())
    print(animal.hacer_sonido())
    print(animal.moverse())
    print("-" * 40)

