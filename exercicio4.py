# 4.	Faça um algoritmo para ler dois números inteiros A e B e informar se A é divisível por B.

numeroA = int(input("Digite o número A : "))
numeroB = int(input("Digite o número B : "))

if numeroA % numeroB == 0:
    print(f"{numeroA} é divísivel por {numeroB}")
else:
    print(f"{numeroA} não é divísivel por {numeroB}")