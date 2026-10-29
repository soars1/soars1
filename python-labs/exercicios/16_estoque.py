def atualizar_estoque(estoque, produto, quantidade):
    atual = estoque.get(produto, 0)
    novo = atual + quantidade
    if novo < 0:
        raise ValueError("Estoque insuficiente")
    atualizado = estoque.copy()
    atualizado[produto] = novo
    return atualizado


if __name__ == "__main__":
    assert atualizar_estoque({"mouse": 2}, "mouse", -1) == {"mouse": 1}
    print(atualizar_estoque({"mouse": 2}, "teclado", 3))
