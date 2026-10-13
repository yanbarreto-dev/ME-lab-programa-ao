def receber_numeros():
    numeros = []

    for i in range(5):
        numero = float(input(f"Digite o {i + 1}º número: "))
        numeros.append(numero)

    return numeros


def maior_numero(numeros):
    return max(numeros)


def menor_numero(numeros):
    return min(numeros)


valores = receber_numeros()

print("Maior:", maior_numero(valores))
print("Menor:", menor_numero(valores))