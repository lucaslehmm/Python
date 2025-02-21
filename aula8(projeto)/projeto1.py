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

## Variveis

MENU = ("O que deseja fazer \n"
        "1. Gerar senha \n"
        "2. Salvar senha \n"
        "3. Consultar senhas\n"
        "4. Editar/Remover \n"
        "5. Sair\n"
        )

escolhas_validas = ["1", "2", "3", "4", "5"]

## Inicio do Programa

print('Olá! seja bem-vindo(a)')
print(MENU)

escolha_usuario = input('Digite sua escolha: ')

# Validar a escolha do usuario.

# Caso o usuario não digite nada.
while escolha_usuario == '':
    print('você não digitou nada, por favor digite novamente.')
    escolha_usuario = input('Digite sua escolha: ')

# Caso o usuario digite algo fora do esperado
while escolha_usuario not in escolhas_validas:
    print('Escolha invalida, tente novamente por favor.')
    escolha_usuario = input('Digite sua escolha: ')

while escolha_usuario != "5":

    # 1. Gerar senha
    if escolha_usuario == "1":
        print("gerar senha...")
        break
    elif escolha_usuario == "2":
        print("salvar senha...")
        break
    elif escolha_usuario == "3":
        print("consultar senhas...")
        break
    elif escolha_usuario == "4":
        print("Editar remover...")
        break
    
print('Obrigado! Até logo.')

controle2 = input('controle2: ')