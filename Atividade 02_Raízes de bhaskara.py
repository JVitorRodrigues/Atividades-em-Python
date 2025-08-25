#Raízes de Bhaskara
# Leia os coeficientes a, b, c de uma equação quadrática. Calcule e mostre as raízes reais
#(caso existam).
#Discriminante: Use a fórmula Δ = b² - 4ac.
#Fórmula de Bhaskara: Utilize a fórmula x = (-b ± √Δ) / 2a para encontrar as raízes.

import math

print ("Cálculo das raizes de uma equação quadrática (ax² + bx + c = 0)")

    # Pede os valores de A, B e C, convertendo para float

try:
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")
    exit()

    # Verifica se a equação é quadrática

if a == 0:
    print("O valor de A não pode ser zero para uma equação quadrática.")
    exit()

    # Calcula o delta (discriminante)

delta = b**2 - 4*a*c

    # Imprime o resultado baseado no valor do delta

if delta < 0:
    print("Não existem raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print(f"Existe uma raiz real: x = {x:.2f}")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"As raízes reais são: x1 = {x1:.2f} e x2 = {x2:.2f}")