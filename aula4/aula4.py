# Condicionais

# A estrutura condicional avalia se uma expressão é verdadeira ou falsa.

# if = se...
# else = se não...
# elif = se não, se...

# Estrutura  basica do if
idade = 18

if idade >= 18:                # Condição
    print('Maior de idade')    # Verdadeiro
else:
    print ('Menor de idade')   # Falso

# Estrutura com elif

nota = 7

if nota >= 9:
    print('Aprovado com prestigio')
elif nota >= 6:
    print ("Aprovado")
else:
    print("Reprovado")

## Operadores de Comparação

#Operador	    #Significado	    #Exemplo (a = 5, b = 3)
#  ==	         Igual a	         a == b - False
#  !=	         Diferente de	     a != b - True
#  >	         Maior que	         a > b - True
#  <	         Menor que	         a < b - False
#  >=	         Maior ou igual	     a >= 5 - True
#  <=	         Menor ou igual	     a <= 4 - False


## Operadores Lógicos

# Operador	     #Significado	               #Exemplo
# and	         E (ambas verdadeiras)	       5 > 2 and 3 < 4 - True
# or	         Ou (uma ou outra)	           5 < 2 or 3 < 4 - True
# not	         Não (inverte valor)	       not 5 > 2 - False

#Exemplo

idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
else:
    print('Não pode dirigir.')