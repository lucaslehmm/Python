# Descrição:
# Crie um programa que:

# Peça ao usuário:

# Seu nome
# Sua idade
# Sua cidade
# Classifique a idade em:

# Criança → 0 a 11 anos
# Adolescente → 12 a 17 anos
# Adulto → 18 a 59 anos
# Idoso → 60+ anos
# Mostre uma mensagem formatada usando F-Strings:
# Olá, [Nome]! Você tem [idade] anos, mora em [cidade] e é classificado como [classificação de idade].
# Imprima o nome do usuário ao contrário.
# Diga quantas letras o nome possui.

# Exemplo de execução:

# Digite seu nome: Lucas  
# Digite sua idade: 22  
# Digite sua cidade: São Paulo  

# Olá, Lucas! Você tem 22 anos, mora em São Paulo e é classificado como Adulto.  
# Seu nome ao contrário é sacuL e possui 5 letras.  

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input('Em qual cidade você mora? : ')

if idade >= 60:
    print(f"Olá, {nome} Você tem {idade} anos, mora em {cidade} e é classificado como Idoso.")
    print(f"Seu nome ao contrário é {nome[::-1]} e possui {len(nome)} letras.")
elif idade >= 18:
    print(f"Olá, {nome} Você tem {idade} anos, mora em {cidade} e é classificado como Adulto.")
    print(f"Seu nome ao contrário é {nome[::-1]} e possui {len(nome)} letras.")
elif idade >= 12:
    print(f"Olá, {nome} Você tem {idade} anos, mora em {cidade} e é classificado como Adolescente.")
    print(f"Seu nome ao contrário é {nome[::-1]} e possui {len(nome)} letras.")
else:
    print(f"Olá, {nome} Você tem {idade} anos, mora em {cidade} e é classificado como Criança.")
    print(f"Seu nome ao contrário é {nome[::-1]} e possui {len(nome)} letras.")