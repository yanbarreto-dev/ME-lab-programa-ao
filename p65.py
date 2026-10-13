def calcularCubo(numero):
    return numero ** 3


def calcularDivisaoCubo(numero):
    if numero % 3 == 0:
        return calcularCubo(numero)

    return False


print(calcularDivisaoCubo(3))
print(calcularDivisaoCubo(5))