while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            print("A idade não pode ser negativa.")
            continue

        print("Idade cadastrada:", idade)
        break

    except ValueError:
        print("Digite uma idade válida.")