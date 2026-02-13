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
            
    def regar_uno(self, planta):
        planta.regar()

    def crecer(self):
        for planta in self.__plantas:
            planta.crecer()

    def recolectar(self):
        cosecha = []
        for planta in self.__plantas:
            cosecha += planta.recolectar()
        return cosecha
    

    # 6. Implementa un metodo de clase en Huerto que se llamen resumen(cosecha) que muestre
    # cuantos frutos de cada tipo se han recolectado tomando como argumento el resultado de
    # huerto.recolectar()
    @classmethod
    def resumen(cls, cosecha):
        t : int = 0
        h : int = 0
        for planta in cosecha:
            if planta == "tomate":
                t += 1
            elif planta == "habas":
                h += 1
            else:
                continue
        
        print("="*30)
        print(f"{"ESTADISTICAS":^30}")
        print("="*30)
        
        print(f'Tomateras recolectadas: {t} ')
        print(f'Habas recolectadas: {h} ')
    
    def __getitem__(self, item):
        return (self.__plantas[item])

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
        # tomatera1.regar()   # riego extra
        huerto.regar()
        huerto.crecer()

    cosecha = huerto.recolectar()
    print(cosecha)

    # 6
    Huerto.resumen(cosecha)

print("="*30)
print(f"{"PREGUNTAS EXTRA":^30}")
print("="*30)
# # 1. ¿Que ocurre si invocamos tomatera1.regar() dentro del bucle?
#       Esa planta recibiría dos riegos en 
#       cada iteración: uno por la llamada explícita y otro por 
#       el riego general del huerto.


# # 2. ¿Los objetos dentro del objeto huerto pueden modificarse independientemente?
#     Si. Cada planta es un objeto distinto; 
#     puedes modificar uno sin tocar los demás:

tomatera1.altura = 50
print(f'Tomatera1 altura => {tomatera1.altura}') # 50


# # 3. ¿Que ocurrir´a si añadimos lineas adicionales de huerto.regar()?
#     Añadir más llamadas a huerto.regar() simplemente repetirá el ciclo 
#     de riego completo tantas veces como las invoques, incrementando la hidratación 
#     (o cualquier efecto asociado) de todas las plantas cada vez.


# # 4. ¿Puedes acceder a la primera planta del huerto con huerto. plantas[0]?
#     No, a menos que la clase Huerto implemente __getitem__, la expresión 
#     huerto.plantas[0] no funcionará directamente. Necesitas un método 
#     específico (por ejemplo, huerto.obtener_planta(0)) o exponer la lista de 
#     forma controlada.

print(f'1º hueco del huerto => {huerto[0]}') # tomatera1

# # 5. ¿Puedes acceder a tomatera1.altura?
        # Si al ser un atributo publico
tomatera1.altura += 10
print(f'Tomatera1 altura => {tomatera1.altura}')

