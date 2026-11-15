from usuarios import menu_usuarios, limpar_tela
from analisador import analisar_prompt


def menu_auxiliador():
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

        except ValueError as erro:
            print(f"\nErro: {erro}")

        except Exception as erro:
            print(f"\nNão foi possível realizar a análise: {erro}")

        opcao = input("\nDeseja analisar outro prompt? (s/n): ").strip().lower()

        if opcao != "s":
            break

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
            menu_auxiliador()

        elif opcao == "0":
            print("Obrigado por usar práxis! Até logo!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")
            input("\nPressione ENTER para continuar...")
        
if __name__ == "__main__":
    menu_principal()
