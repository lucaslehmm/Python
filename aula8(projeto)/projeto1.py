##  Imports
import random
import string

## Variveis
MENU = ("O que deseja fazer \n"
        "[1] Gerar senha \n"
        "[2] Salvar senha \n"
        "[3] Consultar senhas\n"
        "[4] Editar/Remover \n"
        "[5] Sair\n"
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
            if not senhas:
                print("Nenhuma senha salva ainda.")
            else:
                print("Senhas salvas:")
                for nome, senha in senhas.items():
                    print(f"{nome}: {senha}")
            
        ## Editar ou Remover Senhas
        elif escolha_usuario == "4":
            if not senhas:
                print("Nenhuma senha salva ainda.")
            else:
                ESCOLHAS_VALIDAS_OPCAO_4 = ['1', '2']

                print('O que deseja fazer?\n'
                    '[1] Editar senha\n'
                    '[2] Remover senha')
                
                escolha_opcao_4 = input('Digite a opcão desejada: ')

                # Verificação se está vazio
                while escolha_opcao_4 == '':
                    print('Você não digitou nada, por favor digite novamente.')
                    print('O que deseja fazer?\n'
                    '[1] Editar senha\n'
                    '[2] Remover senha')
                    escolha_opcao_4 = input('Digite a opcão desejada: ')

                # Verificação se é um numero e se esta entre o tamanho valido
                while escolha_opcao_4 not in ESCOLHAS_VALIDAS_OPCAO_4:
                    print('Você precisa escolher entre a opção 1 ou 2.')
                    print('O que deseja fazer?\n'
                    '[1] Editar senha\n'
                    '[2] Remover senha')
                    escolha_opcao_4 = input('Digite a opcão desejada: ')

                ## Editar senha
                if escolha_opcao_4 == '1':

                    alterando_senha = True

                    while alterando_senha == True:

                        for nome, senha in senhas.items():
                            print(f"{nome}: {senha}")

                        editar_senha = input('Qual a senha deseja alterar?: ')

                        #Verifica se essa senha está salva
                        while editar_senha not in senhas.keys():
                            print(f'Não há nenhuma senha salva com o nome de "{editar_senha}"')

                            print('Senhas salvas:')
                            for nome, senha in senhas.items():
                                print(f"{nome}: {senha}")

                            editar_senha = input('Qual a senha deseja alterar?: ')
                            

                        print('O que deseja fazer?\n'
                            '[1] Alterar nome\n'
                            '[2] Alterar senha')
                        sub_escolha_opcao_4 = input('Digite a opcão desejada: ')

                        # Verificação se está vazio
                        while sub_escolha_opcao_4 == '':
                            print('Você não digitou nada, por favor digite novamente.')
                            print('O que deseja fazer?\n'
                            '[1] Alterar nome\n'
                            '[2] Alterar senha')
                            sub_escolha_opcao_4 = input('Digite a opcão desejada: ')

                        # Verificação se esta valido
                        while sub_escolha_opcao_4 not in ESCOLHAS_VALIDAS_OPCAO_4:
                            print('Você precisa escolher entre a opção 1 ou 2.')
                            print('O que deseja fazer?\n'
                            '[1] Alterar nome\n'
                            '[2] Alterar senha')
                            sub_escolha_opcao_4 = input('Digite a opcão desejada: ')

                        if sub_escolha_opcao_4 == '1':
                            novo_nome_senha = input('Qual o novo nome da senha?: ')

                            valor_senha_editada = senhas.pop(editar_senha)

                            senhas.update({novo_nome_senha : valor_senha_editada})

                            print(f'A senha "{editar_senha}" teve seu nome alterado para "{novo_nome_senha}."')

                        if sub_escolha_opcao_4 == '2':
                            nova_senha = input(f'Digite a nova senha para "{editar_senha}": ')

                            senha_antiga = senhas.get(editar_senha)

                            senhas.update({editar_senha : nova_senha})

                            print(f'A senha de {editar_senha} foi alterada de "{senha_antiga}" para "{nova_senha}"')

                            
                        # Verificação de saida.
                        alterando_senha = input("Deseja continuar editando?[S]: ")
                        if alterando_senha.lower() == "s":
                            alterando_senha = True
                        else:
                            alterando_senha = False
                        

                if escolha_opcao_4 == '2':
                    print('Senhas salvas:')
                    for nome, senha in senhas.items():
                            print(f"{nome}: {senha}")
                    print("Qual senha você deseja remover?")
                    remover_senha = input("Digite o nome da senha: ")

                    while remover_senha not in senhas.keys():
                        print(f'Não existe nenhuma senha salva com o nome "{remover_senha}" ')
                        print('Senhas salvas:')
                        for nome, senha in senhas.items():
                            print(f"{nome}: {senha}")
                        print("Qual senha você deseja remover?")
                        remover_senha = input("Digite o nome da senha: ")
                        
                    # Confirmar remoção
                    confirmar_remocao = input('Confirma remoção da senha? [S]')

                    if confirmar_remocao.lower() == 's':
                        senhas.pop(remover_senha)
                        print(f'Senha "{remover_senha}" removida com sucesso!')
                    else:
                        print(f'A senha "{remover_senha}" não foi removida. ')

        elif escolha_usuario == "5":
            break
    

        # Verificação de saida.
        chave_de_controle = input("Deseja continuar?[S]: ")
        if chave_de_controle.lower() == "s":
            chave_de_controle = True
        else:
            chave_de_controle = False
            

print('Obrigado! Até logo.')