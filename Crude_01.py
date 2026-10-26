# telas de inicio do programa
import os
os.system("cls || clear")  # Limpa a tela do terminal

print("Bem Vindo ao Programa da PRAXIS")
print("Este programa tem como objetivo de auxiliar na gestão de Prompts")
print("   Escolha uma das opções abaixo para continuar:")
print("----------------------------------")
print("|    1 - Cadastrar Usuário       |")
print("|    2 - Listar Usuários         |")
print("|    3 - Atualizar Usuário       |")
print("|    4 - Deletar Usuário         |")
print("|    5 - Sair do Programa        |")
print("----------------------------------")

# escolha da opção do usuário
opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    print("Você escolheu a opção 1 - Cadastrar Usuário")
    # Aqui você pode adicionar o código para cadastrar um usuário
elif opcao == "2":
    print("Você escolheu a opção 2 - Listar Usuários")
    # Aqui você pode adicionar o código para listar os usuários
elif opcao == "3":
    print("Você escolheu a opção 3 - Atualizar Usuário")
    # Aqui você pode adicionar o código para atualizar um usuário
elif opcao == "4":
    print("Você escolheu a opção 4 - Deletar Usuário")
    # Aqui você pode adicionar o código para deletar um usuário
elif opcao == "5":
    print("Você escolheu a opção 5 - Sair do Programa")
    print("\nSaindo do programa. Até logo!\n")
   
    # Aqui você pode adicionar o código para sair do programa
else:
    print("\nOpção inválida. Por favor, digite um número válido de 1 a 5.\n")    