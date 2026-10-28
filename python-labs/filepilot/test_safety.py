"""Testes para colisões de nomes."""

import tempfile
import unittest
from pathlib import Path

from safety import destino_disponivel


class SafetyTests(unittest.TestCase):
    def test_nao_substitui_existente(self):
        with tempfile.TemporaryDirectory() as temporario:
            destino = Path(temporario) / "foto.png"
            destino.write_text("conteudo")
            self.assertEqual(destino_disponivel(destino).name, "foto (1).png")

    def test_reserva_multiplos_nomes(self):
        with tempfile.TemporaryDirectory() as temporario:
            destino = Path(temporario) / "foto.png"
            reservados = set()
            self.assertEqual(destino_disponivel(destino, reservados), destino)
            self.assertEqual(destino_disponivel(destino, reservados).name, "foto (1).png")


if __name__ == "__main__":
    unittest.main()
