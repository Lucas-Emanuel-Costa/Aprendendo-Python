from math import sqrt, pow, factorial

numero = int(input("Digite um número inteiro não negativo: "))

if numero < 0:
    print("Erro: número negativo não tem fatorial.")
else:
    print(f"Raiz quadrada: {sqrt(numero)}")
    print(f"Potência ao quadrado: {pow(numero, 2)}")
    print(f"Fatorial: {factorial(numero)}")