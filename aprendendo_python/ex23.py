import re

ARQUIVO_CADASTRO = 'cadastros.txt'

def obter_nome():
    while True:
        nome = input("Digite seu nome: ").strip()
        if nome and re.search(r'^[a-zA-Z\s]+$', nome):
            return nome
        else:
            print("O nome deve conter pelo menos uma letra e não pode ser apenas espaços ou pontuações.")

def obter_cidade():
    while True:
        cidade = input("Digite sua cidade: ").strip()
        if cidade and re.search(r'^[a-zA-Z\s]+$', cidade):
            return cidade
        else:
            print("A cidade deve conter pelo menos uma letra e não pode ser apenas espaços ou pontuações.")

def obter_idade():
    while True:
        idade = input("Digite sua idade: ").strip()
        try:
            idade_float = float(idade)
            if idade_float > 0:
                return idade_float
            else:
                print("Por favor, digite uma idade maior que 0.")
        except ValueError:
            print("Por favor, digite apenas números para a idade (maior que 0).")

def deseja_continuar():
    while True:
        continuar = input("Deseja cadastrar outra pessoa? (s/n): ").strip().lower()
        if continuar in ['s', 'n']:
            return continuar == 's'
        else:
            print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")

def salvar_cadastros(cadastros, arquivo_nome):
    with open(arquivo_nome, 'w') as arquivo:
        for c in cadastros:
            arquivo.write(f"Nome: {c['nome']}\n")
            arquivo.write(f"Cidade: {c['cidade']}\n")
            arquivo.write(f"Idade: {c['idade']}\n")
            arquivo.write("-" * 20 + "\n\n")

def exibir_arquivo(arquivo_nome):
    with open(arquivo_nome, 'r') as arquivo:
        conteudo = arquivo.read()
        print("\nConteúdo do arquivo:")
        print(conteudo)

def main():
    cadastros = []
    while True:
        cadastro = {
            "nome": obter_nome(),
            "cidade": obter_cidade(),
            "idade": obter_idade()
        }
        cadastros.append(cadastro)
        if not deseja_continuar():
            break

    salvar_cadastros(cadastros, ARQUIVO_CADASTRO)
    exibir_arquivo(ARQUIVO_CADASTRO)

if __name__ == "__main__":
    main()