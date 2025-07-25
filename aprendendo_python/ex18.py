n = int(input("Digite um número: "))

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if primo(n):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")