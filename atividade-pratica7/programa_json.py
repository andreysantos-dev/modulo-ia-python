import json
import os

# Dados que vamos salvar
dados = {
    "nome": "Andrey",
    "idade": 25,
    "cidade": "São Paulo"
}

arquivo = "dados.json"

# --- Escrita do arquivo JSON ---
try:
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"Arquivo '{arquivo}' salvo com sucesso!")
except Exception as e:
    print(f"Falha ao salvar o arquivo: {e}")

# --- Leitura do arquivo JSON ---
try:
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = json.load(f)
            print("\n📖 Dados lidos do arquivo:")
            for chave, valor in conteudo.items():
                print(f"{chave.capitalize()}: {valor}")
    else:
        print(f"Erro: o arquivo '{arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Falha ao ler o arquivo: {e}")
