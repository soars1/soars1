def calcular_media(notas, pesos=None):
    if not notas:
        raise ValueError("Informe pelo menos uma nota")
    pesos = [1] * len(notas) if pesos is None else pesos
    if len(notas) != len(pesos) or any(p < 0 for p in pesos) or sum(pesos) == 0:
        raise ValueError("Pesos inválidos")
    return sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)


if __name__ == "__main__":
    assert calcular_media([8, 10], [1, 3]) == 9.5
    print(calcular_media([float(x) for x in input("Notas: ").split()]))
