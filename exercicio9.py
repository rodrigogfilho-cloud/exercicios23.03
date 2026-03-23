#9.	Fazer um programa para calcular o salário líquido de um funcionário com base na seguinte fórmula:

#salário líquido = salário bruto + proventos - desconto

#Devem ser respeitadas as seguintes condições para cálculo do desconto:
#Salário Bruto <= R$5000, desconto de 5%
#Salário Bruto > R$5000, desconto de 10%

saláriobruto = float(input("Qual o seu salário bruto? "))

if saláriobruto <= 5000:
    sl1 = round(saláriobruto * 0.05, 2)
    pt1 = round(saláriobruto - sl1, 2)
    print (f"Seu salário líquido é {pt1} reais")
if saláriobruto > 5000:
    sl2 = round(saláriobruto * 0.10, 2)
    pt2 = round(saláriobruto - sl2, 2 )
    print (f"Seu salário líquido é {pt2} reais")