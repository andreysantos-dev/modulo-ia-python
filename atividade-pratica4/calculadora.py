def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

def calculadora():
    while True:
        print("\n--- Calculadora em Python ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == "5":
            print("Saindo da calculadora...")
            break

        if escolha in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, digite números válidos.")
                continue

            if escolha == "1":
                print("Resultado:", soma(num1, num2))
            elif escolha == "2":
                print("Resultado:", subtracao(num1, num2))
            elif escolha == "3":
                print("Resultado:", multiplicacao(num1, num2))
            elif escolha == "4":
                print("Resultado:", divisao(num1, num2))
        else:
            print("Opção inválida, tente novamente.")

# Executa a calculadora
calculadora()
