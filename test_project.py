import pytest
from project import (
    Eletrodomestico, 
    calcular_consumo_total_diario, 
    calcular_consumo_mensal, 
    calcular_custo,
    carregar_dados_sensores
)

def test_eletrodomestico_class():
    """Verifica se a classe calcula corretamente o consumo."""
    a = Eletrodomestico("Teste", 1000, 2)
    assert a.calcular_consumo_kwh() == 2.0

def test_calcular_consumo_total_diario():
    """Verifica se a soma da lista de objetos funciona."""
    lista = [Eletrodomestico("A", 500, 2), Eletrodomestico("B", 1000, 1)]
    assert calcular_consumo_total_diario(lista) == 2.0

def test_calcular_consumo_mensal():
    """Verifica a projeção mensal."""
    assert calcular_consumo_mensal(10) == 300

def test_calcular_custo():
    """Verifica o cálculo do preço."""
    assert calcular_custo(100, 0.20) == 20.0

def test_carregar_dados_sensores():
    """Verifica se o CSV é lido corretamente (Resolve o AssertionError)."""
    dados = carregar_dados_sensores("sensores.csv")
    assert isinstance(dados, list)
    assert len(dados) > 0 # Garante que leu os aparelhos do ficheiro