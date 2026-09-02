def dividir_conta(valor_total, numero_pessoas):
    """
    Função para calcular quanto cada pessoa deve pagar na conta.
    """
    try:
        valor_por_pessoa = valor_total / numero_pessoas
        return f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}"
        
    except ZeroDivisionError:
        return "Erro: O número de pessoas deve ser pelo menos 1!"


print("--- Teste 1: Divisão normal ---")
print(dividir_conta(150.0, 3))

print("\n--- Teste 2: Erro de divisão por zero ---")
print(dividir_conta(150.0, 0))