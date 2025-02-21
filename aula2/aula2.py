# Variaveis
# Espaços na memoria para guardar informações que vao se repetir ou serão manipuladas durante o código

nome = "Lucas"
idade = 22
altura = 1.73

# Regras para variaveis :
   # O nome deve começar com uma letra ou underline (_).
   # Não pode começar com número.
   # Sem espaços no nome
   # Palavras reservadas da linguagem (como if, for, class) não podem ser usadas como nome de variáveis.

# Boas Praticas :
   # Use snake_case para variáveis : "minha_variavel".
   # Use nomes claros e descritivos : "preco_produto" em vez de p.

# Constantes :
   # Não existem em pyhton, mas, os devs criaram uma regra na comunidade que diz que variaveis COM LETRAS MAIUSCULAS não podem ser editadas.

#Tipos de dados

tipo_int = 10                  # Números inteiros
tipo_float = 3.14              # Números decimais
tipo_str = "Lucas"             # Textos (Strings)
tipo_bool = True               # Valores logicos (Verdeiro ou Falso)
tipo_list = [1, 2, 3]          # Coleção de valores (lista)
tipo_dict = {"nome": "Lucas"}  # Pares chave-valor (dicionario)

# Conversão de tipos

#int()	           Inteiro	
#float()	           Ponto flutuante	
#str()	           String	
#bool()	           Booleano	
#list()	           Lista	
#tuple()	           Tupla	

print(int('10'))
print(list('abc'))

#Regras para booleano

# 0 ou 0.0               = False
# "" (vazio)             = False
# None                   = False
# qualquer outro valor   = True

print(bool(""))
print(bool("Lucas"))
print(bool(0))
print(bool(99))



# Operadores Aritimeticos 

a = 10
b = 5

# Operações Matemáticas
soma = a + b                   # Adição
subtracao = a - b              # Subtração
multiplicacao = a * b          # Multiplicação
divisao = a / b                # Divisão (resultado float)
modulo = a % b                 # Resto da divisão
potencia = a ** 2              # Potenciação

print("Soma:", soma)

## Concatenação e Repetição

# Você pode concatenar (juntar) strings com +

texto_1 = "Olá"
texto_2 = "Mundo"

print(texto_1 + " " + texto_2)

# Você pode repetir strings com *

print(texto_2 * 4)

## Interpolação de strings

# Interpolação de string é o processo de inserir variáveis ou valores dentro de uma string. Na pratica o melhor jeito é usando "f-strings"

nome = "Lucas"
idade = 22

print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")

# formatação em f-strings


# Código	      #Significado
# .2f	         2 casas decimais
# :,	         Separador de milhar

preco = 49.99
print(f"Preço: R${preco:.2f}")

numero = 1234
print(f"Número formatado: {numero:,}")