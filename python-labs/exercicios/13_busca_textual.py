import unicodedata


def simplificar(texto):
    normalizado = unicodedata.normalize("NFKD", texto.casefold())
    return "".join(letra for letra in normalizado if not unicodedata.combining(letra))


def buscar(registros, termo):
    consulta = simplificar(termo.strip())
    if not consulta:
        return []
    return [item for item in registros if consulta in simplificar(item)]


if __name__ == "__main__":
    assert buscar(["Ação", "Python"], "acao") == ["Ação"]
    print(buscar(["Programação Web", "Banco de Dados", "Python"], "program"))
