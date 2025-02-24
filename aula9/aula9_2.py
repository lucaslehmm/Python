## Parte 3 - Conjuntos
# Conjuntos (set) - Conjuntos armazenam valores únicos, ou seja, não permitem duplicatas e não têm ordem definida.

set1 = {1, 4, 5, 6, 8}
set2 = {4, 6, 7, 3, 2}

# Metodos uteis
# add(item) - Adiciona um item ao final do conjunto.
set1.add(11)
print(set1)

# remove(item) - Remove o item (erro se não existir).
set1.remove(11)
print(set1)

# discard(item) - Remove o item (sem erro se não existir).
set1.discard
print(set1)
set1.discard(8)
print(set1)

# union(outro_set) - União dos conjuntos. Não funciona para editar variavel. Discarta os valores repetidos.
print(set1.union(set2))

# intersection(outro_set) - Elementos comuns entre os conjuntos.
print(set1.intersection(set2))

# difference(outro_set) - Elementos únicos do primeiro conjunto.
print(set1.difference(set2))

# clear() - Remove todos os elementos.
set2.clear()
print(set2)
