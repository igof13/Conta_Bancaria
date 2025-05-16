from datetime import datetime

class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500
        self.numero_saques = 0
        self.LIMITE_SAQUES_DIARIOS = 10
        self.usuarios = {}  # Dicionário para armazenar usuários (CPF como chave)
    
    def _obter_data_hora(self):
        """Retorna a data e hora atual formatada"""
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def _validar_cpf(self, cpf):
        """Valida se o CPF tem 11 dígitos e contém apenas números"""
        return cpf.isdigit() and len(cpf) == 11
    
    def cadastrar_usuario(self):
        print("\n--- CADASTRO DE NOVO USUÁRIO ---")
        cpf = input("Digite o CPF (apenas números, 11 dígitos): ").strip()
        
        # Validação do CPF
        if not self._validar_cpf(cpf):
            print("CPF inválido! Deve conter exatamente 11 dígitos numéricos.")
            return
        
        # Verifica se CPF já existe
        if cpf in self.usuarios:
            print("Erro: CPF já cadastrado no sistema!")
            return
        
        nome = input("Nome completo: ").strip()
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ").strip()
        
        self.usuarios[cpf] = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'endereco': endereco,
            'contas': []  # Lista para armazenar contas vinculadas
        }
        
        print(f"\nUsuário {nome} cadastrado com sucesso!")
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            data_hora = self._obter_data_hora()
            self.extrato.append(f"{data_hora} - Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite_saque
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            self.saldo -= valor
            data_hora = self._obter_data_hora()
            self.extrato.append(f"{data_hora} - Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    def ver_extrato(self):
        print("\n" + "=" * 50)
        print("EXTRATO BANCÁRIO".center(50))
        print("=" * 50)
        
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        
        print("\n" + "-" * 50)
        print(f"Saldo atual: R$ {self.saldo:.2f}".rjust(50))
        print(f"Saques realizados hoje: {self.numero_saques}/{self.LIMITE_SAQUES_DIARIOS}".rjust(50))
        print("=" * 50)
    
    def menu_principal(self):
        menu = """
        [1] Operações Bancárias
        [2] Cadastrar Usuário
        [3] Listar Usuários
        [0] Sair

        => """
        return input(menu)
    
    def menu_operacoes(self):
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [v] Voltar

        => """
        return input(menu)
    
    def listar_usuarios(self):
        print("\n--- USUÁRIOS CADASTRADOS ---")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for cpf, usuario in self.usuarios.items():
                print(f"\nCPF: {cpf}")
                print(f"Nome: {usuario['nome']}")
                print(f"Data Nasc.: {usuario['data_nascimento']}")
                print(f"Endereço: {usuario['endereco']}")
                print(f"Contas vinculadas: {len(usuario['contas'])}")
        print("\n" + "-" * 30)
    
    def executar(self):
        while True:
            opcao = self.menu_principal().strip()
            
            if opcao == "1":  # Menu de operações bancárias
                while True:
                    op = self.menu_operacoes().lower()
                    
                    if op == "d":
                        try:
                            valor = float(input("Informe o valor do depósito: "))
                            self.depositar(valor)
                        except ValueError:
                            print("Valor inválido! Digite um número.")
                    
                    elif op == "s":
                        try:
                            valor = float(input("Informe o valor do saque: "))
                            self.sacar(valor)
                        except ValueError:
                            print("Valor inválido! Digite um número.")
                    
                    elif op == "e":
                        self.ver_extrato()
                    
                    elif op == "v":
                        break
                    
                    else:
                        print("Operação inválida, por favor selecione novamente.")
            
            elif opcao == "2":  # Cadastrar novo usuário
                self.cadastrar_usuario()
            
            elif opcao == "3":  # Listar usuários cadastrados
                self.listar_usuarios()
            
            elif opcao == "0":  # Sair do sistema
                print("Obrigado por usar nosso sistema bancário!")
                break
            
            else:
                print("Operação inválida, por favor selecione novamente.")


if __name__ == "__main__":
    banco = SistemaBancario()
    banco.executar()