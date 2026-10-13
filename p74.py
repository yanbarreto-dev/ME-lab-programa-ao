produtos = {
    1: "Teclado",
    2: "Mouse",
    3: "Monitor"
}


def buscar_produto(id_produto):
    try:
        produto = produtos[id_produto]
        return produto, 200

    except KeyError:
        return "Produto não encontrado.", 404

    except Exception:
        return "Erro interno do servidor.", 500


print(buscar_produto(1))
print(buscar_produto(10))