# Função que verifica se a senha é segura
def verificar_senha(senha):
    # Critério A: verificar se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."
    
    # Critério B: verificar se a senha contém pelo menos um número
    if not any(char.isdigit() for char in senha):  
        return "A senha deve conter pelo menos um número."
    
    # Se passou em todos os critérios
    return "Senha válida! ✔️"

# --- PROGRAMA PRINCIPAL ---
senha = input("Digite uma senha para verificar: ")
resultado = verificar_senha(senha)
print(resultado)
