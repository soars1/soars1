import re
import unicodedata


def gerar_slug(titulo):
    texto = unicodedata.normalize("NFKD", titulo)
    texto = "".join(letra for letra in texto if not unicodedata.combining(letra))
    return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")


if __name__ == "__main__":
    assert gerar_slug("Introdução ao Python!") == "introducao-ao-python"
    print(gerar_slug(input("Título: ")))
