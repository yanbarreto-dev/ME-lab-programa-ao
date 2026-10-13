import traceback


def processar_dados(dados):
    resultados = []

    for item in dados:
        try:
            numero = float(item)
            resultados.append(numero)

        except (TypeError, ValueError):
            traceback.print_exc()
            print("Elemento inválido ignorado.")

    return resultados


dados = ["10", "abc", 25, None, "8.5"]

print("Dados válidos:", processar_dados(dados))