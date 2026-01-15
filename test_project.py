import pytest
import os
from project import (
    Eletrodomestico, 
    calcular_consumo_total_diario, 
    calcular_consumo_mensal, 
    calcular_custo,
    carregar_dados_sensores
)

def test_eletrodomestico_class():
    # Testa se a classe calcula corretamente o kWh
    aparelho = Eletrodomestico("Teste", 1000, 1)
    assert aparelho.calcular_consumo_kwh() == 1.0

def test_calcular_consumo_total_diario():
    # Testa a soma de uma lista de aparelhos
    lista = [
        Eletrodomestico("A", 100, 10), # 1kWh
        Eletrodomestico("B", 500, 2)   # 1kWh
    ]
    assert calcular_consumo_total_diario(lista) == 2.0

def test_calcular_consumo_mensal():
    # Testa a multiplicação por 30 dias
    assert calcular_consumo_mensal(10) == 300

def test_calcular_custo():
    # Testa o cálculo do preço (ex: 100kWh * 0.20€ = 20€)
    assert calcular_custo(100, 0.20) == 20.0

def test_carregar_dados_sensores():
    # Testa se o programa consegue ler o ficheiro sensores.csv que criaste
    # Este teste garante que o requisito da professora (CSV) está a funcionar
    dados = carregar_dados_sensores("sensores.csv")
    assert isinstance(dados, list)
    assert len(dados) > 0
    assert isinstance(dados[0], Eletrodomestico)