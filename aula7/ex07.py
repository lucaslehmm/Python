# Desafio Prático Combinação de Conceitos
# "Gerador de Senhas Simples"

# Peça ao usuário o tamanho desejado da senha.
# A senha deve conter números e letras aleatórias.
# Use for e concatenação de strings para montar a senha.

import random
import string

print('Olá! Vamos gerar uma senha segura!')
tamanho_da_senha = int(input('Digite  o tamanho da senha a ser gerada: '))

caracteres = list(string.ascii_letters + string.digits + string.punctuation)

senha = "".join(random.choice(caracteres) for _ in range(tamanho_da_senha))

print(senha)