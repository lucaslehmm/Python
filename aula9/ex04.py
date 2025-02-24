# 4. Desafio Final – Sistema de Notas
# Monte um pequeno sistema que:

# Peça o nome de 3 alunos e suas respectivas notas.
# Armazene os dados em um dicionário no formato:

# {
#   "João": 8.5,
#   "Maria": 7.0,
#   "Lucas": 9.2
# }

# Calcule e exiba a média geral da turma.
# Mostre o nome do aluno com a maior nota.

nome_aluno_1 = input("Qual o nome do primeiro aluno: ")
nome_aluno_2 = input("Qual o nome do segundo aluno: ")
nome_aluno_3 = input("Qual o nome do terceiro aluno: ")

nota_aluno_1 = int(input("Qual é a nota do primeiro aluno: "))
nota_aluno_2 = int(input("Qual é a nota do segundo aluno: "))
nota_aluno_3 = int(input("Qual é a nota do terceiro aluno: "))

alunos = {
    nome_aluno_1 : nota_aluno_1,
    nome_aluno_2 : nota_aluno_2,
    nome_aluno_3 : nota_aluno_3
}

media_turma = (nota_aluno_1 + nota_aluno_2  + nota_aluno_3) / 3

print (f'A media da turma é: {media_turma:2f}')

# Aluno com maior nota
maior_nota = max(alunos, key=alunos.get)
print(f'O aluno com a maior nota é {maior_nota}, com nota {alunos[maior_nota]}')

# Como funciona?:

# alunos.get pega o valor (nota) de cada aluno.
# max() encontra o nome do aluno com a maior nota.
