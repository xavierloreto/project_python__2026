class Eletrodomestico:
    def __init__(self, nome, potencia, horas):
        self.nome = nome
        self.potencia = potencia
        self.horas_uso_diario = horas

    def calcular_consumo_kwh(self):
        return (self.potencia * self.horas_uso_diario) / 1000

def calcular_consumo_total_diario(lista):
    return sum(item.calcular_consumo_kwh() for item in lista)

def calcular_consumo_mensal(diario):
    return diario * 30

def calcular_custo(mensal, preco):
    return mensal * preco

def main():
    # Tudo o que está aqui abaixo tem de ter 4 espaços à esquerda
    preco_kwh = 0.22
    
    eletrodomesticos = [
        Eletrodomestico("Frigorifico", 150, 24),
        Eletrodomestico("Televisao", 120, 4),
        Eletrodomestico("Maquina de lavar", 2000, 0.5),
        Eletrodomestico("Forno", 2500, 0.3),
        Eletrodomestico("Computador", 300, 6)
    ]
    
    consumo_diario = calcular_consumo_total_diario(eletrodomesticos)
    consumo_mensal = calcular_consumo_mensal(consumo_diario)
    custo_mensal = calcular_custo(consumo_mensal, preco_kwh)
        
    print("Consumo diario total (kWh):", round(consumo_diario, 2))
    print("Consumo mensal total (kWh):", round(consumo_mensal, 2))
    print("Custo mensal estimado (€):", round(custo_mensal, 2))

if __name__ == "__main__":
    main()
