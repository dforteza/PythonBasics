# ============================================================
# EJERCICIO 1: SISTEMA DE VIDEOJUEGOS (CLASES Y OBJETOS)
# ============================================================
# Crea una clase Personaje con atributos nombre, vida, ataque y defensa.
# Métodos requeridos:
#   - atacar(otro): resta del atributo vida del oponente el daño calculado (ataque - defensa, mínimo 0).
#   - esta_vivo(): devuelve True si la vida es mayor que 0.
#   - curar(cantidad): aumenta la vida sin superar 100.
# Instancia dos personajes y simula turnos de combate hasta que uno muera.

class Personaje:
    def __init__(self, nombre, ataque, defensa):
        self.nombre = nombre
        self.vida = 100
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, otro):
        print(f'{self.nombre} ataca con {self.ataque} a {otro.nombre} que defiende con {otro.defensa}')
        daño = self.ataque - otro.defensa
        if daño < 0:
            daño = 0
        otro.vida -= daño
        if otro.vida < 0:
            otro.vida = 0
        print(f'Vida restante de {otro.nombre}: {otro.vida}')
        if otro.vida == 0:
            print(f"{otro.nombre} ha muerto. FIN DEL COMBATE.")
            return (True)
        return (False)

    def esta_vivo(self) -> bool:
        return (self.vida > 0)

    def curar(self, cantidad):
        if (self.vida + cantidad <= 100):
            self.vida += cantidad
        else:
            self.vida = 100

p1 = Personaje("Pikachu", 40, 30)
p2 = Personaje("Infernate", 50, 20)

print("=========== INICIO DEL COMBATE ==========")
while p1.esta_vivo() and p2.esta_vivo():
    if p1.atacar(p2):
        break
    print("--------")
    if p2.atacar(p1):
        break
    print("--------")
    print("Poción")
    p1.curar(30)
    print(f'Vida de {p1.nombre}: {p1.vida}')
    print(f'Vida de {p2.nombre}: {p2.vida}')
    print("--------")
    

