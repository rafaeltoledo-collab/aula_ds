class ContaBancaria:
    """
    Exemplo de encapsulamento com métodos get/set tradicionais.
    """
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # O underscore indica que este atributo não deve ser acessado diretamente.
        self._saldo = saldo_inicial
    def get_saldo(self):
        """Método 'getter' para retornar o saldo."""
        print("Acessando o saldo através do get_saldo()...")
        return self._saldo
    def set_saldo(self, novo_valor):
        """
        Método 'setter' para alterar o saldo.
        Ele contém uma regra de negócio para não permitir valores negativos.
        """
        print(f"Tentando alterar o saldo para R$ {novo_valor:.2f}...")
        if novo_valor >= 0:
            self._saldo = novo_valor
            print("Saldo alterado com sucesso!")
        else:
            print("Erro: O saldo não pode ser negativo.")

