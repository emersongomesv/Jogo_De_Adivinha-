import random
import os

# Inicializa contagem de erros e gera um número aleatório
erros = 0
sorteado = random.randrange(0, 100)

# Solicita ao jogador que insira um número
jogador = int(input("Digite seu número (0 a 99): "))

# Enquanto o número não for acertado, continue pedindo um novo número
while sorteado != jogador:
    os.system('cls')  # Limpa a tela (para Windows)
    
    # Informa se o número sorteado é maior ou menor que o palpite
    if sorteado > jogador:
        print("Erro, o número é maior.")
    elif sorteado < jogador:
        print("Erro, o número é menor.")
    
    # Incrementa o contador de erros
    erros += 1
    
    # Pede um novo número ao jogador
    jogador = int(input("Digite seu número (0 a 99): "))

# Ao acertar, imprime o número e o número de tentativas
print(f"Número {jogador}, você acertou em {erros + 1} tentativas.")
           
