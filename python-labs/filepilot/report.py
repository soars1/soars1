"""Relatórios textuais sobre a organização."""

from collections import Counter
from pathlib import Path


def resumo(plano: list[tuple[Path, Path]]) -> dict[str, int]:
    """Conta os arquivos de cada categoria."""
    return dict(sorted(Counter(destino.parent.name for _, destino in plano).items()))


def formatar_resumo(plano: list[tuple[Path, Path]]) -> str:
    linhas = [f"Arquivos encontrados: {len(plano)}"]
    for categoria, quantidade in resumo(plano).items():
        linhas.append(f"- {categoria}: {quantidade}")
    return "\n".join(linhas)
