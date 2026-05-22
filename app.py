class ContaBancaria():
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    Para instanciar um objeto da classe temos 3(três) parâmetros:
    OBRIGATÓRIOS:
        -> id
        -> titular
    NÃO OBRIHATÓRIOS:
        -> saldo
    """
    def __init__(self, id, titular, saldo = 0):
        self.id = id
        self.titular = titular
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de {self.saldo:,.2f}")


    def __str__(self):
        return f"\nA conta {self.id} de {self.titular}, tem R${self.saldo:,.2f} de saldo"
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"\nDepósito de R${valor:,.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"\nSaldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"\nSaque de R${valor:,.2f} realizado com sucesso!")


c1 = ContaBancaria(112, "Gustavo", 3000)
c1.depositar(500)
c1.sacar(5000)
print(c1)