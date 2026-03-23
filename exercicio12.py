# 12.	Escreva um programa que leia o código de um aluno e suas três notas.  Calcule a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas restantes, 3.  Mostre o código do aluno, suas três notas, a média calculada e uma mensagem “APROVADO” se a média for maior ou igual a 5 e “REPROVADO" se a média for menor que 5.

nt1 = int(input("Qual é a 1° nota :"))
nt2 = int(input("Qual é a 2° nota :"))
nt3 = int(input("Qual é a 3° nota :"))

codigo = int(input("Qual o código do aluno: "))

media = round((nt1 + nt2 + nt3) / 3,)

if codigo == 12345678 :
    print(f"""
1° nota: {nt1}
2° nota: {nt2}
3° nota: {nt3}
""")

    
    if media >= 5:
        print(f"Sua nota foi {media}")
        print("APROVADO")
    else:
        print(f"Sua nota foi {media}")
        print("REPROVADO")