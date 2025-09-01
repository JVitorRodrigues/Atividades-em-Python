#Classificação de Nota
#Leia três notas (0 a 10), cálculo a média e exiba:
#  Aprovado (≥ 7)
#  Recuperação (≥ 5 e < 7)
#  Reprovado (< 5)
# Obs: Adicione uma verificação para impedir notas inválidas (negativas ou >10)

def ler_nota(numero):
    while True:
        try:
            nota = float(input(f"Digite a nota {numero} (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print(" Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print(" Entrada inválida. Digite um número.")

# Leitura das três notas com validação
nota_1 = ler_nota(1)
nota_2 = ler_nota(2)
nota_3 = ler_nota(3)

# Cálculo da média
media = (nota_1 + nota_2 + nota_3) / 3

# Exibição do resultado
print(f"\nMédia: {media:.2f}")

if media >= 7:
    print(" Resultado: Aprovado")
elif media >= 5:
    print(" Resultado: Recuperação")
else:
    print(" Resultado: Reprovado")



