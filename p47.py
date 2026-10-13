matriz = [
    [10,-5,8],
    [-2,7,0],
    [4,-9,3]
]

positivos = 0

for linha in matriz:
    for valor in linha:
        if valor > 0:
            positivos += 1

print(positivos)
