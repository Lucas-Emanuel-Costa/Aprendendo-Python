import re
import unicodedata

def remove_acentos_pontuacao(frase):
    frase = ''.join(c for c in unicodedata.normalize('NFD', frase)
                  if unicodedata.category(c) != 'Mn')  
    frase = re.sub(r'[^\w\s]', '', frase)  # Remove pontuação
    frase = re.sub(r'\s+', '', frase)  # Remove espaços
    return frase

def eh_palindromo(frase):
    frase_processada = remove_acentos_pontuacao(frase).lower()
    frase_invertida = frase_processada[::-1]
    return frase_processada == frase_invertida

frase = input("Digite uma frase para verificar se é um palíndromo: ")
if eh_palindromo(frase):
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")
