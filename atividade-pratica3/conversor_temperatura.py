def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    """Converte Celsius para Kelvin."""
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    """Converte Fahrenheit para Kelvin."""
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    """Converte Kelvin para Celsius."""
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    """Converte Kelvin para Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32

# Início do programa principal
print("Bem-vindo ao Conversor de Temperatura!")

try:
    temperatura = float(input("Digite a temperatura: "))
    unidade_origem = input("Qual a unidade de origem? (C/F/K): ").upper()
    unidade_destino = input("Para qual unidade deseja converter? (C/F/K): ").upper()

    resultado = None

    if unidade_origem == "C":
        if unidade_destino == "F":
            resultado = celsius_para_fahrenheit(temperatura)
        elif unidade_destino == "K":
            resultado = celsius_para_kelvin(temperatura)
        else:
            resultado = temperatura
    elif unidade_origem == "F":
        if unidade_destino == "C":
            resultado = fahrenheit_para_celsius(temperatura)
        elif unidade_destino == "K":
            resultado = fahrenheit_para_kelvin(temperatura)
        else:
            resultado = temperatura
    elif unidade_origem == "K":
        if unidade_destino == "C":
            resultado = kelvin_para_celsius(temperatura)
        elif unidade_destino == "F":
            resultado = kelvin_para_fahrenheit(temperatura)
        else:
            resultado = temperatura
    else:
        print("Unidade de origem inválida.")

    if resultado is not None:
        print(f"\n{temperatura:.2f}°{unidade_origem} é igual a {resultado:.2f}°{unidade_destino}")
        
except ValueError:
    print("Entrada inválida. Por favor, digite um número para a temperatura.")