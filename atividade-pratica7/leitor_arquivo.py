import csv

# Solicita o nome do arquivo ao usuário
arquivo = input("Informe o nome do arquivo CSV: ")

try:
    # Tenta abrir o arquivo
    with open(arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        
        # Percorre cada linha e exibe
        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print(f"Erro: o arquivo '{arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
