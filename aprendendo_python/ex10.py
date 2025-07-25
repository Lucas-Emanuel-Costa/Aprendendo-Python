compras = input("Digite a lista de compras separada por vírgula: ")
compras = compras.split(',')
print("Lista de compras:")
for item in compras:
    print(item.strip())  