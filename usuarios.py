
import os

usuarios = []


def limpar_tela():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


def menu_usuarios():

    while True:
        limpar_tela()

        print("Bem Vindo ao Programa da PRÁXIS")
        print("Este programa tem como objetivo de auxiliar na gestão de Prompts")
        print("   Escolha uma das opções abaixo para continuar:")
        print("---------------------------------------")
        print("|    1 - Entrar Com Usuário Existente |")
        print("|    2 - Cadastrar Usuário            |")
        print("|    3 - Listar Usuários              |")
        print("|    4 - Atualizar Usuário            |")
        print("|    5 - Deletar Usuário              |")
        print("|    0 - Voltar ao Menu Principal     |")
        print("---------------------------------------")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            print("Você escolheu a opção 1 - Entrar Com Usuário Existente")

        elif opcao == "2":
            print("Você escolheu a opção 2 - Cadastrar Usuário")
            cadastrar_usuario()
            print(usuarios)

        elif opcao == "3":
            print("Você escolheu a opção 3 - Listar Usuários")

        elif opcao == "4":
            print("Você escolheu a opção 4 - Atualizar Usuário")

        elif opcao == "5":
            print("Você escolheu a opção 5 - Deletar Usuário")

        elif opcao == "0":
            print("\nVoltando ao menu principal. Até logo!\n")
            break

        else:
            print("\nOpção inválida. Digite um número de 0 a 5.")

        input("\nPressione ENTER para continuar...")


def cadastrar_usuario():
    usuario = {}
    print("Digite o seu nome")
    usuario["nome"] = input("")
    print("Digite o seu login")
    usuario["login"] = input("")
    print("Digite a sua senha")
    usuario["senha"] = input("")
    print("Como você vai utilizar?")
    usuario["utilizacao"] = input("")

    usuarios.append(usuario)

def listar_usuarios():
    print()

# print("--Cadastrar Usuário--")
# nome = input("Qual o seu nome?: ")
# nome_usuario = input("Qual vai ser o seu nome de usuario?: ")
# senha = input("Crie uma senha: ")


# print("--Listar Usuários--")
# nome_usuario = input("Qual o seu nome completo ou nome de usuario?: ")
# senha = input("Qual a sua senha?: ")

# print("--Atualizar conta--")
# novo_nome = input("Qual o novo nome?: ")
# novo_nome_usuario = input("Qual vai ser o novo nome de usuario?: ")
# nova_senha = input("Escreva sua nova senha: ")

# print("--Remover Conta--")
# usuario_remover = input("Digite seu usuário: ")
# senha_confirmacao = input("Digite sua senha: ")
# print("--Conta Removida--")