class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inválido para saque.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo atual: R$ {self.saldo:.2f}")

conta1 = ContaBancaria("Lucas", 1000)

conta1.depositar(500)
conta1.sacar(200)
conta1.mostrar_saldo()
