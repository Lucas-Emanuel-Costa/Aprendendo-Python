compras = str(input("Digite o nome do produto separados por vírgula: "))
lista_compras = compras.split(",")
for idx, item in enumerate(lista_compras, start=1):
    print(f"Item {idx}: {item.strip()}")