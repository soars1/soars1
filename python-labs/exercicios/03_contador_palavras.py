import re
from collections import Counter


def contar_palavras(texto):
    return Counter(re.findall(r"\w+", texto.casefold(), flags=re.UNICODE))


def mais_comuns(texto, limite=5):
    return contar_palavras(texto).most_common(limite)


if __name__ == "__main__":
    assert contar_palavras("Python python!")["python"] == 2
    print(mais_comuns(input("Texto: ")))
