#6.	Faça um algoritmo para ler dois números inteiros diferentes e escrever o maior.

nmr1 = int(input("Digite um número: "))
nmr2 = int(input("Digite um número: "))

if nmr1 > nmr2:
    print(f"{nmr1} é maior que {nmr2}")
elif nmr2 > nmr1: 
    print(f"{nmr2} é maior que {nmr1}")
elif nmr1 == nmr2:
    print(f"Ambos são iguais")