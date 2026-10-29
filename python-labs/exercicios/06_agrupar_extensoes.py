from collections import defaultdict
from pathlib import Path


def agrupar_extensoes(nomes):
    grupos = defaultdict(list)
    for nome in nomes:
        extensao = Path(nome).suffix.lower() or "(sem extensão)"
        grupos[extensao].append(nome)
    return dict(sorted(grupos.items()))


if __name__ == "__main__":
    exemplo = ["a.PDF", "b.pdf", "foto.png", "README"]
    assert len(agrupar_extensoes(exemplo)[".pdf"]) == 2
    print(agrupar_extensoes(exemplo))
