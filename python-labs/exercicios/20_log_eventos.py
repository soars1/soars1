import json
from datetime import datetime, timezone
from pathlib import Path


def registrar_evento(caminho, acao, detalhes=None):
    evento = {
        "data": datetime.now(timezone.utc).isoformat(),
        "acao": acao,
        "detalhes": detalhes or {},
    }
    with Path(caminho).open("a", encoding="utf-8") as arquivo:
        arquivo.write(json.dumps(evento, ensure_ascii=False) + "\n")
    return evento


def ler_eventos(caminho):
    arquivo = Path(caminho)
    if not arquivo.exists():
        return []
    return [json.loads(linha) for linha in arquivo.read_text(encoding="utf-8").splitlines() if linha.strip()]


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as pasta:
        caminho = Path(pasta) / "eventos.jsonl"
        registrar_evento(caminho, "inicio")
        assert ler_eventos(caminho)[0]["acao"] == "inicio"
