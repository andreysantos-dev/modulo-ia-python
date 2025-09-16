import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Gera erro se a resposta não for 200
        dados = resposta.json()

        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("✅ Usuário encontrado:")
        print("Nome :", nome)
        print("E-mail:", email)
        print("País :", pais)

    except requests.exceptions.RequestException:
        print("❌ Falha ao conectar à API. Verifique sua conexão.")

# Programa principal
buscar_usuario()
