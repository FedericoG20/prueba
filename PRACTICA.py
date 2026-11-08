class CuentaBancaria:
    def __init__(self, titular, saldo: 10000):
        self.titular = titular
        self.saldo = saldo

    def Depositar(self, cantidad):
        self.saldo = self.saldo + cantidad
        return f"El saldo total es de {self.saldo}"

    def Retirar(self, cantidad):

        if self.saldo < cantidad:
            return "Saldo insuficiente para realizar la operacion"
        else:
          self.saldo = self.saldo - cantidad
          return f"El saldo toal es de {self.saldo}"
    

retirar = CuentaBancaria("Juan", 10000)

resultado_retirar = retirar.Retirar(1000)

resultado_depositar = retirar.Depositar(10000)


print(resultado_retirar)

print(resultado_depositar)