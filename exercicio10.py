# 10.	Determine se um determinado ano lido é bissexto.  Sendo que um ano é bissexto se for divisível por 400 ou se for divisível por 4 e não for divisível por 100.

ano = int(input("Qual ano você deseja saber se é bissexto ou não? ")) 

if ano % 4 == 0:
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")

