from project import Eletrodomestico, calcular_consumo_total_diario, calcular_consumo_mensal, calcular_custo

def test_calcular_consumo_total_diario():
    # Criamos uma lista de teste com um aparelho simples
    teste_lista = [Eletrodomestico("Lampada", 100, 10)] # 100W * 10h / 1000 = 1kWh
    assert calcular_consumo_total_diario(teste_lista) == 1.0

def test_calcular_consumo_mensal():
    # Se o consumo diário for 2, o mensal (30 dias) deve ser 60
    assert calcular_consumo_mensal(2) == 60

def test_calcular_custo():
    # Se o consumo for 100 e o preço for 0.20, o custo deve ser 20
    assert calcular_custo(100, 0.20) == 20.0