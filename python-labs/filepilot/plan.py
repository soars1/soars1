"""Montagem de um plano de organização sem alterar arquivos."""

from pathlib import Path

from core import classificar_arquivo


def criar_plano(pasta: Path) -> list[tuple[Path, Path]]:
    """Lista pares (origem, destino) somente de arquivos na pasta."""
    pasta = Path(pasta).expanduser().resolve()
    if not pasta.is_dir():
        raise NotADirectoryError(f"Pasta inexistente: {pasta}")
    plano = []
    for origem in sorted(pasta.iterdir()):
        if origem.is_file() and not origem.is_symlink():
            destino = pasta / classificar_arquivo(origem.name) / origem.name
            plano.append((origem, destino))
    return plano
