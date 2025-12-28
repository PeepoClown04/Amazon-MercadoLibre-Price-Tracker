import pandas as pd
import os
from src.scraper import MercadoLibreScraper
from src.notifier import send_email_alert

# CONFIGURACIÓN DE RASTREO
# Formato: "URL": Precio_Maximo_a_Pagar
TRACKING_LIST = {
    "https://www.mercadolibre.cl/apple-iphone-15-128-gb-negro-distribuidor-autorizado/p/MLC1027172677": 800000, # Si baja de 800k, avísame
    "https://www.mercadolibre.cl/consola-ps5-slim-digital-juego-astro-bot-y-gran-turismo-7-blanconegro-sony/p/MLC51702073": 600000  # Si baja de 600k, avísame
}

def main():
    bot = MercadoLibreScraper(headless=True) # Modo silencioso activado
    products_data = []

    try:
        for url, target_price in TRACKING_LIST.items():
            data = bot.get_product_data(url)
            
            if data:
                print(f"📊 {data['titulo'][:40]}... | Actual: ${data['precio']:,.0f} | Objetivo: ${target_price:,.0f}")
                
                # LÓGICA DE ALERTA
                if data['precio'] > 0 and data['precio'] <= target_price:
                    print("   🔥 ¡PRECIO OBJETIVO ALCANZADO!")
                    send_email_alert(data['titulo'], data['precio'], data['url'])
                else:
                    print("   zzz... Aún muy caro.")

                products_data.append(data)
            else:
                print("❌ Fallo en la extracción.")
        
    finally:
        bot.close_driver()

    # Guardar CSV (Igual que antes)
    if products_data:
        df = pd.DataFrame(products_data)
        os.makedirs("output", exist_ok=True)
        csv_path = "output/precios_historicos.csv"
        file_exists = os.path.isfile(csv_path)
        df.to_csv(csv_path, mode='a', header=not file_exists, index=False)
        print(f"\n📁 Histórico actualizado en: {csv_path}")

if __name__ == "__main__":
    main()