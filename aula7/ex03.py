# Senha correta:
# Crie um programa que peça ao usuário uma senha.

# A senha correta é 1234.
# O programa deve continuar pedindo a senha até que o usuário acerte.
# Quando acertar, exiba a mensagem "Acesso permitido!".

senha = input('Digite a senha: ')

while senha != "1234":
    senha = input('Acesso negado. Digite novamente: ')

print("Acesso permitido!")