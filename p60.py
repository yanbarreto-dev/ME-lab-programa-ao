def converter_temperatura(f):
    return (5 / 9) * (f - 32)


fahrenheit = float(input("Temperatura em Fahrenheit: "))
celsius = converter_temperatura(fahrenheit)

print(f"Temperatura em Celsius: {celsius:.2f} °C")