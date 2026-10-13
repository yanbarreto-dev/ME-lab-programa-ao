try:
    lucro = float(input("Lucro do trimestre: R$ "))
    acionistas = int(input("Quantidade de acionistas: "))

    resultado = lucro / acionistas

except ZeroDivisionError:
    print("Não é possível dividir por zero.")

except ValueError:
    print("Digite valores numéricos válidos.")

else:
    print(f"Lucro por acionista: R$ {resultado:.2f}")