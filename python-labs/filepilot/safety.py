"""Proteções para evitar sobrescrever arquivos existentes."""

from pathlib import Path


def destino_disponivel(destino: Path, reservados: set[Path] | None = None) -> Path:
    """Encontra nome livre usando sufixo numérico se necessário."""
    reservados = reservados if reservados is not None else set()
    candidato = destino
    numero = 1
    while candidato.exists() or candidato in reservados:
        candidato = destino.with_name(f"{destino.stem} ({numero}){destino.suffix}")
        numero += 1
    reservados.add(candidato)
    return candidato
