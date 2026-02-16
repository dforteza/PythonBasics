# ============================================================
# EJERCICIO 3: SISTEMA BANCARIO (HERENCIA Y POLIMORFISMO)
# ============================================================
# Clase base CuentaBancaria con atributos titular y saldo, métodos depositar(), retirar(), mostrar_saldo().
# Clases hijas:
#   - CuentaAhorro: atributo interes_anual y método aplicar_interes().
#   - CuentaCorriente: atributo limite_sobregiro y retirar() permite saldo negativo hasta el límite.
# Crea instancias de ambos tipos, guárdalas en una lista y demuestra polimorfismo llamando a métodos comunes.

class CuentaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, n):
        self.saldo += n
    
    def retirar(self, n):
        if (self.saldo - n >= 0):
            self.saldo -= n
    
    def mostrar_saldo(self):
        print(f'TITULAR ({self.titular}) | SALDO ({self.saldo})')

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes_anual):
        super().__init__(titular, saldo)
        self.interes_anual = interes_anual

    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes_anual

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo, limite_sobregiro):
        super().__init__(titular, saldo)
        self.limite = limite_sobregiro
    
    def retirar(self, n):
        if (self.saldo - n >= self.limite):
            self.saldo -= n

cuentas = [
    CuentaAhorro("Ana", 1000, 0.05),
    CuentaCorriente("Luis", 500, -200)
]

for cuenta in cuentas:
    cuenta.depositar(100)
    cuenta.retirar(200)
    cuenta.mostrar_saldo()
