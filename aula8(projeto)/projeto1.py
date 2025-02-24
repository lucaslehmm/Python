# Projeto: Gerenciador de Senhas
# Objetivo: Desenvolver um programa que permita gerar, armazenar, consultar e gerenciar senhas de forma prática e segura.

#  Funcionalidades Detalhadas:
# 1. Gerar Senhas Seguras
#   O usuário poderá escolher:
# - Tamanho da senha (mínimo de 8 caracteres).
# - Incluir números, letras maiúsculas/minúsculas e/ou símbolos.
# - Opção de gerar uma senha totalmente aleatória.
# Exemplo: X@9dR!8zL#

# 2️. Armazenar Senhas
# O usuário insere o nome do serviço (Ex: "Gmail", "Netflix").
# A senha gerada ou personalizada é vinculada a esse nome.
# As senhas serão guardadas em uma estrutura de dados (como um dicionário: {"Gmail": "X@9dR!8zL#"}).

# 3️. Consultar Senhas Salvas
# O usuário poderá:
# - Pesquisar por nome do serviço.
# - Listar todas as senhas salvas.

# 4️. Editar ou Remover Senhas
# Permitir que o usuário:
# - Atualize a senha de um serviço.
# - Apague registros que não são mais necessários.

# 5️. Sair do Sistema
# O sistema deve encerrar o programa ao comando do usuário..
#           +-----------------------+
#           |   Iniciar Programa    |
#           +-----------------------+
#                      ↓
#           +-----------------------+
#           |   Exibir Menu:        |
#           | 1. Gerar Senha        |
#           | 2. Salvar Senha       |
#           | 3. Consultar Senhas   |
#           | 4. Editar/Remover     |
#           | 5. Sair               |
#           +-----------------------+
#                      ↓
#        +-------------+-------------+
#        |             |             |
#    Opção 1       Opção 2       Opção 3
# (Gerar Senha)  (Salvar Senha) (Consultar)
#        ↓             ↓             ↓
#   Gerar senha    Inserir Nome   Pesquisar
#  com critérios    + Senha      ou Listar
#        ↓             ↓             ↓
#    Exibir          Salvar       Mostrar
# Resultado        no Sistema     Resultado
#        ↓             ↓             ↓
#        +-------------+-------------+
#                      ↓
#              +--------------+
#              |   Continuar? |
#              +--------------+
#                ↓         ↓
#              Sim        Não
#                ↓         ↓
#            Volta ao    Sair do
#              Menu     Programa

##  Imports
import random
import string

## Varivei
MENU = ("O que deseja fazer \n"
        "1. Gerar senha \n"
        "2. Salvar senha \n"
        "3. Consultar senhas\n"
        "4. Editar/Remover \n"
        "5. Sair\n"
        )

ESCOLHAS_VALIDAS = ["1", "2", "3", "4", "5"]

TAMANHO_DE_SENHA_VALIDO = ["6", "7", "8", "9", "10", "11", "12"]

## Inicio do Programa

print('Olá! seja bem-vindo(a)')
print(MENU)

escolha_usuario = input('Digite sua escolha: ')

# Validar a escolha do usuario.

# Caso o usuario não digite nada.
while escolha_usuario == '':
    print('Você não digitou nada, por favor digite novamente.')
    escolha_usuario = input('Digite sua escolha: ')

# Caso o usuario digite algo fora do esperado
while escolha_usuario not in ESCOLHAS_VALIDAS:
    print('Escolha invalida, tente novamente por favor.')
    escolha_usuario = input('Digite sua escolha: ')

while escolha_usuario != "5":

    # 1. Gerar senha
    if escolha_usuario == "1":
        print("OK! Vamos gerar uma senha para você!")
        tamanho_senha_gerada = input("Qual tamanho a senha deve ter? (6 a 12 digitos): ")

        # Verificação se está vazio
        while tamanho_senha_gerada == '':
            print('Você não digitou nada, por favor digite novamente.')
            tamanho_senha_gerada = input('Qual tamanho a senha deve ter? (6 a 12 digitos): ')

        # Verificação se é um numero e se esta entre o tamanho valido
        while tamanho_senha_gerada not in TAMANHO_DE_SENHA_VALIDO:
            print('Você precisa digitar um número inteiro entre 6 a 12.')
            tamanho_senha_gerada = input('Qual tamanho a senha deve ter? (6 a 12 digitos): ')

        # Converte para número
        tamanho_senha_gerada = int(tamanho_senha_gerada)

        caracteres_aleatorios =  list(string.ascii_letters + string.digits + string.punctuation)
        senha_gerada = ''.join(random.choice(caracteres_aleatorios) for _ in range(tamanho_senha_gerada))

        print(f'Senha gerada com sucesso!\n'
              f'Sua senha é: {senha_gerada} \n')
        
        salvar_senha_gerada = input('Deseja salvar senha?[S]/[N]: ')

        #Apos a senha ser gerada, perguntar se o usuario deseja salvar a senha e guardar ela em uma lista.

        if salvar_senha_gerada == 's' or 'S':
            nome_senha_salva = input('De um nome para sua senha: ')
            print('Sua senha foi salva com sucesso!')
        elif salvar_senha_gerada == 'n' or "N":
            print('A senha não foi salva.')
        break

    ## Salvar senha
    elif escolha_usuario == "2":
        print('Certo, vamos armazenar sua senha.')
        senha_usuario = input('Digite a senha que quer salvar: ')
        nome_senha_usuario = input('Certo! Agora dê um nome para a sua senha (Ex: Netflix, Amazon, etc..): ')

        print(f'Senha salva com sucesso!\n'
              f'A senha de {nome_senha_usuario} é {senha_usuario} \n')
    
    ## Aprender a manipular listas e objetos para continuar...
        break
    elif escolha_usuario == "3":
        print("consultar senhas...")
        break
    elif escolha_usuario == "4":
        print("Editar remover...")
        break
    
print('Obrigado! Até logo.')

controle2 = input('controle2: ')