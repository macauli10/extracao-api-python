import requests
import tracemalloc

def get_bitcoin_price():
    """Obtém o preço atual do Bitcoin na Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)  
    data = response.json()
    price = data['data']['amount']
    print(f"Preço atual do Bitcoin: ${price} USD")
    return float(price)

if __name__ == "__main__":
    
    tracemalloc.start()

   
    snapshot_inicio = tracemalloc.take_snapshot()

    
    get_bitcoin_price()

    
    snapshot_fim = tracemalloc.take_snapshot()

    
    memoria_pico = tracemalloc.get_traced_memory()[1] / (1024 * 1024)  

   
    print(f"🔍 Pico de memória durante a execução: {memoria_pico:.2f} MB")

    
    tracemalloc.stop()