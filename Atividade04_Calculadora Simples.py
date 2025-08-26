#Calculadora Simples
#Leia dois números, uma operação (+, -, *, /) e exiba o resultado.

try:
    
    numero_01 = float (input ("Digite o primero número para uma operação:"))
    numero_02 = float (input ("Digite o segundo número para a operação:"))



    print ("Digite o número correspondente à operação que deseja realizar:")

    print ("----------------------------------------------------------------")

    print ("Digite 1 para Adição (+)")
    print ("Digite 2 para Subtração (-)")
    print ("Digite 3 para Multiplicação (*)")
    print ("Digite 4 para Divisão (/)")

    print ("----------------------------------------------------------------")

    operacao = int (input ("Operação: "))

    if operacao == 1:
        print ("Resutado: ",numero_01 + numero_02)
    elif operacao == 2:
        print ("Resutado: ",numero_01 - numero_02)
    elif operacao == 3:
        print ("Resutado: ", numero_01 * numero_02)
    elif operacao == 4:
    
        if numero_02 != 0:
            print ("Resuttado: ",numero_01 / numero_02)
        else:
            print ("ERRO: divisão por 0 não é permitida!")
    else:
        print ("Operção invalida")

except:
    print ("ERRO: Digite apenas números")


