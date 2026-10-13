import random

sorteio = random.randint(1,10)

escolha = int(input('Escolha um número de 1 a 10 : '))

if sorteio == escolha :
    print("Você acertou!!")
else:
    print("Você errou, o número sorteado era ",sorteio)