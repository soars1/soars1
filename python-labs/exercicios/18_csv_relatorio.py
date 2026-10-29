import csv
from pathlib import Path


def salvar_csv(caminho, registros, campos):
    caminho = Path(caminho)
    with caminho.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(registros)
    return caminho


def ler_csv(caminho):
    with Path(caminho).open(newline="", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as pasta:
        caminho = Path(pasta) / "dados.csv"
        salvar_csv(caminho, [{"nome": "Ana"}], ["nome"])
        assert ler_csv(caminho) == [{"nome": "Ana"}]
