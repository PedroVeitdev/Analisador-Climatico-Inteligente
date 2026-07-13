import requests

def buscar_clima_por_nome():
    print("\n--- CONSULTA DE CLIMA ---")
    cidade = input("Digite o nome da cidade (ex: Fortaleza, São Paulo, Toronto): ").strip()
    
    if not cidade:
        print("Você precisa digitar o nome de uma cidade!")
        return

    # Descobre as coordenadas (latitude e longitude) pelo nome da cidade
    url_geocodificacao = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt"
