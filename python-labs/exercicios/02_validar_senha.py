def validar_senha(senha):
    return {
        "tamanho": len(senha) >= 8,
        "numero": any(letra.isdigit() for letra in senha),
        "maiuscula": any(letra.isupper() for letra in senha),
        "minuscula": any(letra.islower() for letra in senha),
    }


def senha_forte(senha):
    return all(validar_senha(senha).values())


if __name__ == "__main__":
    assert senha_forte("Teste123")
    assert not senha_forte("senha")
    print(validar_senha(input("Senha para avaliar: ")))
