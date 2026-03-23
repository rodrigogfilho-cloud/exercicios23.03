# 7.	Tendo como dados de entrada a altura e o sexo de uma pessoa (M = masculino e F = feminino), construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7 * h) - 58; Para mulheres: (62.1 * h) - 44.7

altura = float(input("Qual a sua altura em metros: "))
sexo = input("Qual seu genêro: ").upper()

if sexo == "MASCULINO" or sexo == "M":
    mediaM = round(72.7 * altura - 58)
    print(f"Seu peso ideal é {mediaM} KG")
if sexo == "FEMININO" or sexo == "F":
    mediaF = round(62.1 * altura - 44.7)
    print(f"Seu peso ideal é {mediaF} KG")