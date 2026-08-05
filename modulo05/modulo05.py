def saudacao(nome):

    print(f"\nOlá, {nome}! Seja muito bem-vindo(a) ao curso de Python!")

def calcular_media(notas):
    
    if not notas:
        print("Nenhuma nota fornecida.")
        return
    
    media = sum(notas) / len(notas)
    print(f"\nMédia final: {media:.2f}")
    
    if media >= 7.0:
        print("Status: APROVADO(A) 🎉")
    else:
        print("Status: REPROVADO(A) ❌")

def maior_menor(lista_numeros):
    if not lista_numeros:
        return None, None
    return max(lista_numeros), min(lista_numeros)

def validar_login(usuario, senha, usuarios_db):
    if usuario in usuarios_db and usuarios_db[usuario] == senha:
        return True
    return False



def exercicio_1():
    print("\n--- 1. Saudação Personalizada ---")
    nome_user = input("Digite o seu nome: ").strip()
    saudacao(nome_user)

def exercicio_2():
    print("\n--- 2. Calcular Média de Aluno ---")
    qtd = int(input("Quantas notas deseja inserir? "))
    notas = []
    for i in range(qtd):
        n = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(n)
    calcular_media(notas)

def exercicio_3():
    print("\n--- 3. Maior e Menor Valor ---")
    entrada = input("Digite números separados por espaço (ex: 5 12 3 88 1): ")
    numeros = [float(n) for n in entrada.split()]
    
    maior, menor = maior_menor(numeros)
    if maior is not None:
        print(f"Maior valor: {maior}")
        print(f"Menor valor: {menor}")
    else:
        print("Nenhum número foi inserido.")

def desafio_extra():
    print("\n--- Desafio Extra: Sistema de Login ---")
   
    usuarios_cadastrados = {
        "admin": "1234",
        "aluno": "python2026",
        "dev": "senha123"
    }
    
    print("Tentativa de Login:")
    user = input("Usuário: ").strip()
    senha = input("Senha: ").strip()
    
    if validar_login(user, senha, usuarios_cadastrados):
        print(f"\nLogin realizado com sucesso! Bem-vindo, {user}!")
    else:
        print("\nUsuário ou senha incorretos. Acesso negado.")


def main():
    while True:
        print("\n=================================")
        print("       FUNÇÕES EM PYTHON         ")
        print("=================================")
        print("1 - Exercício 1: Saudação Personalizada")
        print("2 - Exercício 2: Calcular Média")
        print("3 - Exercício 3: Maior e Menor Valor")
        print("4 - Desafio Extra: Sistema de Login")
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
            print("Programa encerrado! Bons estudos!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()