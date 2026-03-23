
# 5.	Modifique o programa do exercício 4, adicione uma condicional para impedir que o segundo número seja zero. Neste caso, imprima: “impossível dividir N por zero!”, onde N é o primeiro número digitado.

numeroA = int(input("Digite o número A : "))
numeroB = int(input("Digite o número B : "))

if numeroB == 0:
    print(f"{numeroA} não pode ser divido por {numeroB}")
    

elif numeroA % numeroB == 0:
        print(f"{numeroA} é divísivel por {numeroB}")
else:
    print(f"{numeroA} não é divísivel por {numeroB}")
 