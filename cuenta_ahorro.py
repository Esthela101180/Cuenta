
from cuentas import cuentas

class CuentaAhorros(cuentas):
    def __init__(self, numero, nombre_propietario, saldo, interes):
        super().__init__(numero, nombre_propietario, saldo)
        self.interes = interes

    @property
    def interes(self):
        return self._interes

    @interes.setter
    def interes(self, interes):
        self._interes = interes

    def pagar_interes(self):
        interes_generado = self.saldo * self.interes
        self.credito(interes_generado)

    def mostrar_cuenta(self):
        print("Cuenta de Ahorros:")
        print("Número de cuenta:", self.numero)
        print("Propietario:", self.nombre_propietario)
        self.mostrar_saldo()
print("_______________________________________")
cuenta_ahorros = CuentaAhorros("235901447812", "Luis Rosero Campoverde", 15100.0, 0.0)
cuenta_ahorros.mostrar_cuenta()
cuenta_ahorros.credito(254.55)
cuenta_ahorros.debito(579.98)
cuenta_ahorros.mostrar_cuenta()
cuenta_ahorros.pagar_interes()
cuenta_ahorros.mostrar_cuenta()
print("_______________________________________")