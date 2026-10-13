import random

sorteio = random.randint(1,100)

escolha = int(input('Escolha um número de 1 a 100 : '))

while sorteio != escolha :
    

    if sorteio > escolha :
        print("O Número sorteado é maior")
    else :
        print("O Número sorteado é menor")

    escolha = int(input('Escolha um número de 1 a 100 : '))

print("Você acertou!!")
