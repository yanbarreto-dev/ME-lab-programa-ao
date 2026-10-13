def cadastrar_produto(nome, preco, quantidade):
    if not nome.strip():
        raise ValueError("O nome não pode ser vazio.")

    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    return "Produto cadastrado com sucesso!"


try:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade: "))

    mensagem = cadastrar_produto(nome, preco, quantidade)

except ValueError as erro:
    print("Erro:", erro)

else:
    print(mensagem)