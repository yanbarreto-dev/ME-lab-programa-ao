
numero = int(input("Digite um número inteiro positivo: "))

fatorial = 1

while numero > 1:
    fatorial *= numero
    numero -= 1

print("O fatorial é:", fatorial)

