def validar_cpf(cpf):
    numeros = "".join(letra for letra in cpf if letra.isdigit())
    if len(numeros) != 11 or len(set(numeros)) == 1:
        return False
    for tamanho in (9, 10):
        soma = sum(int(numero) * peso for numero, peso in zip(numeros[:tamanho], range(tamanho + 1, 1, -1)))
        resto = (soma * 10) % 11
        digito = 0 if resto == 10 else resto
        if digito != int(numeros[tamanho]):
            return False
    return True


if __name__ == "__main__":
    assert not validar_cpf("111.111.111-11")
    assert not validar_cpf("123.456.789-00")
    print(validar_cpf(input("CPF: ")))
