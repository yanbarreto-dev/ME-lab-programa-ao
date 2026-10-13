preco = input("Digite o preço do produto: R$ ")

try:
    preco = float(preco)

except ValueError:
    print("Preço inválido.")

else:
    desconto = preco * 0.10
    preco_final = preco - desconto

    print(f"Preço com desconto: R$ {preco_final:.2f}")