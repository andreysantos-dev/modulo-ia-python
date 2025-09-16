import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres possíveis
    letras = string.ascii_letters  # a-z e A-Z
    numeros = string.digits        # 0-9
    simbolos = string.punctuation  # !@#$%...

    # Garante que tenha pelo menos 1 de cada tipo
    senha = [
        random.choice(letras),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Completa o restante da senha com caracteres aleatórios de todos os tipos
    todos_caracteres = letras + numeros + simbolos
    senha += random.choices(todos_caracteres, k=tamanho - len(senha))

    # Embaralha a senha para não ficar previsível
    random.shuffle(senha)

    return "".join(senha)

# Programa principal
tamanho = int(input("Digite o tamanho da senha desejada: "))

if tamanho < 4:
    print("⚠️ O tamanho mínimo recomendado é 4 para garantir segurança.")
else:
    senha_gerada = gerar_senha(tamanho)
    print("🔑 Senha gerada:", senha_gerada)
