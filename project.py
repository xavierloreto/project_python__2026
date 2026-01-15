import csv  # Importa a biblioteca para ler ficheiros CSV
import sys  # Importa a biblioteca para interagir com o sistema (ex: sair do programa)

class Eletrodomestico:
    """Classe que representa um aparelho elétrico e o seu consumo."""
    def __init__(self, nome, potencia, horas):
        self.nome = nome
        self.potencia = float(potencia)  # Converte a potência para número decimal
        self.horas_uso_diario = float(horas)  # Converte as horas para número decimal

    def calcular_consumo_kwh(self):
        """Calcula o consumo diário: (Watts * Horas) / 1000 para obter kWh."""
        return (self.potencia * self.horas_uso_diario) / 1000

def carregar_dados_sensores(nome_ficheiro):
    """Lê o CSV e transforma cada linha num objeto da classe Eletrodomestico."""
    lista_aparelhos = []
    try:
        with open(nome_ficheiro, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)  # Lê o ficheiro usando o cabeçalho como chaves
            for linha in leitor:
                # Cria o objeto usando os nomes das colunas do CSV
                novo = Eletrodomestico(
                    linha['aparelho'].strip(), 
                    linha['potencia_watts'].strip(), 
                    linha['horas_uso'].strip()
                )
                lista_aparelhos.append(novo)
        return lista_aparelhos
    except (FileNotFoundError, KeyError):
        # Se o ficheiro não existir ou as colunas estiverem erradas, retorna lista vazia
        return []

def calcular_consumo_total_diario(lista):
    """Soma o consumo de todos os aparelhos na lista fornecida."""
    return sum(item.calcular_consumo_kwh() for item in lista)

def calcular_consumo_mensal(diario):
    """Multiplica o consumo diário por 30 para obter o valor mensal."""
    return diario * 30

def calcular_custo(consumo, preco=0.22):
    """Calcula o custo final multiplicando o consumo pelo preço do kWh."""
    return consumo * preco

def main():
    """Função principal que executa a lógica do programa."""
    # Carrega os dados simulados dos sensores
    inventario = carregar_dados_sensores("sensores.csv")
    
    # Verifica se o inventário tem dados antes de prosseguir
    if not inventario:
        sys.exit("Erro: Não foi possível carregar os dados do ficheiro 'sensores.csv'.")
    
    # Executa os cálculos matemáticos
    total_diario = calcular_consumo_total_diario(inventario)
    total_mensal = calcular_consumo_mensal(total_diario)
    custo_final = calcular_custo(total_mensal)
    
    # Apresenta os resultados de forma organizada
    print("--- RELATÓRIO ENERGÉTICO (GREEN DATA SCIENCE) ---")
    print(f"Consumo Diário Total: {total_diario:.2f} kWh")
    print(f"Consumo Mensal Estimado: {total_mensal:.2f} kWh")
    print(f"Custo Mensal Estimado (0.22€/kWh): {custo_final:.2f}€")

if __name__ == "__main__":
    main()
    