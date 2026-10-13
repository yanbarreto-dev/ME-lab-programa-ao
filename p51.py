temperaturas = []

for i in range(5):
    temperatura = float(input("Digite a temperatura do dia: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)

print("Temperaturas cadastradas:", temperaturas)
print("Média das temperaturas:", media)

if 18 <= media <= 28:
    print("A média está dentro da faixa ideal de cultivo.")
else:
    print("A média está fora da faixa ideal de cultivo.")
