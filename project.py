import csv
import sys

class Eletrodomestico:
    """Classe que representa um aparelho e calcula o seu consumo individual."""
    def __init__(self, nome, potencia, horas):
        self.nome = nome
        self.potencia = float(potencia)
        self.horas_uso_diario = float(horas)

    def calcular_consumo_kwh(self):
        """Calcula kWh diários: (Watts * Horas) / 1000."""
        return (self.potencia * self.horas_uso_diario) / 1000

def carregar_dados_sensores(nome_ficheiro):
    """Simula sensores: lê o CSV e cria objetos Eletrodomestico."""
    lista_aparelhos = []
    try:
        with open(nome_ficheiro, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                
                novo = Eletrodomestico(
                    linha['aparelho'].strip(), 
                    linha['potencia_watts'].strip(), 
                    linha['horas_uso'].strip()
                )
                lista_aparelhos.append(novo)
        return lista_aparelhos
    except (FileNotFoundError, KeyError, Exception):
        return []

def calcular_consumo_total_diario(lista):
    """Soma o consumo de todos os itens da lista."""
    return sum(item.calcular_consumo_kwh() for item in lista)

def calcular_consumo_mensal(diario):
    """Projeção para 30 dias."""
    return diario * 30

def calcular_custo(consumo, preco=0.22):
    """Calcula o custo final em Euros."""
    return consumo * preco

def main():
    """Executa a lógica principal e exibe o relatório detalhado."""
    # 1. Carregamento
    inventario = carregar_dados_sensores("sensores.csv")
    
    if not inventario:
        sys.exit("Erro: Ficheiro 'sensores.csv' não encontrado ou inválido.")
    
    # 2. Cálculos
    total_diario = calcular_consumo_total_diario(inventario)
    total_mensal = calcular_consumo_mensal(total_diario)
    custo_final = calcular_custo(total_mensal)
    
    # 3. Output Detalhado
    print("\n" + "="*55)
    print("      RELATÓRIO DE CONSUMO (DADOS DOS SENSORES)")
    print("="*55)
    
    for item in inventario:
        consumo_item = item.calcular_consumo_kwh()
        print(f"-> {item.nome:18} | Consumo: {consumo_item:>7.2f} kWh/dia")
    
    print("-" * 55)
    print(f"CONSUMO TOTAL DIÁRIO:    {total_diario:>7.2f} kWh")
    print(f"PROJEÇÃO MENSAL:         {total_mensal:>7.2f} kWh")
    print(f"CUSTO ESTIMADO (MÊS):    {custo_final:>7.2f} €")
    print("="*55 + "\n")

if __name__ == "__main__":
    main()
