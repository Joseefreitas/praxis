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

    if not usuario["nome"] or not usuario["login"] or not usuario["senha"]:
        print("\nNome, login e senha são obrigatórios.")
        return

    try:
        with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
            for registro in csv.DictReader(arquivo):
                if registro["login"] == usuario["login"]:
                    print("\nEsse login já está cadastrado. Escolha outro.")
                    return
    except FileNotFoundError:
        pass

    with open("usuarios.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)

        if arquivo.tell() == 0:
            escritor.writeheader()

        escritor.writerow(usuario)

    print("\nUsuário cadastrado com sucesso!")


def listar_usuarios():
    try:
        with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
            usuarios = list(csv.DictReader(arquivo))
    except FileNotFoundError:
        print("\nNenhum usuário cadastrado.")
        return

    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return

    print("\n=== USUÁRIOS CADASTRADOS ===")
    for usuario in usuarios:
        print(usuario["nome"])


def atualizar_usuario():
    try:
        with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
            usuarios = list(csv.DictReader(arquivo))
    except FileNotFoundError:
        print("\nNenhum usuário cadastrado.")
        return

    login_busca = input("Digite o login do usuário que deseja atualizar: ").strip()
    usuario_alvo = None

    for usuario in usuarios:
        if usuario["login"] == login_busca:
            usuario_alvo = usuario
            break

    if not usuario_alvo:
        print("\nUsuário não encontrado.")
        return

    print(f"\nUsuário encontrado: {usuario_alvo['nome']}")
    print("Pressione ENTER para manter o valor atual.\n")

    novo_nome = input(f"Novo nome ({usuario_alvo['nome']}): ").strip()
    novo_login = input(f"Novo login ({usuario_alvo['login']}): ").strip()
    nova_senha = input("Nova senha: ")
    nova_utilizacao = input(
        f"Nova utilização ({usuario_alvo['utilizacao']}): "
    ).strip()

    if novo_login and novo_login != login_busca:
        for registro in usuarios:
            if registro["login"] == novo_login:
                print("\nEsse login já está sendo utilizado.")
                return

    if novo_nome:
        usuario_alvo["nome"] = novo_nome
    if novo_login:
        usuario_alvo["login"] = novo_login
    if nova_senha:
        usuario_alvo["senha"] = nova_senha
    if nova_utilizacao:
        usuario_alvo["utilizacao"] = nova_utilizacao

    with open("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)
        escritor.writeheader()
        escritor.writerows(usuarios)

    if novo_login and novo_login != login_busca:
        try:
            with open("historico.csv", "r", newline="", encoding="utf-8") as arquivo:
                historico = list(csv.DictReader(arquivo))

            for registro in historico:
                if registro["login"] == login_busca:
                    registro["login"] = novo_login

            with open("historico.csv", "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS_HISTORICO)
                escritor.writeheader()
                escritor.writerows(historico)
        except FileNotFoundError:
            pass

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
            for usuario in csv.DictReader(arquivo):
                if usuario["login"] == login and usuario["senha"] == senha:
                    return usuario
    except FileNotFoundError:
        return None

    return None


def salvar_historico(login, prompt, analise):
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
            historico = [
                registro for registro in csv.DictReader(arquivo)
                if registro["login"] == login
            ]
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


def buscar_usuario(login):
    try:
        with open("usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
            for usuario in csv.DictReader(arquivo):
                if usuario["login"] == login:
                    return usuario
    except FileNotFoundError:
        return None
    return None