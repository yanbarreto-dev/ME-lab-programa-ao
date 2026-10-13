def contar_caractere(texto, caractere):
    return texto.count(caractere)


texto = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

print("Quantidade:", contar_caractere(texto, caractere))