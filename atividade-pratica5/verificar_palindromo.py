import string

def verificar_palindromo(texto):
    # Coloca tudo em minúsculas
    texto = texto.lower()
    # Remove espaços e pontuação
    texto = ''.join(ch for ch in texto if ch.isalnum())
    # Verifica se é igual ao reverso
    if texto == texto[::-1]:
        return "Sim"
    else:
        return "Não"


# Exemplos de uso
print(verificar_palindromo("Ame a ema"))           # Sim
print(verificar_palindromo("Socorram-me subi no ônibus em Marrocos"))  # Sim
print(verificar_palindromo("Python"))             # Não
