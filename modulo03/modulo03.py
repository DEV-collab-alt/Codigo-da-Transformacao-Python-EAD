def exercicio_1():
    print("\n--- 1. Operadores Aritméticos ---")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    print(f"Soma (+): {num1 + num2}")
    print(f"Subtração (-): {num1 - num2}")
    print(f"Multiplicação (*): {num1 * num2}")
    print(f"Divisão (/): {num1 / num2 if num2 != 0 else 'Divisão por zero não é permitida'}")
    print(f"Resto da divisão (%): {num1 % num2 if num2 != 0 else 'N/A'}")

def exercicio_2():
    print("\n--- 2. Maior de Dois Números ---")
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    
    if num1 > num2:
        print(f"O maior número é: {num1}")
    elif num2 > num1:
        print(f"O maior número é: {num2}")
    else:
        print("Os dois números são iguais!")

def exercicio_3():
    print("\n--- 3. Classificação de Idade ---")
    idade = int(input("Digite a sua idade: "))
    
    if idade < 0:
        print("Idade inválida!")
    elif idade <= 12:
        print("Categoria: Criança")
    elif idade <= 17:
        print("Categoria: Adolescente")
    elif idade <= 59:
        print("Categoria: Adulto")
    else:
        print("Categoria: Idoso")

def desafio_extra():
    print("\n--- Desafio Extra: Menu Interativo (while) ---")
    while True:
        print("\n--- MENU DO DESAFIO ---")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"Resultado da Soma: {n1 + n2}")
        elif opcao == '2':
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"Resultado da Subtração: {n1 - n2}")
        elif opcao == '3':
            print("Saindo do desafio extra...")
            break
        else:
            print("Opção inválida! Tente novamente.")

 
def main():
    while True:
        print("\n=================================")
        print("   EXERCÍCIOS DE PYTHON - VAD    ")
        print("=================================")
        print("1 - Executar Exercício 1 (Operadores Aritméticos)")
        print("2 - Executar Exercício 2 (Maior Número)")
        print("3 - Executar Exercício 3 (Classificação de Idade)")
        print("4 - Executar Desafio Extra (Menu com while)")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção para testar: ")
        
        if escolha == '1':
            exercicio_1()
        elif escolha == '2':
            exercicio_2()
        elif escolha == '3':
            exercicio_3()
        elif escolha == '4':
            desafio_extra()
        elif escolha == '0':
            print("Encerrando o programa. Bons estudos!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()