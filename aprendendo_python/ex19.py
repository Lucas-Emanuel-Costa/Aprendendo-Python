print('Participe do experimento, digite 9 números:')

numeros = []
for i in range(1, 10):
    num = int(input(f"Digite o {i}º número: "))
    numeros.append(num)


matriz = [
    numeros[0:3],
    numeros[3:6],
    numeros[6:9]
]


diagonal_principal = [matriz[0][0], matriz[1][1], matriz[2][2]]
diagonal_secundaria = [matriz[0][2], matriz[1][1], matriz[2][0]]


print("\nMatriz 3x3:")
for linha in matriz:
    print(linha)


print(f"\nMultiplicação da diagonal principal: {diagonal_principal[0] * diagonal_principal[1] * diagonal_principal[2]}")
print(f"Multiplicação da diagonal secundária: {diagonal_secundaria[0] * diagonal_secundaria[1] * diagonal_secundaria[2]}")
print(f"Soma da diagonal principal: {sum(diagonal_principal)}")
print(f"Soma da diagonal secundária: {sum(diagonal_secundaria)}")