import pandas as pd

def analisar_logs(caminho_csv):
    try:
        # Lendo o arquivo CSV
        df = pd.read_csv(caminho_csv)

        # Verificando se a coluna existe
        if "tempo_execucao" not in df.columns:
            print("Erro: a coluna 'tempo_execucao' não foi encontrada no arquivo.")
            return

        # Calculando média e desvio padrão
        media = df["tempo_execucao"].mean()
        desvio = df["tempo_execucao"].std()

        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f}")

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# Exemplo de uso
if __name__ == "__main__":
    analisar_logs("logs_treinamento.csv")
