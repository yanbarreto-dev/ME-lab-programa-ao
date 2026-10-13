def buscar_permissao(perfis, perfil, indice):
    try:
        return perfis[perfil][indice]

    except (KeyError, IndexError):
        return "acesso_restrito"


perfis = {
    "administrador": ["ler", "escrever", "excluir"],
    "usuario": ["ler"]
}

print(buscar_permissao(perfis, "administrador", 1))
print(buscar_permissao(perfis, "usuario", 5))