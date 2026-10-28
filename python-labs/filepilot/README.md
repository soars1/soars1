# FilePilot

Um laboratório de Python para organizar arquivos de forma segura.

## Objetivo
Aprender funções, módulos, testes e operações com arquivos. O programa organiza os arquivos de **uma pasta**, sem entrar em subpastas.

## Uso
Requer Python 3.10+ e não utiliza bibliotecas externas.

```bash
python -m python-labs.filepilot
```

Como o diretório tem hífen, execute diretamente:

```bash
python python-labs/filepilot/cli.py --help
python python-labs/filepilot/cli.py ~/Downloads
python python-labs/filepilot/cli.py ~/Downloads --aplicar
```

Por padrão, somente simula as ações. Use --aplicar para mover os arquivos, depois de conferir a prévia. Evite usar sobre pastas importantes sem backup.
