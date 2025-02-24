##  Imports
import random
import string

## Variveis
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
print('Olá! seja bem-vindo(a) ao Gerador de Senhas!')
chave_de_controle = input("Presione [S] para iniciar o programa: ")

# Validar escolha de inicialização
if chave_de_controle.lower() == "s":
    chave_de_controle = True

    senhas = {

    }

    # Programa vai rodar enquanto a chave de controle estiver ligada.
    while chave_de_controle == True:
        print(MENU)

        escolha_usuario = input('Digite sua escolha: ')

        # Caso o usuario não digite nada.
        while escolha_usuario == '':
            print('Você não digitou nada, por favor digite novamente.')
            escolha_usuario = input('Digite sua escolha: ')

        # Caso o usuario digite algo fora do esperado
        while escolha_usuario not in ESCOLHAS_VALIDAS:
            print('Escolha invalida, tente novamente por favor.')
            escolha_usuario = input('Digite sua escolha: ')

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

            # Gerador de senha:
            caracteres_aleatorios =  list(string.ascii_letters + string.digits + string.punctuation)
            senha_gerada = ''.join(random.choice(caracteres_aleatorios) for _ in range(tamanho_senha_gerada))

            print(f'Senha gerada com sucesso!\n'
                f'Sua senha é: {senha_gerada} \n')
            
            salvar_senha_gerada = input('Deseja salvar senha?[S]: ')

            # Salvar senha
            if salvar_senha_gerada.lower() == 's':
                nome_senha_salva = input('De um nome para sua senha: ')

                senhas.update({nome_senha_salva : senha_gerada})

                print(f'Sua senha "{nome_senha_salva}" foi salva com sucesso!')
            else:
                print('A senha não foi salva.')
            

        ## Salvar senha
        elif escolha_usuario == "2":
            print('Certo, vamos armazenar sua senha.')
            senha_usuario = input('Digite a senha que quer salvar: ')
            nome_senha_usuario = input('Certo! Agora dê um nome para a sua senha (Ex: Netflix, Amazon, etc..): ')

            senhas.update({nome_senha_usuario : senha_usuario})

            print(f'Senha salva com sucesso!\n'
                f'A senha de {nome_senha_usuario} é {senha_usuario} \n')
            
        elif escolha_usuario == "3":
            print('Senhas salvas:')
            print(senhas.items())
            
        elif escolha_usuario == "4":
            print("Certo, qual senha você deseja remover: ")

        # Verificação de saida.
        chave_de_controle = input("Deseja continuar?[S]: ")
        if chave_de_controle.lower() == "s":
            chave_de_controle = True
        else:
            chave_de_controle = False
            

print('Obrigado! Até logo.')

controle2 = input('controle2: ')