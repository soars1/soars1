from collections import Counter


def apurar_votos(votos, candidatos):
    permitidos = set(candidatos)
    contagem = Counter(voto for voto in votos if voto in permitidos)
    return {nome: contagem[nome] for nome in candidatos}


def vencedores(resultado):
    if not resultado:
        return []
    maior = max(resultado.values())
    return [nome for nome, votos in resultado.items() if votos == maior]


if __name__ == "__main__":
    resultado = apurar_votos(["A", "B", "A", "X"], ["A", "B"])
    assert vencedores(resultado) == ["A"]
    print(resultado)
