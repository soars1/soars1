"""Teste integrado do plano sem alterações no disco."""

import tempfile
import unittest
from pathlib import Path

from plan import criar_plano
from report import resumo


class PlanoTests(unittest.TestCase):
    def test_plano_nao_move_arquivos(self):
        with tempfile.TemporaryDirectory() as temporario:
            pasta = Path(temporario)
            arquivo = pasta / "imagem.jpg"
            arquivo.write_bytes(b"exemplo")
            plano = criar_plano(pasta)
            self.assertTrue(arquivo.exists())
            self.assertEqual(plano[0][1], pasta / "Imagens" / "imagem.jpg")
            self.assertEqual(resumo(plano), {"Imagens": 1})


if __name__ == "__main__":
    unittest.main()
