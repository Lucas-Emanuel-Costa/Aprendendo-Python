cadastros = []

while True:
    cadastro = {
        "nome": input("Digite seu nome: "),
        "cidade": input("Digite sua cidade: "),
        "idade": int(input("Digite sua idade: "))
    }
    cadastros.append(cadastro)

    while True:
        continuar = input("Deseja cadastrar outra pessoa? (s/n): ").strip().lower()
        if continuar in ['s', 'n']:
            break
        else:
            print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")

    if continuar != 's':
        break

print("\nCadastros realizados:")
for idx, c in enumerate(cadastros, start=1):
    print(f"{idx}. Nome: {c['nome']}, Cidade: {c['cidade']}, Idade: {c['idade']}")
