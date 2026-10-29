def celsius_para_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    assert celsius_para_fahrenheit(0) == 32
    assert fahrenheit_para_celsius(212) == 100
    valor = float(input("Graus Celsius: "))
    print(f"{celsius_para_fahrenheit(valor):.1f} °F")
