## Parte 1 - Listas
# Lista (list) - As listas são coleções ordenadas e mutáveis que permitem armazenar múltiplos itens em uma única variável.

alunos = ['Lucas','André','João', 'Eduardo', 'Maria']

# Metodos Uteis do tipo list
#ps. metodos sao usados com notacao de ponto - lista.metodo(parametro)

# append(item) - Insere um item ao final da lista
alunos.append('Helena')
print(alunos)

# insert(pos, item) - insere um item em uma posição especifica
alunos.insert(0, 'Cleber')
print(alunos)

#remove(item) - Remove o primeiro item com o valor especificado. Não da pra usar indice.
alunos.remove('João')
print(alunos)

# pop([pos]) - Remove e retorna o item em uma posição (ou o último, se não especificar).
aluno_popado = alunos.pop()
print(alunos, aluno_popado)

# sort() - Ordena a lista em ordem crescente.
alunos.sort()
print(alunos)

# reverse() - Inverte a ordem da lista.
alunos.reverse()
print(alunos)

# index(item) - Retorna a posição do primeiro item encontrado.
print(alunos.index('Lucas'))

# count(item) - Conta quantas vezes o item aparece na lista.
print(alunos.count('Lucas'))