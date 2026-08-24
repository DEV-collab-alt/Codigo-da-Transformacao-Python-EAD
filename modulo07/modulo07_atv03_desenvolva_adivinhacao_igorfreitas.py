import math
import random
import sys
import time


def digitar(texto, velocidade=0.02):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()


def jogo_adivinhacao():
    print("=" * 55)
    digitar("  🎯 DESAFIO SUPREMO DE ADIVINHAÇÃO (1 a 24) 🎯")
    print("=" * 55)

    inicio = 1
    fim = 24
    numero_secreto = random.randint(inicio, fim)

    chance_porcento = math.floor((1 / 24) * 100)
    tentativas_ideais = math.ceil(math.log2(fim - inicio + 1))

    digitar(f"\n📊 [Análise Math]: Chance de acerto direto: ~{chance_porcento}%")
    digitar(
        f"📊 [Análise Math]: Com estratégia perfeita, dá pra vencer em {tentativas_ideais} chutes!"
    )
    digitar(
        "\n⚠️  Regra: Você tem 6 tentativas no total. Faça valer cada chute!\n"
    )

    max_tentativas = 6

    for tentativa in range(1, max_tentativas + 1):
        
        while True:
            try:
                palpite = int(
                    input(
                        f"👉 Tentativa {tentativa}/{max_tentativas} - Digite um número ({inicio}-{fim}): "
                    )
                )
                if inicio <= palpite <= fim:
                    break
                print(f"⚠️ Por favor, escolha um número entre {inicio} e {fim}!")
            except ValueError:
                print("⚠️ Entrada inválida! Digite apenas números inteiros.")

        if tentativa == 6:
            print("\n" + "🔥" * 20)
            digitar("⚡ ÚLTIMA CHANCE! O MOMENTO DA VERDADE! ⚡")
            print("🔥" * 20)
            time.sleep(1)

            if palpite == numero_secreto:
                digitar(
                    f"\n🎉 🏆 NÚMERO PERFEITO! VOCÊ ACERTOU NA 6ª TENTATIVA! O número era {numero_secreto}!"
                )
                digitar("Sua frieza no momento decisivo foi impressionante!")
            else:
                digitar(
                    f"\n❌ 😞 ☠️ QUE PENA! Você errou a 6ª tentativa. O número era {numero_secreto}."
                )
                digitar("💥 GAME OVER! Tente novamente para dominar o jogo!")
            break

        if palpite == numero_secreto:
            digitar(
                f"\n🎉 🏆 INCRÍVEL! Você acertou o número {numero_secreto} na tentativa {tentativa}/{max_tentativas}!"
            )
            digitar("Mente brilhante! Leitura de jogo impecável.")
            break
        elif palpite < numero_secreto:
            print(f"📈 O número secreto é MAIOR que {palpite}.\n")
        else:
            print(f"📉 O número secreto é MENOR que {palpite}.\n")

    print("\n" + "=" * 55)
    digitar("     Obrigado por jogar! Desenvolvido em Python. 🐍")
    print("=" * 55)



if __name__ == "__main__":
    jogo_adivinhacao()