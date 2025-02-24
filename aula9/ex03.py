# 3. Dicionários – Dados Estruturados
# Crie um dicionário chamado contato com os dados:

# 
#  "nome": "Ana",
#  "telefone": "1234-5678",
#  "email": "ana@email.com"
# 

# Realize as seguintes ações:

# a) Atualize o telefone para "9876-5432".
# b) Adicione o campo "endereço" com o valor "Rua das Flores, 123".
# c) Remova o campo "email".
# d) Liste todas as chaves e valores do dicionário.

contato = {
    'nome': 'Ana',
    'telefone': '1234-5678',
    'email': 'ana@email.com'
}

contato.update(telefone = '9876-5432')
contato.update({"endereco": 'Rua das Flores, 123'})
contato.pop("email")

print(contato.items())