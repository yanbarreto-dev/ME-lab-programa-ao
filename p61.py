def inverter(texto):
    return texto[::-1]


frases = [
    "python2023",
    "0203programacao2023",
    "luz azul",
    "arara rara",
    "anotaram a data da maratona"
]

for frase in frases:
    print(inverter(frase))