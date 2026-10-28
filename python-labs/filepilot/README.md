# FilePilot

Laboratório em Python para organizar arquivos por extensão, com prévia antes de qualquer alteração.

## O que demonstra

Funções, estruturas de dados, módulos, `pathlib`, movimentação de arquivos, tratamento de erros e testes com `unittest`. Somente arquivos da pasta escolhida são analisados; subpastas não são percorridas.

## Requisitos

Python 3.10+; nenhuma dependência externa.

## Como usar

No terminal, a partir da raiz do repositório:

```bash
python python-labs/filepilot/cli.py --help
python python-labs/filepilot/cli.py "C:/Users/SeuUsuario/Downloads"
```

A primeira execução é uma **simulação**: mostra quais arquivos seriam organizados, sem mover nada. Depois de revisar a prévia, para realizar os movimentos:

```bash
python python-labs/filepilot/cli.py "C:/Users/SeuUsuario/Downloads" --aplicar
```

Teste primeiro em uma pasta temporária com arquivos descartáveis e mantenha backup. Os arquivos são movidos, não copiados. Se já existir um nome igual na pasta de destino, o programa usa um sufixo numérico.

## Testes

```bash
python -m unittest discover -s python-labs/filepilot -p "test_*.py"
```

## Próximos exercícios

Adicionar um registro das movimentações para permitir desfazer, opção para filtrar extensões e testes de integração da execução.
