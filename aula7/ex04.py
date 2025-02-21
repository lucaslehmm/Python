# Tabuada:
# Peça ao usuário um número e exiba a tabuada desse número (de 1 a 10) usando for.

numero_usuario = int(input('Digite um numero: '))
print(f'Tabuada do {numero_usuario}')

for numero in range(11):
    if numero == 0:
        continue
    print(f"{numero_usuario} x {numero} = {numero_usuario * numero}")

(input('Digite um numero: '))