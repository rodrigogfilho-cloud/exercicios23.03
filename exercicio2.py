#2.	Crie um algoritmo para ler dois números inteiros e informar se estes números são iguais ou diferentes.  

numero1 = int(input("Me fale o primeiro número :"))
numero2 = int(input("Me fale o segundo número :"))

if numero1 == numero2:
    print (f"{numero1}, {numero2} são iguais")
else: 
    print(f"{numero1}, {numero2} são diferentes")