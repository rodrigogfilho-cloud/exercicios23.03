#1.	Faça um algoritmo para ler um número inteiro e informar se este é menor, maior ou igual 10.

numero = int(input("Qual o número? "))
if numero > 10:
    print(f" {numero} é maior que 10")
if numero < 10:
    print(f" {numero} é menor que 10")
if numero == 10:
    print(f" {numero} é igual a 10")
