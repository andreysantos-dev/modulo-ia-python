# Este programa calcula o preço total de uma compra com tratamento de erros

def obter_float(mensagem):
    """Função para garantir que o usuário digite um número válido (float)."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número válido (use ponto para decimais).")

def obter_int(mensagem):
    """Função para garantir que o usuário digite um número inteiro válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número inteiro válido.")

# Solicita informações sobre o produto ao usuário
nome_produto = input("Digite o nome do Produto: ")
preco_unitario = obter_float("Digite o valor unitário do Produto: R$ ")
quantidade = obter_int("Digite a quantidade de Produtos: ")

# Calcula o preço total
preco_total = preco_unitario * quantidade

# Exibe o resultado formatado
print("\n--- RESUMO DA COMPRA ---")
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {preco_total:.2f}")