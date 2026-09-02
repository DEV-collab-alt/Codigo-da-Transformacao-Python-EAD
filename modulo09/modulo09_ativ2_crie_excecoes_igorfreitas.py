
class SaldoIndisponivelException(Exception):
    """
    Exceção disparada quando uma tentativa de retirada 
    excede o montante atual da conta.
    """
    pass


class ContaCorrente:
    def __init__(self, quantia_inicial):
        """
        Cria a conta com o fundo inicial fornecido.
        """
        self.saldo_atual = quantia_inicial

    def realizar_saque(self, montante):
        """
        Executa a debitação do valor se houver fundos suficientes.
        """
        if montante > self.saldo_atual:
            raise SaldoIndisponivelException(
                f"Operação cancelada! Retirada: R$ {montante:.2f} | Saldo atual: R$ {self.saldo_atual:.2f}"
            )
        
        self.saldo_atual -= montante
        return f"Retirada de R$ {montante:.2f} concluída! Novo saldo: R$ {self.saldo_atual:.2f}"


if __name__ == "__main__":
    
    conta_usuario = ContaCorrente(quantia_inicial=100.0)

    print("--- Cenário 1: Saque Válido ---")
    try:
        resultado = conta_usuario.realizar_saque(40.0)
        print(resultado)
    except SaldoIndisponivelException as falha:
        print(f"Aviso: {falha}")

    print("\n--- Cenário 2: Tentativa Sem Fundo ---")
    try:
        resultado = conta_usuario.realizar_saque(100.0)
        print(resultado)
    except SaldoIndisponivelException as falha:
        print(f"Exceção capturada: {falha}")