# Simulador de Consumo Energético - Green Data Science

# Autores: Xavier Loreto e João Cristóvão

Este projeto foi desenvolvido para a disciplina introdução ao Python e tem como objetivo simular a monitorização de consumos energéticos domésticos, promovendo a consciência ambiental através de **Green Data Science**.

## Funcionalidades
* **Simulação de Sensores**: O programa lê dados de consumo real a partir de um ficheiro externo (`sensores.csv`).
* **Cálculos Automáticos**: Calcula o consumo diário em kWh, a projeção mensal e o custo estimado em Euros.
* **Relatórios Detalhados**: Apresenta uma tabela organizada no terminal com o gasto individual de cada eletrodoméstico.

## Estrutura do Projeto
* `project.py`: Código principal com a lógica de classes e processamento de dados.
* `test_project.py`: Testes unitários para garantir a precisão dos cálculos.
* `sensores.csv`: Base de dados simulada com aparelhos, potências (Watts) e horas de uso.
* `requirements.txt`: Lista de dependências necessárias (pytest).

## Como Executar
* Instale as dependências:
* Instale o pytest: `pip install -r requirements.txt`
* Corra o projeto: `python project.py`
* Teste: `pytest test_project.py`
