voto = int(input('Informe a sua idade: '))

if voto >= 18 and voto < 70:
    print('Seu voto é obrigatório.')
elif (voto >= 16 and voto < 18) or (voto >= 70):
    print('Você pode votar, mas não é obrigatório.')
else:
    print('Você não pode votar.')
