def exercicio_1():
    print("\n--- 1. Lista de Compras ---")
    lista_compras = []
    
    while True:
        print("\n[1] Adicionar item | [2] Remover item | [3] Ver lista | [4] Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            item = input("Digite o nome do item a adicionar: ").strip()
            if item:
                lista_compras.append(item)
                print(f"'{item}' foi adicionado à lista!")
        elif opcao == '2':
            item = input("Digite o nome do item a remover: ").strip()
            if item in lista_compras:
                lista_compras.remove(item)
                print(f"'{item}' foi removido com sucesso!")
            else:
                print("Item não encontrado na lista.")
        elif opcao == '3':
            print("\n--- SUA LISTA DE COMPRAS ---")
            if not lista_compras:
                print("A lista está vazia.")
            else:
                for i, item in enumerate(lista_compras, start=1):
                    print(f"{i}. {item}")
        elif opcao == '4':
            break
        else:
            print("Opção inválida!")

def exercicio_2():
    print("\n--- 2. Dados de um Aluno (Dicionário) ---")
    aluno = {
        "nome": input("Digite o nome do aluno: "),
        "idade": int(input("Digite a idade do aluno: ")),
        "notas": []
    }
    
    qtd_notas = int(input("Quantas notas deseja cadastrar? "))
    for i in range(qtd_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        aluno["notas"].append(nota)
        
    print("\n--- DADOS DO ALUNO CADASTRADO ---")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']} anos")
    print(f"Notas: {aluno['notas']}")
    if aluno['notas']:
        media = sum(aluno['notas']) / len(aluno['notas'])
        print(f"Média: {media:.2f}")

def exercicio_3():
    print("\n--- 3. Pares e Ímpares em um Conjunto de Números ---")
    entrada = input("Digite números separados por espaço (ex: 10 15 22 7 8): ")
    numeros = [int(n) for n in entrada.split()]
    
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    
    print(f"\nNúmeros digitados: {numeros}")
    print(f"Números Pares: {pares}")
    print(f"Números Ímpares: {impares}")

def desafio_extra():
    print("\n--- Desafio Extra: Agenda de Contatos ---")
    agenda = {}
    
    while True:
        print("\n[1] Adicionar/Atualizar | [2] Remover | [3] Buscar | [4] Listar Todos | [5] Voltar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome do contato: ").strip()
            telefone = input("Digite o telefone: ").strip()
            agenda[nome] = telefone
            print(f"Contato '{nome}' salvo com sucesso!")
        elif opcao == '2':
            nome = input("Digite o nome do contato para remover: ").strip()
            if nome in agenda:
                del agenda[nome]
                print(f"Contato '{nome}' removido!")
            else:
                print("Contato não encontrado.")
        elif opcao == '3':
            nome = input("Digite o nome para buscar: ").strip()
            if nome in agenda:
                print(f"Telefone de {nome}: {agenda[nome]}")
            else:
                print("Contato não encontrado na agenda.")
        elif opcao == '4':
            print("\n--- AGENDA DE CONTATOS ---")
            if not agenda:
                print("Agenda vazia.")
            else:
                for nome, tel in agenda.items():
                    print(f"• {nome}: {tel}")
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")


def main():
    while True:
        print("\n=================================")
        print("   ESTRUTURAS DE DADOS - PYTHON  ")
        print("=================================")
        print("1 - Exercício 1: Lista de Compras")
        print("2 - Exercício 2: Dados do Aluno")
        print("3 - Exercício 3: Separar Pares e Ímpares")
        print("4 - Desafio Extra: Agenda de Contatos")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção para executar: ")
        
        if escolha == '1':
            exercicio_1()
        elif escolha == '2':
            exercicio_2()
        elif escolha == '3':
            exercicio_3()
        elif escolha == '4':
            desafio_extra()
        elif escolha == '0':
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
