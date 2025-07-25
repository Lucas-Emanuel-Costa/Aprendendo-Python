import re

ARQUIVO_CADASTRO = 'cadastros.txt'  

cadastros = []
while True:
    cadastro = {}

    while True:
        nome = input("Digite seu nome: ").strip()
        if nome and re.search(r'[a-zA-Z]', nome):
            cadastro["nome"] = nome
            break
        else:
            print("O nome deve conter letras e não pode ser apenas números ou ficar em branco.")


    while True:
        cidade = input("Digite sua cidade: ").strip()
        if cidade and re.search(r'[a-zA-Z]', cidade):
            cadastro["cidade"] = cidade
            break
        else:
            print("A cidade deve conter letras e não pode ser apenas números ou ficar em branco.")

    while True:
        idade = input("Digite sua idade: ").strip()
        if idade.isdigit():
            cadastro["idade"] = int(idade)
            break
        else:
            print("Por favor, digite apenas números para a idade.")

    cadastros.append(cadastro)

    while True:
        continuar = input("Deseja cadastrar outra pessoa? (s/n): ").strip().lower()
        if continuar in ['s', 'n']:
            break
        else:
            print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")

    if continuar != 's':
        break

with open(ARQUIVO_CADASTRO, 'w') as arquivo:
    for c in cadastros:
        arquivo.write(f"Nome: {c['nome']}\n")
        arquivo.write(f"Cidade: {c['cidade']}\n")
        arquivo.write(f"Idade: {c['idade']}\n")
        arquivo.write("-" * 20 + "\n\n")  

with open(ARQUIVO_CADASTRO, 'r') as arquivo:
    conteudo = arquivo.read()
    print("\nConteúdo do arquivo:")
    print(conteudo)