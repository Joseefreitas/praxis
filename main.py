from usuarios import menu_usuarios, limpar_tela, cadastrar_usuario, autenticar_usuario, salvar_historico, consultar_historico
from analisador import analisar_prompt


def menu_auxiliador(usuario=None):
    while True:
        limpar_tela()

        print("==================================")
        print("       PRÁXIS | AUXILIADOR")
        print("==================================")

        prompt = input("\nDigite seu prompt: ")

        try:
            resultado = analisar_prompt(prompt)

            print("\n=== ANÁLISE DO PRÁXIS ===\n")
            print(resultado)

            if usuario:
                salvar_historico(usuario["login"], prompt, resultado)
                print("\nAnálise salva no seu histórico!")

        except ValueError as erro:
            print(f"\nErro: {erro}")

        except Exception as erro:
            print(f"\nNão foi possível realizar a análise: {erro}")

        opcao = input("\nDeseja analisar outro prompt? (s/n): ").strip().lower()

        if opcao != "s":
            break

def menu_principal(usuario=None):
    while True:
        limpar_tela()

        print("==================================")
        print("       BEM-VINDO AO PRÁXIS")
        print("==================================")

        if usuario:
            print(f"Olá, {usuario['nome']}!")
            print("1 - Gerenciar usuários")
            print("2 - Auxiliar de prompts")
            print("3 - Meu histórico")
        else:
            print("Acesso anônimo")
            print("1 - Auxiliar de prompts")

        print("0 - Sair")
        print("==================================")

        opcao = input("Escolha uma opção: ")

        if usuario and opcao == "1":
            menu_usuarios()

        elif (usuario and opcao == "2") or (usuario is None and opcao == "1"):
            menu_auxiliador(usuario)

        elif usuario and opcao == "3":
            limpar_tela()
            consultar_historico(usuario["login"])
            input("\nPressione ENTER para voltar ao menu...")

        elif opcao == "0":
            print("\nObrigado por utilizar o PRÁXIS! Até logo!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar...")


def menu_entrada():
    while True:
        limpar_tela()

        print("==================================")
        print("       BEM-VINDO AO PRÁXIS")
        print("==================================")
        print("1 - Entrar")
        print("2 - Cadastrar usuário")
        print("3 - Utilizar anonimamente")
        print("0 - Sair")
        print("==================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login = input("Digite seu login: ").strip()
            senha = input("Digite sua senha: ")

            usuario = autenticar_usuario(login, senha)

            if usuario:
                return usuario

            print("\nLogin ou senha incorretos.")
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            cadastrar_usuario()
            input("\nPressione ENTER para continuar...")

        elif opcao == "3":
            return None

        elif opcao == "0":
            print("\nObrigado por utilizar o PRÁXIS! Até logo!")
            return False

        else:
            print("\nOpção inválida. Tente novamente.")
            input("\nPressione ENTER para continuar...")

        
if __name__ == "__main__":
    usuario = menu_entrada()

    if usuario is not False:
        menu_principal(usuario)
