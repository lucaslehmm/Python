## Parte 4 - Dicionarios
# Dicionários (dict) - Dicionários armazenam dados em pares chave:valor, permitindo acessar rapidamente valores usando suas chaves.

pessoa1 = {
    "nome": "Lucas",
    "sobrenome" : "Lehm",
    "idade": 22,
    "cor_favorita": "Roxo"
}

print(pessoa1)

# Notação de colchete
print(pessoa1["nome"])

# Metodos Uteis
# get(chave, valor_padrao) - Retorna o valor da chave ou um valor padrão.
print(pessoa1.get("nome")) # Valor da chave
print(pessoa1.get("carro", "não informado")) # Caso a chave não exista, voce pode informar um valor padrao a ela

# keys() - Retorna todas as chaves.
print(pessoa1.keys())

# values() - Retorna todos os valores.
print(pessoa1.values())

# items() - Retorna pares (chave, valor).
print(pessoa1.items())

# update({"chave":valor}) - Atualiza/Edita o dicionario

pessoa1.update({'nome' : 'Maria Helena', "idade": 12})  # Posso alterar mais de um de uma vez
print(pessoa1)

pessoa1.update({'filme_favorito' : "Interstellar"}) # Caso não exista, ele adiciona ao final das chaves

novos_dados = {
    "email" : "mariahelena433@gmail.com",
    "sobrenome" : "Leite Lehm"
}

pessoa1.update(novos_dados) # Pode atualizar com outro dict, as chaves iguais serão alteradas e as novas serão adicionadas.

print(pessoa1)

pessoa1.update(idade = 10, filme_favorito = "Bela e a Fera") # da pra alterar como se fosse parametros de função também

print(pessoa1)


# pop(chave) - Remove a chave e retorna seu valor.
print(pessoa1.pop("cor_favorita"), pessoa1)
print(pessoa1)

# clear() - Remove todos os itens.
print(pessoa1.clear())