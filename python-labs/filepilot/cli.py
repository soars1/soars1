"""Interface de linha de comando do FilePilot."""

import argparse
from pathlib import Path

from actions import aplicar_plano
from plan import criar_plano
from report import formatar_resumo


def main() -> None:
    parser = argparse.ArgumentParser(description="Organize arquivos por categoria.")
    parser.add_argument("pasta", type=Path, help="Pasta a examinar")
    parser.add_argument("--aplicar", action="store_true", help="Executar movimentos após a prévia")
    args = parser.parse_args()
    try:
        plano = criar_plano(args.pasta)
        print(formatar_resumo(plano))
        for origem, destino in plano:
            print(f"{origem.name} -> {destino.parent.name}/")
        if args.aplicar:
            executados = aplicar_plano(plano)
            print(f"Movimentos realizados: {len(executados)}")
        else:
            print("Simulação: nenhum arquivo foi movido. Use --aplicar para executar.")
    except (OSError, ValueError) as erro:
        parser.exit(1, f"Erro: {erro}\n")


if __name__ == "__main__":
    main()
