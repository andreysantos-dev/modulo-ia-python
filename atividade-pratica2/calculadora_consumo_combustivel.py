# Calculadora de consumo de combustível

# Dados da viagem
distancia_percorrida = int(input("Digite a distância percorrida em km: "))
combustivel_gasto = int(input("Digite a quantidade gasta de combustível em Litros: "))

# Cálculo do consumo
consumo = distancia_percorrida / combustivel_gasto

# Exibição do resultado
print("\nDados da Viagem:")
print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litro(s)")
print(f"Consumo Médio: {consumo:.2f} km/l")