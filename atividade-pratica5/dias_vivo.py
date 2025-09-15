from datetime import datetime

# Solicita a data de nascimento
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte para objeto datetime
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Pega a data atual
data_atual = datetime.today()

# Calcula diferença em dias
dias_vivo = (data_atual - data_nascimento).days

# Exibe resultado
print(f"\nVocê está vivo há {dias_vivo} dias.")