arquivo = None

try:
    arquivo = open("relatorio_vendas.txt", "r", encoding="utf-8")
    conteudo = arquivo.read()

    print(conteudo)

except FileNotFoundError:
    print("Arquivo não encontrado.")

finally:
    if arquivo is not None:
        arquivo.close()

    print("Encerramento do recurso.")