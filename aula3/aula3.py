# Indices, fatiamento, in - not in

# Em python existem indices positos e negativos

# P  Y  T  H  O  N
# 0  1  2  3  4  5 (positivos)
#-1 -2 -3 -4 -5 -6 (negativos)

nome = 'Lucas'

print(nome[1])
print(nome[-1])

## Fatiamento

# Sintaxe
# texto[início:fim:passo]

#Parâmetro	   #Descrição
#início	       Índice onde o fatiamento começa (inclusivo)
#fim	       Índice onde o fatiamento termina (exclusivo)
#passo	       (opcional) De quantos em quantos índices avançar

texto = "Programação"

print(texto[0:4])

# Omitindo iniico ou fim

print(texto[:7])
print(texto[5:])

# Indices negativos e Inversão

print(texto[-4:])
print(texto[::-1])

## in e not in

# In verifica se um valor existe em uma sequencia

aluno = "Eduardo"
if "a" in aluno:
    print('A letra "a" esta no nome do aluno')

# Not in verifica se um valor NÃO existe em uma sequencia

frutas = ["maça", "banana", "laranja"]
if "uva" not in frutas:
    print("Uva não está na lista.")