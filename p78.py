def calcular_media(n1, n2, n3):
    notas = [n1, n2, n3]

    for nota in notas:
        if nota < 0 or nota > 10:
            raise ValueError("As notas devem estar entre 0 e 10.")

    return sum(notas) / 3


try:
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    n3 = float(input("Terceira nota: "))

    media = calcular_media(n1, n2, n3)

except ValueError as erro:
    print("Erro:", erro)

else:
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")