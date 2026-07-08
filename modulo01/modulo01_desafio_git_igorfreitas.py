'''
>PO (Como dono do negocio: Quero um sistema de agendamento de horários para cortar o cabelo, fazer a barba e
sombrancelha de meus clientes, diferenciando cada um dos pedidos e armazenando seus dados.)<

>QA (Como cliente: Quero um sistema de agendamento de horários, para que eu possa agendar meus horários
disponíveis de forma rápida e fácil)<
 
 >Tech (Como programador: Quero um sistema de agendamento de horários para minha barbearia, para que eu possa
 desenvolver um software eficiente e funcional para o negócio.)<
 
 >Dev (Como programador: Quero um sistema de agendamento de horários para minha barbearia, para que eu possa
 implementar as funcionalidades necessárias para atender as necessidades do negócio e dos clientes.)

 >UX (Como designer de experiência do usuário: Quero um sistema de agendamento de horários para minha barbearia,
 para que eu possa criar uma interface intuitiva e agradável para os usuários, garantindo uma experiência de
 agendamento satisfatório.)<

 >IA (Como analista de dados: Quero um sistema de agendamento de horários para minha barbearia, para que eu possa
 coletar e analisar os dados armazenados, ajudando a identificar um padrão de cada cliente e otimizar as estratégias de marketing.)<]


isso e um bloco isso e um bloco de comentario.
projeto- 

este e um exemplo de docstring para o modulo.
ele pode conter uma descricao geral do modulo,
informacoes sobre o autor, data de criaco e outras informacoes relevantes.

'''
# isso e um comentarion de lingua, Finalmente quebramos a maldicao.
#print("Ola mundo!")

#print('\n---------------------------------------------------------------------\n')

print('olá, mundo!')
print('/n----------------------------------------------------------------------------')
print('bem vido ao sistema de vendas - barbearia')
print('1 - selecionar sua necessidade')
print('2 - escolha o melhor horario')
print('3 - realizar agendamento')
print('0 - sair')
print('/n-----------------------------------------------------------------------------')

opcao = input('Digete a opcao desejada: ')

if opcao == '1':
 printi('Opção 1 - Cadastrando produtos...')
# faca a logica para cadastrar o produto aqui,
# e somente a insencao dos dados usando input e os tipos de dados.
nome_produto = input('digite o nome do produto:')

quantidade_estoque = int(input("Digite a quantidade em estoque: "))


preco_produto = float(input('Digite o preço do produto: '))

p1_nome = ""
p2_nome = ""
p3_nome = ""

print("Cadastrando produtos")

# Cadastro na vaga 1
if p1_nome == "":

    p1_nome = input("Digite o nome do produto: ")
    p1_estoque = int(input("Digite a quantidade em estoque: "))
    p1_preco = float(input("Digite o preço do produto: "))
    p1_validade = input("Digite a validade do produto: ")
    p1_descricao = input("Digite a descrição do produto: ")

    print(f'\nProduto "{p1_nome}" cadastrado na vaga 1!')

# Cadastro na vaga 2
elif p2_nome == "":

    p2_nome = input("Digite o nome do produto: ")
    p2_estoque = int(input("Digite a quantidade em estoque: "))
    p2_preco = float(input("Digite o preço do produto: "))
    p2_validade = input("Digite a validade do produto: ")
    p2_descricao = input("Digite a descrição do produto: ")

    print(f'\nProduto "{p2_nome}" cadastrado na vaga 2!')

# Cadastro na vaga 3
elif p3_nome == "":

    p3_nome = input("Digite o nome do produto: ")
    p3_estoque = int(input("Digite a quantidade em estoque: "))
    p3_preco = float(input("Digite o preço do produto: "))
    p3_validade = input("Digite a validade do produto: ")
    p3_descricao = input("Digite a descrição do produto: ")

    print(f'\nProduto "{p3_nome}" cadastrado na vaga 3!')

else:
    print("Não há vagas disponíveis para cadastro.")