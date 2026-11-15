
import os
import csv

COLUNAS = ("nome", "login", "senha", "utilizacao")
COLUNAS_HISTORICO = ("login", "prompt", "analise")


def limpar_tela():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


def menu_usuarios():
    while True:
        limpar_tela()

        print("=====================================")
        print("       PRÁXIS | GERENCIAR USUÁRIOS")
        print("=====================================")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("0 - Voltar ao menu principal")
        print("=====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            atualizar_usuario()

        elif opcao == "4":
            deletar_usuario()

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")


def cadastrar_usuario():
    usuario = {
        "nome": input("Digite seu nome: ").strip(),
        "login": input("Digite seu login: ").strip(),
        "senha": input("Digite sua senha: "),
        "utilizacao": input("Como você vai utilizar o PRÁXIS? ").strip()
    }

    arquivo_existe = os.path.isfile("usuarios.csv")

    with open("usuarios.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)

        if not arquivo_existe:
            escritor.writeheader()

        escritor.writerow(usuario)

    print("\nUsuário cadastrado com sucesso!")


def listar_usuarios():
    try:
        with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            print("\n=== USUÁRIOS CADASTRADOS ===")

            for usuario in leitor:
                print(usuario["nome"])

    except FileNotFoundError:
        print("\nNenhum usuário cadastrado.")


def atualizar_usuario():
    try:
        with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
            usuarios = list(csv.DictReader(arquivo))

    except FileNotFoundError:
        print("\nNenhum usuário cadastrado.")
        return

    login_busca = input("Digite o login do usuário que deseja atualizar: ").strip()
    encontrado = False

    for usuario in usuarios:
        if usuario["login"] == login_busca:
            encontrado = True

            print(f"\nUsuário encontrado: {usuario['nome']}")
            print("Pressione ENTER para manter o valor atual.\n")

            novo_nome = input(f"Novo nome ({usuario['nome']}): ").strip()
            novo_login = input(f"Novo login ({usuario['login']}): ").strip()
            nova_senha = input("Nova senha: ")
            nova_utilizacao = input(
                f"Nova utilização ({usuario['utilizacao']}): "
            ).strip()

            if novo_nome:
                usuario["nome"] = novo_nome

            if novo_login:
                usuario["login"] = novo_login

            if nova_senha:
                usuario["senha"] = nova_senha

            if nova_utilizacao:
                usuario["utilizacao"] = nova_utilizacao

            break

    if not encontrado:
        print("\nUsuário não encontrado.")
        return

    with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)
        escritor.writeheader()
        escritor.writerows(usuarios)

    print("\nUsuário atualizado com sucesso!")


def deletar_usuario():
    try:
        with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
            usuarios = list(csv.DictReader(arquivo))

    except FileNotFoundError:
        print("\nNenhum usuário cadastrado.")
        return

    login_busca = input("Digite o login do usuário que deseja deletar: ").strip()

    usuario_encontrado = None

    for usuario in usuarios:
        if usuario["login"] == login_busca:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("\nUsuário não encontrado.")
        return

    senha = input("Digite sua senha para confirmar a exclusão: ")

    if senha != usuario_encontrado["senha"]:
        print("\nSenha incorreta. Exclusão cancelada.")
        return

    usuarios_restantes = [
        usuario for usuario in usuarios
        if usuario["login"] != login_busca
    ]

    with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)
        escritor.writeheader()
        escritor.writerows(usuarios_restantes)

    deletar_historico(login_busca)

    print("\nUsuário deletado com sucesso!")


def autenticar_usuario(login, senha):
    
    try:
        with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for usuario in leitor:
                if usuario["login"] == login and usuario["senha"] == senha:
                    return usuario

    except FileNotFoundError:
        return None

    return None


def salvar_historico(login, prompt, analise):
  
    from usuarios import (
    limpar_tela,
    menu_usuarios,
    autenticar_usuario,
    cadastrar_usuario,
    salvar_historico
)
    with open("historico.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS_HISTORICO)

        if arquivo.tell() == 0:
            escritor.writeheader()

        escritor.writerow({
            "login": login,
            "prompt": prompt,
            "analise": analise
        })


def consultar_historico(login):
    try:
        with open("historico.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            historico = []

            for registro in leitor:
                if registro["login"] == login:
                    historico.append(registro)

    except FileNotFoundError:
        print("\nVocê ainda não possui histórico de análises.")
        return

    if not historico:
        print("\nVocê ainda não possui histórico de análises.")
        return

    print("\n========== MEU HISTÓRICO ==========")

    for indice, registro in enumerate(historico, start=1):
        print(f"\nANÁLISE {indice}")
        print(f"\nPrompt: {registro['prompt']}")
        print(f"\nAnálise do PRÁXIS:\n{registro['analise']}")
        print("\n----------------------------------")


def deletar_historico(login):
    try:
        with open("historico.csv", "r", newline="", encoding="utf-8") as arquivo:
            historico = list(csv.DictReader(arquivo))

    except FileNotFoundError:
        return

    historico_restante = [
        registro for registro in historico
        if registro["login"] != login
    ]

    with open("historico.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS_HISTORICO)
        escritor.writeheader()
        escritor.writerows(historico_restante)
