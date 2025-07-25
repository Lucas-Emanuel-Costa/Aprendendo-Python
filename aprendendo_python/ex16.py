
cadastro = {
    "nome": input("Digite seu nome: "),
    "cidade": input("Digite sua cidade: "),
    "idade": int(input("Digite sua idade: "))
}
print("Cadastro realizado:")
print(f"Nome: {cadastro['nome']}")
print(f"Cidade: {cadastro['cidade']}")
print(f"Idade: {cadastro['idade']}")