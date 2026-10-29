from decimal import Decimal


def aplicar_desconto(preco, percentual):
    preco = Decimal(str(preco))
    percentual = Decimal(str(percentual))
    if preco < 0 or not 0 <= percentual <= 100:
        raise ValueError("Preço ou desconto inválido")
    return (preco * (1 - percentual / 100)).quantize(Decimal("0.01"))


if __name__ == "__main__":
    assert aplicar_desconto("100", "15") == Decimal("85.00")
    print(aplicar_desconto(input("Preço: "), input("Desconto (%): ")))
