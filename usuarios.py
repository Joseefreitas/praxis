import os
import ast
import csv

COLUNAS = ("nome", "login", "senha", "utilizacao")
CAMINHO_ARQUIVO = "dados/usuarios.csv"


def limpar_tela():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


def menu_usuarios():

    while True:
        limpar_tela()

        print("Bem Vindo ao Programa da PRÁXIS")
        print("Este programa tem como objetivo de auxiliar na gestão de Prompts")
        print("Escolha uma das opções abaixo para continuar:")
        print("-------------------------------------")
        print("|    1 - Cadastrar Usuário           |")
        print("|    2 - Listar Usuários             |")
        print("|    3 - Atualizar Usuário           |")
        print("|    4 - Deletar Usuário             |")
        print("|    0 - Voltar ao Menu Principal    |")
        print("-------------------------------------")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            print("Você escolheu a opção 1 - Cadastrar Usuário")
            cadastrar_usuario()

        elif opcao == "2":
            print("Você escolheu a opção 2 - Listar Usuários")
            listar_usuarios()


        elif opcao == "3":
            print("Você escolheu a opção 3 - Atualizar Usuário")
            atualizar_usuario()

        elif opcao == "4":
            print("Você escolheu a opção 4 - Deletar Usuário")
            deletar_usuario()

        elif opcao == "0":
            print("\nVoltando ao menu principal. Até logo!\n")
            break

        else:
            print("\nOpção inválida. Digite um número de 0 a 5.")

        input("\nPressione ENTER para continuar...")


def cadastrar_usuario():
  usuario = {
      "nome": input("Digite o seu nome: ").strip(),
      "login": input("Digite o seu login: ").strip(),
      "senha": input("Digite a sua senha: "),
      "utilizacao": input("Como você vai utilizar? ").strip(),
  }

  os.makedirs("dados", exist_ok=True)
  arquivo_existe = os.path.isfile(CAMINHO_ARQUIVO)

  with open(CAMINHO_ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)

    if not arquivo_existe:
      escritor.writeheader()

    escritor.writerow(usuario)


def listar_usuarios():
  try:
    with open(CAMINHO_ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
      leitor = csv.DictReader(arquivo)

      for usuario in leitor:
        print(usuario["nome"])

  except FileNotFoundError:
    print("Arquivo de usuários não encontrado.")


def atualizar_usuario():
  try:
    with open(CAMINHO_ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
      usuarios = list(csv.DictReader(arquivo))
  except FileNotFoundError:
    print("Arquivo de usuários não encontrado.")
    return

  if not usuarios:
    print("Nenhum usuário cadastrado.")
    return

  login_busca = input("Digite o login do usuário que deseja atualizar: ")
  encontrado = False

  for usuario in usuarios:
    if usuario["login"] == login_busca:
      encontrado = True
      print(f"\nUsuário encontrado: {usuario['nome']}")
      print("Pressione ENTER caso queira manter o valor atual.\n")

      novo_nome = input(f"Novo nome ({usuario['nome']}): ").strip()
      novo_login = input(f"Novo login ({usuario['login']}): ").strip()
      nova_senha = input("Nova senha: ").strip()
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
    print("Usuário não encontrado.")
    return

  with open(CAMINHO_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)
    escritor.writeheader()
    escritor.writerows(usuarios)

  print("Usuário atualizado com sucesso!")


def deletar_usuario():
  try:
    with open(CAMINHO_ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
      usuarios = list(csv.DictReader(arquivo))
  except FileNotFoundError:
    print("Arquivo de usuários não encontrado.")
    return

  if not usuarios:
    print("Nenhum usuário cadastrado.")
    return

  login_busca = input("Digite o login do usuário que deseja deletar: ").strip()

  usuarios_restantes = [u for u in usuarios if u["login"] != login_busca]

  if len(usuarios_restantes) == len(usuarios):
    print("Usuário não encontrado.")
    return

  confirmacao = (
      input(f"Tem certeza que deseja deletar o login '{login_busca}'? (s/n): ")
      .strip()
      .lower()
  )
  if confirmacao != "s":
    print("Operação cancelada.")
    return

  with open(CAMINHO_ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=COLUNAS)
    escritor.writeheader()
    escritor.writerows(usuarios_restantes)

  print("Usuário deletado com sucesso!")