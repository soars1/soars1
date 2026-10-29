from math import ceil


def paginar(itens, pagina=1, tamanho=10):
    if tamanho <= 0 or pagina <= 0:
        raise ValueError("Página e tamanho devem ser positivos")
    inicio = (pagina - 1) * tamanho
    return {
        "itens": itens[inicio:inicio + tamanho],
        "pagina": pagina,
        "total_paginas": ceil(len(itens) / tamanho),
    }


if __name__ == "__main__":
    assert paginar(list(range(9)), 2, 5)["itens"] == [5, 6, 7, 8]
    print(paginar(list(range(25)), 2, 10))
