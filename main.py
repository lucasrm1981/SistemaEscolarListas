# Inicializa a matriz de alunos
alunos = alunos_lista =[]
# Função para cadastrar um novo aluno
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    turma = input("Digite a turma do aluno: ")
    media = float(input("Digite sua média "))

    # Adiciona os dados do aluno como uma lista dentro da matriz
    # atributos      0      1     2     3
    alunos_lista = {"Nome": nome, "Idade": idade, "Turma": turma, "Media": media}
    alunos.append([nome, idade, turma, media])
    
    print("Aluno cadastrado com sucesso!")

# Função para exibir todos os alunos cadastrados
def exibir_alunos():
    if not alunos: # Se o array estiver vazio
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de alunos:") # caso o array tenha algum aluno
        # Percorrer um array extenso como uma análise do conteúdo dele
        # start serve para exibir como indice 1, sendo pela lista inicia no 0
        for i, aluno in enumerate(alunos):
            print(f"Mat.{i} Nome: {aluno[0]}, Idade: {aluno[1]}, Turma: {aluno[2]}, Média: {aluno[3]}")


# Menu principal
while True: # Enquanto for TRUE verdadeiro
    print("\nMENU")    
    print("1. Cadastrar aluno")
    print("2. Exibir alunos")
    print("3. Buscar Alunos")
    print("4. Atualizar um aluno")
    print("5. Apagar um aluno")
    print("6. Verificar se Passou")
    print("7. Sair")
    # Faz a análise da opção enquanto for verdadeira
    opcao = input("Escolha uma opção: ")    
    
    if opcao == "1":
        cadastrar_aluno()
    
    elif opcao == "2":
        exibir_alunos()        
    
    elif opcao=="3": # Busca de um aluno
        buscar= input("Digite o Aluno que deseja buscar:\n")
        for i,row in enumerate(alunos):
            if row[0] == buscar:
                print(f"A turma dele é {row[2]}")
    
    elif opcao == "4":
        escolha = int(input("\nO que deseja Alterar:\n1. Nome\n2. Idade\n3. Turma\n4. Média\n"))
        mat = int(input("\nDigite a matricula do aluno: "))
        match escolha:
            case 1:
                print(f"{alunos[mat]}")
                n= input("Digite o Novo nome: ")
                alunos[mat][0] = n
                print(alunos[mat])                
            case 2:
                print(f"{alunos[mat]}")
                i=int(input("Digite a Idade: "))
                alunos[mat][1] = i
                print(alunos[mat])
            case 3:
                print(f"{alunos[mat]}")
                t=input("Digite a Turma: ")
                alunos[mat][2] = t
                print(alunos[mat])
            case 4:   
                print(f"{alunos[mat]}")
                m=float(input("Digite a Média: "))
                alunos[mat][3]=m
                print(alunos[mat])
        
    
    elif opcao=="5":# Verificar se passou através da média        
        for i, aluno in enumerate(alunos, start=1):
            if aluno[3]>7:
                print(f"{aluno[0]} você Passou")
            else:
                print(f"{aluno[0]} você Reprovou")   

    elif opcao == "6":
        apagar = int(input("Digite a matricula do Aluno: "))
        x = alunos.pop(apagar)

    elif opcao == "7":
        print("Saindo do programa...")
        break # Saida do Sistema
    else:
        print("Opção inválida. Tente novamente.")
