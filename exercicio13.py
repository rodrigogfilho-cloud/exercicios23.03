# 13.	Leia a idade e o tempo de serviço, em anos, de um trabalhador e escreva se ele pode ou não se aposentar.  As condições para aposentadoria são:

#Ter pelo menos 65 anos,
#Ou ter trabalhado pelo menos 30 anos,
#Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Quantos anos você tem?"))
trabalho = int(input("Quantos anos de trabalho você tem? "))

if idade >= 65 or trabalho >= 30 or idade >= 60 and trabalho >= 25:
    print("Pode se aposentar!")
else:
    print("Ainda não pode se aposentar")