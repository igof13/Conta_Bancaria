class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite_saque
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def ver_extrato(self):
        print("\n=============== EXTRATO ===============")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("=======================================")

    def menu(self):
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """
        return input(menu)

    def executar(self):
        while True:
            opcao = self.menu().lower()

            if opcao == "d":
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    self.depositar(valor)
                except ValueError:
                    print("Valor inválido! Digite um número.")

            elif opcao == "s":
                try:
                    valor = float(input("Informe o valor do saque: "))
                    self.sacar(valor)
                except ValueError:
                    print("Valor inválido! Digite um número.")

            elif opcao == "e":
                self.ver_extrato()

            elif opcao == "q":
                print("Obrigado por usar nosso sistema bancário!")
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    banco = SistemaBancario()
    banco.executar()