class Planta:
    """
    Clase de atributos b´asicos de una planta
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.altura = 0
        self.agua = 0

    def regar(self):
        self.agua += 1
        
    def crecer(self):
        """Crecimiento en una semana"""
        pass

    def recolectar(self):
        """Lista de furtos que produce"""
        pass

    def __str__(self):
        return f"{self.nombre} ({self.altura} cm.)"

class Tomatera(Planta):
    def __init__(self):
        super().__init__("Tomatera")
    def crecer(self):
        self.altura += self.agua*3
        self.agua = 0
    def recolectar(self):
        if self.altura > 20:
            return ['tomate'] * int(self.altura/10)
        return []
        
class Habas(Planta):
    def __init__(self):
        super().__init__("Habas")
    def crecer(self):
        self.altura += self.agua*5
        self.agua = 0
    def recolectar(self):
        if self.altura > 10:
            return ['habas'] * int(self.altura/5)
        return []

class Huerto:
    """Coleccion sencilla de plantas cultivadas en el huerto"""
    __max_plantas = 10

    def __init__(self):
        self.__plantas = []

    def plantar(self, planta):
        if len(self.__plantas) >= self.__max_plantas:
            print("No hay suelo disponible")
        else:
            self.__plantas.append(planta)

    def regar(self):
        for planta in self.__plantas:
            planta.regar()

    def crecer(self):
        for planta in self.__plantas:
            planta.crecer()

    def recolectar(self):
        cosecha = []
        for planta in self.__plantas:
            cosecha += planta.recolectar()
        return cosecha

    def __str__(self):
        msg = f"Hay {len(self.__plantas)} en el huerto:\n"
        for planta in self.__plantas:
            msg += str(planta) + "\n"
        return msg

if __name__ == "__main__":
    tomatera1 = Tomatera()
    tomatera2 = Tomatera()
    tomatera3 = Tomatera()
    habas1 = Habas()
    habas2 = Habas()

    huerto = Huerto()
    huerto.plantar(tomatera1)
    huerto.plantar(tomatera2)
    huerto.plantar(tomatera3)
    huerto.plantar(habas1)
    huerto.plantar(habas2)

    for _ in range(15):  # cada iteracion es una semana
        #huerto.regar()
        #huerto.crecer()
        tomatera1.regar()

    print(huerto.recolectar())

