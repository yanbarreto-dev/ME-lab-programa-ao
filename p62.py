def numero_perfeito(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    return soma == numero


n = int(input("Digite um número: "))

if numero_perfeito(n):
    print("É um número perfeito.")
else:
    print("Não é um número perfeito.")