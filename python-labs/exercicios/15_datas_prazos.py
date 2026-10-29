from datetime import date


def dias_ate(data_texto, hoje=None):
    destino = date.fromisoformat(data_texto)
    hoje = date.today() if hoje is None else hoje
    return (destino - hoje).days


def situacao_prazo(data_texto, hoje=None):
    dias = dias_ate(data_texto, hoje)
    return "vencido" if dias < 0 else "hoje" if dias == 0 else "pendente"


if __name__ == "__main__":
    assert dias_ate("2026-11-02", date(2026, 10, 29)) == 4
    print(situacao_prazo(input("Data (AAAA-MM-DD): ")))
