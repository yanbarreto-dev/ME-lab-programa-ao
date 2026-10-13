
def registrar_venda(produto, preco, quantidade):
    if not produto.strip():
        raise ValueError("Nome do produto inválido.")

    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser positiva.")

    total = preco * quantidade

    return {
        "produto": produto,
        "preco": preco,
        "quantidade": quantidade,
        "total": total
    }


def gerar_relatorio(vendas):
    if len(vendas) == 0:
        print("\nNenhuma venda registrada.")
        return

    produtos = {}
    faturamento = 0

    for venda in vendas:
        nome = venda["produto"]

        produtos[nome] = produtos.get(nome, 0) + venda["quantidade"]
        faturamento += venda["total"]

    mais_vendido = max(produtos, key=produtos.get)
    ticket_medio = faturamento / len(vendas)

    print("\n===== RELATÓRIO DE VENDAS =====")
    print("Quantidade de vendas:", len(vendas))
    print("Produto mais vendido:", mais_vendido)
    print("Unidades vendidas:", produtos[mais_vendido])
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")


def registrar_erro(mensagem):
    try:
        with open("log_erros.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(mensagem + "\n")
    except OSError:
        print("Não foi possível salvar o erro no arquivo.")


def salvar_venda(venda):
    try:
        with open("vendas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(
                f"Produto: {venda['produto']} | "
                f"Preço: R$ {venda['preco']:.2f} | "
                f"Quantidade: {venda['quantidade']} | "
                f"Total: R$ {venda['total']:.2f}\n"
            )
    except OSError as erro:
        registrar_erro(f"Erro ao salvar venda: {erro}")


def main():
    vendas = []

    while True:
        produto = input("\nNome do produto (ou 'fim'): ").strip()

        if produto.lower() == "fim":
            break

        try:
            preco = float(input("Preço unitário: R$ "))
            quantidade = int(input("Quantidade vendida: "))

            venda = registrar_venda(produto, preco, quantidade)

        except ValueError as erro:
            print("Erro:", erro)
            registrar_erro(str(erro))

        except Exception as erro:
            print("Ocorreu um erro inesperado.")
            registrar_erro(str(erro))

        else:
            vendas.append(venda)
            salvar_venda(venda)
            print("Venda registrada com sucesso!")

        finally:
            print("Operação finalizada.")

    gerar_relatorio(vendas)


main()
