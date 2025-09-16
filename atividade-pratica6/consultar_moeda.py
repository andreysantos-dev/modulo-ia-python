import requests
from datetime import datetime

def consultar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        # A API retorna com a chave MOEDABRL, ex: USDBRL, EURBRL
        chave = f"{moeda}BRL"
        if chave not in dados:
            print("❌ Moeda não encontrada. Verifique o código informado.")
            return

        info = dados[chave]

        valor_atual = info["bid"]
        valor_maximo = info["high"]
        valor_minimo = info["low"]
        ultima_atualizacao = datetime.fromtimestamp(int(info["timestamp"]))

        print("✅ Cotação encontrada:")
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual : R$ {valor_atual}")
        print(f"Máximo      : R$ {valor_maximo}")
        print(f"Mínimo      : R$ {valor_minimo}")
        print("Última atualização:", ultima_atualizacao.strftime("%d/%m/%Y %H:%M:%S"))

    except requests.exceptions.RequestException:
        print("❌ Erro na conexão com a API.")

# Programa principal
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()
consultar_moeda(moeda)
