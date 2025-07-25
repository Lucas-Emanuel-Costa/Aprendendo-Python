import csv
import os

# Lista global para armazenar os produtos
produtos = []


# --- Funções de Arquivo ---
def carregar_csv(nome_arquivo="produtos.csv"):
    """
    Carrega produtos de um arquivo CSV, se ele existir.
    Popula a lista global 'produtos'.
    """
    produtos.clear()  # Garante que não haverá duplicação
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado. Iniciando com lista vazia.")
        return

    try:
        with open(nome_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            if not leitor.fieldnames:
                print(f"Arquivo '{nome_arquivo}' está vazio ou sem cabeçalho. Iniciando com lista vazia.")
                return

            expected_fields = {"Nome", "Preço", "Quantidade"}
            if not expected_fields.issubset(leitor.fieldnames):
                print(f"Cabeçalho do arquivo '{nome_arquivo}' inválido. Esperado: {expected_fields}.")
                return

            for linha in leitor:
                try:
                    produto = {
                        "nome": linha["Nome"],
                        "preco": float(linha["Preço"]),
                        "quantidade": int(linha["Quantidade"])
                    }
                    produtos.append(produto)
                except (ValueError, KeyError):
                    print(f"Erro ao ler linha inválida: {linha}. Pulando...")
        print(f"Produtos carregados com sucesso do arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo '{nome_arquivo}': {e}")


def salvar_csv(nome_arquivo="produtos.csv"):
    """
    Salva todos os produtos da lista global 'produtos' em um arquivo CSV.
    """
    try:
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            campos = ["Nome", "Preço", "Quantidade"]
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            for p in produtos:
                escritor.writerow({
                    "Nome": p["nome"],
                    "Preço": p["preco"],
                    "Quantidade": p["quantidade"]
                })
        print(f"Produtos salvos com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar produtos no arquivo '{nome_arquivo}': {e}")


# --- Funções do Sistema ---
def cadastrar_produto():
    """Permite ao usuário cadastrar um novo produto."""
    print("\n=== Cadastro de Produto ===")
    nome = input("Nome do produto: ").strip()

    while True:
        try:
            preco = float(input("Preço do produto (R$): ").replace(',', '.'))
            if preco > 0:
                break
            print("O preço deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))
            if quantidade >= 0:
                break
            print("A quantidade não pode ser negativa.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
    print(f"Produto '{nome}' cadastrado com sucesso!")


def listar_produtos():
    """Exibe todos os produtos cadastrados."""
    print("\n=== Lista de Produtos ===")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for i, p in enumerate(sorted(produtos, key=lambda x: x['nome'].lower()), start=1):
        print(f"{i}. Nome: {p['nome']} | Preço: R$ {p['preco']:.2f} | Quantidade: {p['quantidade']}")


def buscar_produto():
    """Busca produtos pelo nome."""
    termo = input("\nDigite o nome (ou parte) do produto: ").strip().lower()
    encontrados = [p for p in produtos if termo in p['nome'].lower()]

    if encontrados:
        print(f"\nResultados da busca por '{termo}':")
        for i, p in enumerate(encontrados, start=1):
            print(f"{i}. Nome: {p['nome']} | Preço: R$ {p['preco']:.2f} | Quantidade: {p['quantidade']}")
    else:
        print(f"Nenhum produto encontrado com '{termo}'.")


def editar_produto():
    """Edita os dados de um produto existente."""
    listar_produtos()
    if not produtos:
        return
    try:
        indice = int(input("\nDigite o número do produto para editar: ")) - 1
        if 0 <= indice < len(produtos):
            p = produtos[indice]
            print(f"Editando '{p['nome']}'...")

            novo_nome = input("Novo nome (deixe vazio para manter): ").strip()
            if novo_nome:
                p["nome"] = novo_nome

            try:
                novo_preco = input("Novo preço (deixe vazio para manter): ").replace(',', '.')
                if novo_preco:
                    p["preco"] = float(novo_preco)
            except ValueError:
                print("Preço inválido, mantendo valor anterior.")

            try:
                nova_qtd = input("Nova quantidade (deixe vazio para manter): ")
                if nova_qtd:
                    p["quantidade"] = int(nova_qtd)
            except ValueError:
                print("Quantidade inválida, mantendo valor anterior.")

            print("Produto atualizado com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")


def excluir_produto():
    """Exclui um produto da lista."""
    listar_produtos()
    if not produtos:
        return
    try:
        indice = int(input("\nDigite o número do produto para excluir: ")) - 1
        if 0 <= indice < len(produtos):
            removido = produtos.pop(indice)
            print(f"Produto '{removido['nome']}' removido com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("Entrada inválida.")


# --- Menu Principal ---
def menu():
    carregar_csv()
    while True:
        print("\n=== Sistema de Cadastro de Produtos ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Editar produto")
        print("5 - Excluir produto")
        print("6 - Salvar produtos")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            buscar_produto()
        elif opcao == "4":
            editar_produto()
        elif opcao == "5":
            excluir_produto()
        elif opcao == "6":
            salvar_csv()
        elif opcao == "7":
            salvar_csv()
            print("Saindo do sistema. Produtos salvos!")
            break
        else:
            print("Opção inválida, tente novamente.")


# --- Execução do Programa ---
if __name__ == "__main__":
    menu()