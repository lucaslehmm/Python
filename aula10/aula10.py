## Funções
# Funções são blocos de código que realizam tarefas específicas. Elas ajudam a organizar o código e evitam repetição.

## Sintaxe

# def nome_da_funcao(parâmetros):
#     # Bloco de código
#     return resultado


# def - palavra-chave para definir a função.
# nome_da_funcao - nome que você escolhe.
# parâmetros - dados que a função recebe (podem ser opcionais).
# return - valor que a função devolve (também pode ser opcional).

# Exemplo basico.
def saudacao():
    print('Olá, mundo!')

saudacao()

# Com parametro.
def saudacao_personalizada(nome):
    print(f'olá {nome}')

saudacao_personalizada("Lucas")

# Return
def soma(a, b):
    soma = a + b
    return soma

print(soma(1, 1))

# Valor padrao de parametro

def saudacao_padrao(nome = "visitante"):
    print(f'Olá {nome}')

saudacao_padrao()
saudacao_padrao('Lucas')

# Escopo

x = 10 # Escopo global

def mostra_valor():
    x = 5 # Escopo local (escopo da função será  priorizazado)
    print(x)

print(x)
mostra_valor()