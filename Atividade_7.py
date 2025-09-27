"""Analisando uma pesquisa de opiniões
Uma empresa fez uma pesquisa com N clientes e perguntou:

● Idade do cliente
● Nota de satisfação (de 1 a 5)
O programa deve:
● Ler os dados de cada cliente.
● Calcular a média de idade dos clientes satisfeitos (nota ≥ 4).
● Calcular a porcentagem de clientes insatisfeitos (nota ≤ 2).
● Mostrar a nota média geral"""

numero_clientes = int(input("Digiti o número de cliente: "))

total_idade_satisfeitos = 0 
total_clientes_satisfeitos = 0
total_clientes_insatisfeitos = 0
total_satisfacao = 0
total_idade = 0 

for i in  range (numero_clientes):
    idade = int(input(f"Digite a idade do cliente {i+1}: "))
    satisfacao = int(input(f"Digite a nota de satisfação do cliente {1+1} (1 a 5): "))

    total_idade += idade
    total_satisfacao += satisfacao

    if satisfacao  >4:
        total_clientes_satisfeitos += 1
        total_idade_satisfeitos += idade
    else:
        satisfacao <= 2 
        total_clientes_insatisfeitos += 1
porcentagem_insatisfeitos = (total_clientes_insatisfeitos / numero_clientes) * 100  if numero_clientes > 0 else 0 

if numero_clientes >0:
    media_satisfacao = total_clientes_satisfeitos / numero_clientes
else:
     media_satisfacao = 0 

print(f"média dos clientes satisfeitos: {media_satisfacao: .2f}")
print(f"Porcentagem de clientes insatisfeito: {porcentagem_insatisfeitos: .2f}%")
print(f"Média de satisfação: {media_satisfacao: .2}%")









