# Soma acumulada:
# Peça ao usuário para digitar números até que ele digite 0. Ao final, exiba a soma de todos os números inseridos (exceto o zero).

numero = ''
soma_dos_numeros = 0

print("Vamos somar numeros!")

while numero != 0:
    print('Digite "0 para parar a soma."')
    numero = int(input('Digite um numero: '))
    soma_dos_numeros += numero


print(f"A soma dos números é: {soma_dos_numeros}")

input('Digite um numero: ')