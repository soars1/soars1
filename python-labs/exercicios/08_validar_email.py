import re

PADRAO = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def validar_email(email):
    return bool(PADRAO.fullmatch(email.strip())) and ".." not in email


if __name__ == "__main__":
    assert validar_email("pessoa@exemplo.com")
    assert not validar_email("exemplo@")
    print(validar_email(input("E-mail: ")))
