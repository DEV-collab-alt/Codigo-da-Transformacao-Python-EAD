
print("--- ATIVIDADE 2 ---")

print("Olá, mundo!")
print(10 + 5)


print(type("Texto"))    
print(type(25))        
print(type(19.90))     
print()                

print("--- ATIVIDADE 3 ---")

nome = input("Digite o seu nome: ")


print(f"Olá, {nome}! Seja muito bem-vindo ao mundo do Python!")
print()                 


print("--- DESAFIO EXTRA ---")
from datetime import datetime

nome_desafio = input("Digite o seu nome para o desafio extra: ")


agora = datetime.now()


hora_formatada = agora.strftime("%H:%M")


print(f"Olá, {nome_desafio}! Seja muito bem-vindo! Agora são exatamente {hora_formatada}.")