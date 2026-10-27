import os

os.system("cls || clear")

print("Bem Vindo ao Programa da PRÁXIS")
print("Este programa tem como objetivo de auxiliar na gestão de Prompts")
print("   Escolha uma das opções abaixo para continuar:")
print("----------------------------------")
print("|    1 - Cadastrar Usuário       |")
print("|    2 - Listar Usuários         |")
print("|    3 - Atualizar Usuário       |")
print("|    4 - Deletar Usuário         |")
print("|    5 - Sair do Programa        |")
print("----------------------------------")

opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    print("Você escolheu a opção 1 - Cadastrar Usuário")
elif opcao == "2":
    print("Você escolheu a opção 2 - Listar Usuários")
elif opcao == "3":
    print("Você escolheu a opção 3 - Atualizar Usuário")
elif opcao == "4":
    print("Você escolheu a opção 4 - Deletar Usuário")
elif opcao == "5":
    print("Você escolheu a opção 5 - Sair do Programa")
    print("\nSaindo do programa. Até logo!\n")
    False
   
else:
    print("\nOpção inválida. Por favor, digite um número válido de 1 a 5.\n")    

print("--Cadastrar Usuário--")
nome = input("Qual o seu nome?: ")
nome_usuario = input("Qual vai ser o seu nome de usuario?: ")
senha = input("Crie uma senha: ")


print("--Listar Usuários--")
nome_usuario = input("Qual o seu nome completo ou nome de usuario?: ")
senha = input("Qual a sua senha?: ")

print("--Atualizar conta--")
novo_nome = input("Qual o novo nome?: ")
novo_nome_usuario = input("Qual vai ser o novo nome de usuario?: ")
nova_senha = input("Escreva sua nova senha: ")

print("--Remover Conta--")
usuario_remover = input("Digite seu usuário: ")
senha_confirmacao = input("Digite sua senha: ")
print("--Conta Removida--")