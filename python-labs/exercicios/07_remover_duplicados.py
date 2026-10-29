def remover_duplicados(valores):
    vistos = set()
    resultado = []
    for valor in valores:
        if valor not in vistos:
            vistos.add(valor)
            resultado.append(valor)
    return resultado


if __name__ == "__main__":
    assert remover_duplicados([2, 1, 2, 3, 1]) == [2, 1, 3]
    print(remover_duplicados(input("Palavras: ").split()))
