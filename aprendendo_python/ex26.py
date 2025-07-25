import requests
from datetime import datetime
import time
import csv

def get_dolar_quotation(retries=3, delay=5):
   
    api_url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    for attempt in range(retries):
        try:
            response = requests.get(api_url)
            response.raise_for_status()

            data = response.json()

            if "USDBRL" in data:
                dolar_data = data["USDBRL"]
                required_keys = ["bid", "high", "low", "timestamp"]

                if all(key in dolar_data for key in required_keys):
                    return {
                        "bid": float(dolar_data["bid"]),
                        "high": float(dolar_data["high"]),
                        "low": float(dolar_data["low"]),
                        "timestamp": int(dolar_data["timestamp"])
                    }
                else:
                    print("❌ Dados incompletos na resposta da API.")
                    return None
            else:
                print("❌ Dados do dólar não encontrados na resposta.")
                return None

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                print(f"⚠️ Tentativa {attempt + 1}/{retries}: Erro 429 (Muitas requisições). Aguardando {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                print(f"❌ Erro HTTP: {e}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro de conexão: {e}")
            return None
        except ValueError:
            print("❌ Erro ao converter os valores da API.")
            return None
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return None

    print("❌ Todas as tentativas falharam.")
    return None

def salvar_txt(data_string):
    with open("cotacao_dolar.txt", "a", encoding="utf-8") as f:
        f.write(data_string + "\n")

def salvar_csv(data_formatada, bid, high, low):
    with open("cotacao_dolar.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([data_formatada, bid, high, low])

def main():
    cotacao = get_dolar_quotation()

    if cotacao:
        bid = cotacao["bid"]
        high = cotacao["high"]
        low = cotacao["low"]
        timestamp = cotacao["timestamp"]

        data_formatada = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print("\n📊 COTAÇÃO DO DÓLAR")
        print(f"Valor atual: R$ {bid:.2f}")
        print(f"Alta do dia: R$ {high:.2f}")
        print(f"Baixa do dia: R$ {low:.2f}")
        print(f"Data/Hora: {data_formatada}\n")

        texto = f"Cotação: R$ {bid:.2f} | Alta: R$ {high:.2f} | Baixa: R$ {low:.2f} | Data: {data_formatada}"
        salvar_txt(texto)
        salvar_csv(data_formatada, bid, high, low)

        print("✅ Dados salvos em: 'cotacao_dolar.txt' e 'cotacao_dolar.csv'.")
    else:
        print("⚠️ Não foi possível obter a cotação do dólar.")

if __name__ == "__main__":
    main()
