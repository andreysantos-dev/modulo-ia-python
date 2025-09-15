# Programa para calcular preço final com desconto

# Solicita valores ao usuário
preco_original = float(input("Digite o preço original do produto: R$ "))
desconto_percentual = float(input("Digite o percentual de desconto (%): "))

# Cálculo do desconto
valor_desconto = preco_original * (desconto_percentual / 100)

# Preço final após desconto
preco_final = preco_original - valor_desconto

# Exibe o resultado formatado
print(f"\nPreço original: R$ {preco_original:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")
