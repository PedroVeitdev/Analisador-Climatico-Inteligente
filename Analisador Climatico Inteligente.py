import requests

def buscar_clima_por_nome():
    print("\n--- CONSULTA DE CLIMA ---")
    cidade = input("Digite o nome da cidade (ex: Fortaleza, São Paulo, Toronto): ").strip()
    
    if not cidade:
        print("Você precisa digitar o nome de uma cidade!")
        return

    # Descobrir as coordenadas (latitude e longitude) pelo nome da cidade
    url_geocodificacao = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt"
    
    try:
        resposta_geo = requests.get(url_geocodificacao, timeout=10)
        dados_geo = resposta_geo.json()
        
        # Verificar se a API encontrou a cidade
        if "results" not in dados_geo or len(dados_geo["results"]) == 0:
            print(f"❌ Não encontrei nenhuma cidade chamada '{cidade}'. Verifique a grafia.")
            return
            
        # Extrair os dados de localização da cidade encontrada
        infos_da_cidade = dados_geo["results"][0]
        nome_correto = infos_da_cidade["name"]
        estado = infos_da_cidade.get("admin1", "")  # Estado ou Região
        pais = infos_da_cidade.get("country", "")
        lat = infos_da_cidade["latitude"]
        lon = infos_da_cidade["longitude"]
        
        print(f"🌍 Cidade localizada: {nome_correto} ({estado} - {pais})")
        print("Obtendo o clima em tempo real...")

        # Buscar as informações climáticas reais usando as coordenadas
        url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        resposta_clima = requests.get(url_clima, timeout=10)
        dados_clima = resposta_clima.json()["current_weather"]
        
        temp = dados_clima["temperature"]
        vento = dados_clima["windspeed"]
        
        # Lógica da temperatura e resposta:
        if temp >= 30:
            conselho = "🥵 Muito quente! Evite exposição direta ao sol nos horários de pico e lembre-se de beber bastante água para não desidratar."
        elif temp >= 25:
            conselho = "🌤️ Temperatura agradável. O clima está ótimo para passear ou fazer atividades ao ar livre."
        elif temp >= 20:
            conselho = "🍃 A temperatura está ok, mas é bom levar um casaco leve por garantia se for voltar mais tarde."
        elif temp >= 15:
            conselho = "🥶 Frio! O uso de blusa é obrigatório para não passar aperto na rua."
        else:
            conselho = "❄️ Frio intenso... Agasalhe-se muito bem e prefira ficar em ambientes protegidos do vento."

        print("\n================ RESULTADO ================")
        print(f"Local: {nome_correto} ({estado} - {pais})")
        print(f"Temperatura Atual: {temp}°C")
        print(f"Velocidade do Vento: {vento} km/h")
        print(f"Recomendação do Sistema: {conselho}")
        print("===========================================")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão com o servidor: {e}")

def main():
    while True:
        print("\n1. Consultar Clima de uma Cidade")
        print("2. Sair")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            buscar_clima_por_nome()
        elif opcao == "2":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
