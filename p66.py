def calcular_animais():
    for coelhos in range(36):
        galinhas = 35 - coelhos

        pernas = coelhos * 4 + galinhas * 2

        if pernas == 94:
            return coelhos, galinhas


coelhos, galinhas = calcular_animais()

print("Coelhos:", coelhos)
print("Galinhas:", galinhas)