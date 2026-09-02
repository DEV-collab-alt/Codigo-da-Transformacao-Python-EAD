
def obter_idade_usuario():
    """
    Pede a idade do usuário e garante que o valor inserido seja um inteiro positivo.
    
    Retorna:
    - int: O valor da idade já validado.
    """
    while True:
        
        valor_digitado = input("Informe a sua idade: ")
        
        try:
            
            idade_informada = int(valor_digitado)
            
            
            if idade_informada <= 0:
                print("Aviso: Por favor, insira um valor numérico estritamente maior que zero.\n")
                continue  
            
            
            return idade_informada

        except ValueError:
           
            print("Aviso: Formato inválido! Insira somente algarismos inteiros.\n")


if __name__ == "__main__":
    print("--- Execução do Teste: Cadastro de Idade ---\n")
    
    
    idade_registrada = obter_idade_usuario()
    
    print(f"\nCadastro concluído! A idade {idade_registrada} foi gravada com sucesso.")