def calcular_gorjeta(conta):
    return conta * 0.10


valor = float(input("Valor da conta: R$ "))
gorjeta = calcular_gorjeta(valor)

print(f"Gorjeta: R$ {gorjeta:.2f}")