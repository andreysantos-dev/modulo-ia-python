# Função para registrar as notas dos alunos
def registrar_notas():
    alunos = {}  # Dicionário para armazenar no formato {nome: [lista_de_notas]}
    qtd_alunos = int(input("Quantos alunos deseja registrar? "))  # Pergunta quantos alunos no total

    # Loop para registrar cada aluno
    for i in range(qtd_alunos):
        nome = input(f"\nDigite o nome do {i+1}º aluno: ")  # Pede o nome do aluno
        notas = []  # Lista para guardar as notas desse aluno
        qtd_notas = int(input(f"Quantas notas deseja registrar para {nome}? "))  # Pergunta quantas notas esse aluno terá

        # Loop para registrar as notas do aluno
        for j in range(qtd_notas):
            while True:  # Garante que só sai quando digitar uma nota válida
                try:
                    nota = float(input(f"Digite a {j+1}ª nota de {nome}: "))  # Pede a nota
                    if 0 <= nota <= 10:  # Verifica se a nota está entre 0 e 10
                        notas.append(nota)  # Adiciona a nota na lista
                        break  # Sai do while e vai para a próxima nota
                    else:
                        print("A nota deve estar entre 0 e 10.")  # Aviso caso esteja fora do intervalo
                except ValueError:  # Caso o usuário digite algo que não seja número
                    print("Digite um número válido.")
        
        alunos[nome] = notas  # Adiciona no dicionário o aluno e suas notas
    
    return alunos  # Retorna o dicionário de alunos com as notas


# Função para calcular as médias dos alunos e da turma
def calcular_medias(alunos):
    medias = {}  # Dicionário para guardar a média de cada aluno
    soma_turma = 0  # Vai acumular a soma de todas as notas da turma
    qtd_turma = 0  # Vai contar quantas notas foram registradas no total

    # Percorre cada aluno e suas notas
    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)  # Calcula a média do aluno (soma das notas dividido pela quantidade)
        medias[nome] = media  # Salva a média do aluno no dicionário
        soma_turma += sum(notas)  # Soma todas as notas desse aluno na soma geral da turma
        qtd_turma += len(notas)  # Conta quantas notas esse aluno teve para somar no total da turma

    # Calcula a média geral da turma (soma de todas as notas dividido pela quantidade total de notas)
    media_turma = soma_turma / qtd_turma if qtd_turma > 0 else 0
    return medias, media_turma  # Retorna o dicionário com as médias e a média da turma


# --- PROGRAMA PRINCIPAL ---

# Primeiro registra os alunos e suas notas
alunos = registrar_notas()

# Calcula as médias individuais e a média da turma
medias, media_turma = calcular_medias(alunos)

# Mostra os resultados finais
print("\n--- Resultados ---")
for nome, media in medias.items():
    print(f"{nome}: média = {media:.2f}")  # Mostra a média de cada aluno com 2 casas decimais

print(f"\nMédia da turma: {media_turma:.2f}")  # Mostra a média da turma
