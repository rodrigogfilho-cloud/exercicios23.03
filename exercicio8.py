#8.	Faça um programa que leia a idade de uma pessoa e verifique se ela é:

#Criança:  Idade de 1 a 13 anos;
#Adolescente:  Idade maior que 13 anos e menor ou igual a 20 anos;
#Adulto:  Idade maior que 20 e menor ou igual a 50 anos;
#Idosa:  idade maior que 50 anos.  

idade = int(input("Qual a sua idade ? "))

if idade <= 13 : 
    print("Você é uma criança")
elif idade <= 20 and idade > 13:
    print("Você é um adolescente")
elif idade <= 50 and idade > 20:
    print("Você é um adulto")
elif idade > 50:
    print("Você já é uma pessoa idosa")