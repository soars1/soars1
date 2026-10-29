def normalizar_nome(nome):
    return " ".join(parte.capitalize() for parte in nome.strip().split())


if __name__ == "__main__":
    assert normalizar_nome("  aNA   SOARES ") == "Ana Soares"
    print(normalizar_nome(input("Nome: ")))
