import json
from pathlib import Path


def salvar_configuracao(caminho, configuracao):
    Path(caminho).write_text(json.dumps(configuracao, indent=2, ensure_ascii=False), encoding="utf-8")


def carregar_configuracao(caminho, padrao=None):
    arquivo = Path(caminho)
    if not arquivo.exists():
        return {} if padrao is None else padrao.copy()
    return json.loads(arquivo.read_text(encoding="utf-8"))


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as pasta:
        arquivo = Path(pasta) / "config.json"
        salvar_configuracao(arquivo, {"tema": "claro"})
        assert carregar_configuracao(arquivo)["tema"] == "claro"
