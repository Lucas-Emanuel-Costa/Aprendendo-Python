from datetime import datetime

ARQUIVO_HISTORICO = "historico_calculos.txt"


def obter_numero(prompt):
   
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")


def deseja_continuar():
   
    while True:
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar in ['s', 'n']:
            return continuar == 's'
        else:
            print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")


def salvar_historico(historico, nome_arquivo):
   
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        session_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        arquivo.write(f"\n--- Sessão de Cálculos Iniciada em: {session_time} ---\n")
        for calculo in historico:
            n1 = calculo['n1']
            n2 = calculo['n2']
            res = calculo['resultados']
            timestamp = calculo['timestamp']

            arquivo.write(f"[{timestamp}] Cálculo com os números {n1} e {n2}:\n")
            arquivo.write(f"  - Soma: {res['soma']:.2f}\n")
            arquivo.write(f"  - Subtração: {res['subtracao']:.2f}\n")
            arquivo.write(f"  - Multiplicação: {res['multiplicacao']:.2f}\n")

            div_res = res['divisao']
            if isinstance(div_res, (int, float)):
                arquivo.write(f"  - Divisão: {div_res:.2f}\n\n")
            else:
                arquivo.write(f"  - Divisão: {div_res}\n\n")

def main():
    historico = []
    while True:
        n1 = obter_numero("Digite o primeiro número: ")
        n2 = obter_numero("Digite o segundo número: ")

        soma = n1 + n2
        subtracao = n1 - n2
        multiplicacao = n1 * n2

        if n2 != 0:
            divisao = n1 / n2
        else:
            divisao = "Erro: Divisão por zero não é permitida."

        timestamp = datetime.now().strftime("%H:%M:%S")
        historico.append({
            "n1": n1,
            "n2": n2,
            "timestamp": timestamp,
            "resultados": {
                "soma": soma, "subtracao": subtracao,
                "multiplicacao": multiplicacao, "divisao": divisao
            }
        })

        print("\n--- Resultados ---")
        print(f"Soma: {n1} + {n2} = {soma:.2f}")
        print(f"Subtração: {n1} - {n2} = {subtracao:.2f}")
        print(f"Multiplicação: {n1} * {n2} = {multiplicacao:.2f}")

        if isinstance(divisao, (int, float)):
            print(f"Divisão: {n1} / {n2} = {divisao:.2f}")
        else:
            print(f"Divisão: {n1} / {n2} = {divisao}")
        print("------------------\n")

        if not deseja_continuar():
            if historico:
                salvar_historico(historico, ARQUIVO_HISTORICO)
                print(f"\nObrigado por usar a calculadora! Histórico da sessão salvo em '{ARQUIVO_HISTORICO}'.")

                with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as arq:
                    print("\n--- Conteúdo Completo do Histórico ---")
                    print(arq.read())
                    print("------------------------------------")
            else:
                print("\nObrigado por usar a calculadora! Nenhuma operação foi realizada nesta sessão.")
            break

if __name__ == "__main__":
    main()
