# Discoteca Pessoal
from datetime import date 
discoteca = {}

def adicionar():
    titulo = input("Qual Disco Deseja Adicionar?")
    autor = input("Qual o Autor da Obra?")
    discoteca[titulo] = autor
    print("Disco Adicionado Com Sucesso!")

def case():
    if discoteca:
        print("Seu Case de Discos:")
        print("-" * 30)
        for titulo, autor in discoteca.items():
            print(f"{titulo} - {autor}")
            print("-" * 30)
    else:
        print("Nenhum disco encontrado.")

def pesquisar():
    titulo = input("Qual Disco Está Procurando?")
    if titulo in discoteca:
        print("-" * 30)
        print(f"Disco: {titulo} - Autor: {discoteca[titulo]}")
        print("-" * 30)
    else:
        print("Disco não encontrado.")

def deletar():
    titulo = input("Qual Disco Deseja Deletar?")
    if titulo in discoteca:
        del discoteca[titulo]
        print("-" * 30)
        print("O Disco Foi Deletado Com Sucesso")
        print("-" * 30)
    else:
        print("-" * 30)
        print("Obra Não Foi Encontrada")
        print("-" * 30)

def menu():
    print("1. Para adicionar novos discos")
    print("2. Para ver o meu case")
    print("3. Para pesquisar algum disco")
    print("4. Para deletar algum disco")
    print("5. Fechar o meu case")

def finalizar():
    print("1. Sim")
    print("2. Não")

def loop():
    while True:
        menu()
        escolha = input("Escolha uma Opção: ")
        
        if escolha == "1":
            adicionar()
        elif escolha == "2":
            case()
        elif escolha == "3":
            pesquisar()
        elif escolha == "4":
            deletar()
        elif escolha == "5":
            print("Até a Próxima")
            break
        
        finalizar()
        final = input("Deseja Mais Alguma Coisa? (1 para Sim, 2 para Não): ")
        if final == "2":
            print("Até A Próxima")
            break

loop()
