"""Regras puras de classificação do FilePilot."""

from pathlib import Path

CATEGORIAS = {
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "Documentos": {".pdf", ".doc", ".docx", ".txt", ".odt"},
    "Vídeos": {".mp4", ".mov", ".mkv", ".webm"},
    "Áudios": {".mp3", ".wav", ".flac", ".ogg"},
    "Compactados": {".zip", ".rar", ".7z", ".tar"},
}


def classificar_arquivo(nome: str) -> str:
    """Retorna a categoria pela extensão, sem diferenciar maiúsculas."""
    extensao = Path(nome).suffix.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "Outros"
