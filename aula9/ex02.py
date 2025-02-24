# 2. Tuplas – Dados Imutáveis
# Crie uma tupla chamada dias_semana com os dias: ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo") e:

# a) Mostre o dia correspondente ao índice 3.
# b) Verifique se "domingo" está na tupla.
# c) Conte quantas vezes a palavra "sábado" aparece na tupla.

dias_da_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")

print(dias_da_semana[3])
print(dias_da_semana.index("domingo"))
print(dias_da_semana.count("sabado"))