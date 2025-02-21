## Introdução a bibliotecas de código.

#para importar uma biblioteca use "import nome da biblioteca"

import random

# random - A biblioteca random é usada para gerar números ou escolher itens de forma aleatória.

# Funções mais usadas:

# 1. random.choice(lista) → Escolhe um elemento aleatório de uma lista, string ou tupla.

frutas = ['morango', 'maça', 'pera', 'laranja']

print(random.choice(frutas))

# 2. random.randint(inicio, fim) → Gera um número inteiro aleatório entre o valor inicial e final.

print(random.randint(1, 10))

# 3. random.sample(lista, k) → Retorna k elementos únicos aleatórios de uma lista.

lista = list(range(1,11))

print(random.sample(lista, 3))

# 4.random.shuffle(lista) → Embaralha os elementos de uma lista.

cartas = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Q", "J", "K"]

random.shuffle(cartas)

print(cartas)
