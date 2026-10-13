disciplinas = ("Matemática", "Português")

alunos = {
    "Ana": {"Matemática": 8, "Português": 7},
    "Carlos": {"Matemática": 6, "Português": 5},
    "Pedro": {"Matemática": 9, "Português": 8},
    "Beatriz": {"Matemática": 7, "Português": 6},
    "Maria": {"Matemática": 10, "Português": 9}
}

print("Disciplinas:", disciplinas)

for nome, notas in alunos.items():
    media = (notas["Matemática"] + notas["Português"]) / 2

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(nome, "- Média:", media, "-", situacao)
