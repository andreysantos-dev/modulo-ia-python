def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Entrada de dados do usuário
total_conta = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

# Cálculo
gorjeta = calcular_gorjeta(total_conta, porcentagem)

# Saída formatada
print(f"Para uma conta de R${total_conta:.2f}, você deseja pagar {porcentagem:.2f}% de gorjeta = R${gorjeta:.2f}")
