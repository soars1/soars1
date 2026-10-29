from collections import defaultdict
from decimal import Decimal


def resumir_despesas(lancamentos):
    totais = defaultdict(lambda: Decimal("0"))
    for categoria, valor in lancamentos:
        total = Decimal(str(valor))
        if total < 0:
            raise ValueError("Despesa negativa")
        totais[categoria] += total
    return dict(sorted(totais.items()))


if __name__ == "__main__":
    exemplo = [("Comida", "12.50"), ("Livros", "20"), ("Comida", "7.50")]
    assert resumir_despesas(exemplo)["Comida"] == Decimal("20.00")
    print(resumir_despesas(exemplo))
