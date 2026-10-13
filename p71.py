
def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor do saque deve ser positivo.")

    if valor > saldo:
        raise ValueError("Saldo insuficiente.")

    return saldo - valor


try:
    saldo = float(input("Digite seu saldo: R$ "))
    valor = float(input("Digite o valor do saque: R$ "))

    novo_saldo = sacar(saldo, valor)

except ValueError as erro:
    print("Erro:", erro)

else:
    print(f"Novo saldo: R$ {novo_saldo:.2f}")
