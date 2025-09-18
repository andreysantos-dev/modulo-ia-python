import pandas as pd

def criar_csv():
    # Dados fictícios
    dados = {
        "Nome": ["Ana", "Bruno", "Carla", "Diego", "Fernanda"],
        "Idade": [25, 30, 22, 28, 35],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador"]
    }

    # Criando DataFrame
    df = pd.DataFrame(dados)

    # Pergunta ao usuário o nome do arquivo
    caminho_arquivo = input("Digite o nome do arquivo CSV para salvar (exemplo: pessoas.csv): ")

    try:
        # Salvando em CSV
        df.to_csv(caminho_arquivo, index=False)
        print(f"Arquivo '{caminho_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

# Programa principal
if __name__ == "__main__":
    criar_csv()
