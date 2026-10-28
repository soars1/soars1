"""Execução explícita das alterações planejadas."""

from pathlib import Path
import shutil

from safety import destino_disponivel


def aplicar_plano(plano: list[tuple[Path, Path]]) -> list[tuple[Path, Path]]:
    """Move apenas arquivos ainda presentes, sem sobrescrever destinos."""
    concluidos = []
    reservados: set[Path] = set()
    for origem, destino in plano:
        if not origem.is_file() or origem.is_symlink():
            continue
        destino = destino_disponivel(destino, reservados)
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(origem), str(destino))
        concluidos.append((origem, destino))
    return concluidos
