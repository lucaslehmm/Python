##  Estruturas de Repetição

# While (Repetição condicional)
# O while executa um bloco de código enquanto a condição for verdadeira. Ele checa a condição antes de cada repetição.

contador = 0 # Inicio da variavel de "controle"

while contador < 5: # Enquanto contador for menor do que 5, execute a condição.
    print(f"Contando: {contador}") # Exibe o valor da contagem
    contador += 1 # Incrementa ao contador

print(f"Fim da contagem em: {contador}")

# For (Repetição por sequência)
# O for é usado para iterar coleções como listas, strings ou um intervalo de números.

frutas = ["Melão", "Abacaxi", "Morango"]

for fruta in frutas: # vai pegar cada item da lista de frutas e colocar na variavel "fruta"
    print(f"eu gosto de {fruta}")

# Range() = usado para definir um "limite" para o for. O range não inclui o ultimo número.
for numero in range(1,6):
    print(f'Numeros: {numero}')

# Break - Para o loop imediatamente
for numero in range(10):
    if numero == 5:
        print('Parando no número: 5')
        break
    print(f"Número: {numero}")

# Continue - Pula a próxima repetição
for numero in range(7):
    if numero == 2:
        continue
    print(f'Número: {numero}')


## Laços aninhados

for i in range(3):  # Loop externo
    for j in range(2):  # Loop interno
        print(f"i = {i}, j = {j}")