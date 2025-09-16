import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        # Se o CEP não existir, a API retorna {"erro": true}
        if "erro" in dados:
            print("❌ CEP não encontrado.")
            return

        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        print("✅ Resultado da consulta:")
        print("Logradouro:", logradouro)
        print("Bairro    :", bairro)
        print("Cidade    :", cidade)
        print("Estado    :", estado)

    except requests.exceptions.RequestException:
        print("❌ Falha na conexão com a API. Verifique sua internet.")

# Programa principal
cep = input("Digite o CEP (apenas números): ").strip()
consultar_cep(cep)
