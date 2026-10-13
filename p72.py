def parse_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if not cpf.isdigit() or len(cpf) != 11:
        raise ValueError("CPF inválido.")

    return cpf


def main():
    try:
        cpf = input("Digite o CPF: ")
        resultado = parse_cpf(cpf)

        print("CPF válido:", resultado)

    except ValueError as erro:
        print(erro)


main()