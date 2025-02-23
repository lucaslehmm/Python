import string
import random

caracteres_aleatorios =  list(string.ascii_letters + string.digits + string.punctuation)

# tamanho_senha_gerada = input("Qual tamanho a senha deve ter?: ")
tamanho_senha_gerada = 8
caracteres_aleatorios =  list(string.ascii_letters + string.digits + string.punctuation)
senha_gerada = ''.join(random.choice(caracteres_aleatorios) for _ in range(tamanho_senha_gerada))

print(senha_gerada)