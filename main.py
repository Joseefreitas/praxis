from usuarios import *


def menu_principal():
    while True:
        limpar_tela()
        print("==================================")
        print("       BEM-VINDO AO PRÁXIS")
        print("==================================")
        print("1 - Gerenciar usuários")
        print("2 - Auxiliar de prompts")
        print("0 - Sair")
        print("==================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_usuarios()

        elif opcao == "2":
            print("Auxiliador de prompts embreve")

        elif opcao == "0":
            print("Obrigador por usar práxi tchau!")
            break

        else:
            print("Opção invalida tente novamente")
        
if __name__ == "__main__":
    menu_principal()
