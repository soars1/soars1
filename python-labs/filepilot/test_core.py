"""Testes das regras puras; execute python -m unittest discover."""

import unittest

from core import classificar_arquivo


class ClassificacaoTests(unittest.TestCase):
    def test_imagem_maiuscula(self):
        self.assertEqual(classificar_arquivo("FOTO.PNG"), "Imagens")

    def test_documento(self):
        self.assertEqual(classificar_arquivo("relatorio.pdf"), "Documentos")

    def test_desconhecido(self):
        self.assertEqual(classificar_arquivo("dados.xyz"), "Outros")

    def test_sem_extensao(self):
        self.assertEqual(classificar_arquivo("README"), "Outros")


if __name__ == "__main__":
    unittest.main()
