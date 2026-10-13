def realizar_saque(saldo, valor_saque):
    if valor_saque <= 0:
        raise ValueError("O valor deve ser positivo.")

    if valor_saque > saldo:
        raise ValueError("Saldo insuficiente.")

    return saldo - valor_saque


try:
    saldo = float(input("Saldo atual: R$ "))
    saque = float(input("Valor do saque: R$ "))

    novo_saldo = realizar_saque(saldo, saque)

except ValueError as erro:
    print("Erro:", erro)

else:
    print(f"Novo saldo: R$ {novo_saldo:.2f}")