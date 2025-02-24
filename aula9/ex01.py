# 1. Listas – Manipulação de Dados
# Crie uma lista chamada frutas contendo: ["maçã", "banana", "laranja", "uva"] e realize as seguintes operações:

# a) Adicione "melancia" à lista.
# b) Remova "banana" da lista.
# c) Ordene a lista em ordem alfabética.
# d) Exiba o número total de itens. ? 

frutas = ["Maça", "Banana", "Laranja", "Uva"]

frutas.append("Melancia")
frutas.remove("Banana")
frutas.sort()

print(frutas, frutas.count("Maça"))