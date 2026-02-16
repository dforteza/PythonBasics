# ============================================================
# EJERCICIO 4: TIENDA ONLINE (ENCAPSULACIÓN + DUNDER METHODS)
# ============================================================
# Clase Producto:
#   - Atributos privados __nombre, __precio, __stock con properties para validación.
#   - Métodos dunder: __str__, __repr__, __eq__ (mismo nombre), __lt__ (precio), __add__ (suma stock si son iguales).
# Clase CarritoCompra:
#   - Contiene una lista de productos.
#   - Métodos dunder: __len__, __getitem__, __contains__, __add__ (combina carritos).
#   - Métodos extra: agregar_producto(), total().
# Practica comparando productos, sumando carritos y listando contenidos.

class Producto:
    def __init__(self, nb, p, stock):
        self.__nombre = nb
        self.__precio = p
        self.__stock = stock
    
    def __str__(self):
        return (f'Nombre = {self.__nombre}, Precio = {self.__precio}, STOCK = {self.__stock}')
    
    def __repr__(self):
        return (f'Producto(Nombre =  {self.__nombre}, Precio = {self.__precio}, STOCK = {self.__stock})')
    
    def __eq__(self, value):
        return (self.__nombre == value.__nombre and self.__precio == value.__precio and self.__stock == value.__stock)
    
    def __lt__(self, value):
        return (self.__precio < value.__precio)
    
    def __add__(self, value):
        return (Producto(self.__nombre, self.__precio, self.__stock + value.__stock))
    
class CarritoCompra:
    def __init__(self):
        self.productos : list = []
    
    def add_product(self, p):
        if p:
            return (self.productos.append(p))

    def __len__(self):
        return (len(self.productos))
    
    def __getitem__(self, p):
        return (self.productos[p])
    
    def __contains__(self, p):
        if (p not in self.productos):
            return (False)
        return (True)
    
    def __add__(self, otro):
        nuevo_carrito = CarritoCompra()
        nuevo_carrito.productos = self.productos + otro.productos
        return nuevo_carrito
    
    def __repr__(self):
        return (f'CarritoCompra(Productos = {self.productos})')
    
tomate = Producto("tomate", 2.99, 50)
peras = Producto("Peras", 1.5, 40)
rabano = Producto("Rabano", 0.99, 80)
lechuga = Producto("lechuga", 1.5, 100)

carrito1 = CarritoCompra()
carrito1.add_product(tomate)
carrito1.add_product(peras)

carrito2 = CarritoCompra()
carrito2.add_product(rabano)
carrito2.add_product(lechuga)

print("CARRITO 1")
print(repr(carrito1))

print("="*20)

print("CARRITO 2")
print("REPR: ",repr(carrito1))
print("LEN: ", len(carrito2))
print("GETITEM: ", repr(carrito2[0])) # rabano
print("CONTAINS rabano :", rabano in carrito2)
print("CARRITO 1 + CARRITO 2", carrito1 + carrito2)


    