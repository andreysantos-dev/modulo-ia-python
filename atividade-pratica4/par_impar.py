# Função para analisar os números digitados
def analisar_numeros():
    pares = 0   # contador de números pares
    impares = 0 # contador de números ímpares

    print("Digite números inteiros (digite 0 para encerrar):")

    while True:
        try:
            numero = int(input("Número: "))  # lê o número do usuário
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue  # volta para pedir outro número

        if numero == 0:  # condição de parada
            break

        if numero % 2 == 0:  # verifica se é par
            print(f"{numero} é PAR")
            pares += 1
        else:  # se não for par, é ímpar
            print(f"{numero} é ÍMPAR")
            impares += 1

    # Exibe o resultado final
    print("\n--- Resultado final ---")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


# --- PROGRAMA PRINCIPAL ---
analisar_numeros()
