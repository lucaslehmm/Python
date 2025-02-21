# Crie um programa que:

# Peça a idade do usuário.
# Se a idade for menor que 12 - imprima: "Criança"
# Se a idade estiver entre 12 e 17 - imprima: "Adolescente"
# Se a idade for entre 18 e 59 - imprima: "Adulto"
# Se a idade for 60 ou mais - imprima: "Idoso"

idade = int(input("Digite sua idade: "))

if idade >= 60:
    print("Idoso")
elif idade >= 18:
    print("Adulto")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")
