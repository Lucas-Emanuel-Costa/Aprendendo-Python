n1 = float(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

operacao = input('Escolha a operação (soma, subtracao, multiplicacao, divisao): ').strip().lower()

if operacao == 'soma':
    resultado = n1 + n2
elif operacao == 'subtracao':
    resultado = n1 - n2
elif operacao == 'multiplicacao':
    resultado = n1 * n2
elif operacao == 'divisao':
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = 'Divisão por zero não é permitida.'
else:
    resultado = 'Operação inválida.'

print(f"Resultado da {operacao}: {resultado}")