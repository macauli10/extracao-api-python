import requests
import tracemalloc
from datetime import datetime
import csv
import os

def get_bitcoin_price():
    """Obtém o preço atual do Bitcoin na Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    data = response.json()
    price = float(data['data']['amount'])
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"📊 Preço: ${price} USD | Data/Hora: {timestamp}")
    return timestamp, price

def salvar_em_csv(timestamp, price, arquivo_csv='data/bitcoin_prices.csv'):
    """Salva o registro de preço com data/hora em um CSV."""
    existe = os.path.isfile(arquivo_csv)
    with open(arquivo_csv, mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        if not existe:
            writer.writerow(['timestamp', 'price_usd'])  # Cabeçalho
        writer.writerow([timestamp, price])

if __name__ == "__main__":
    tracemalloc.start()
    snapshot_inicio = tracemalloc.take_snapshot()

    timestamp, price = get_bitcoin_price()
    salvar_em_csv(timestamp, price)

    snapshot_fim = tracemalloc.take_snapshot()
    memoria_pico = tracemalloc.get_traced_memory()[1] / (1024 * 1024)
    print(f"🔍 Pico de memória: {memoria_pico:.2f} MB")

    tracemalloc.stop()
