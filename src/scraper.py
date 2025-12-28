import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

class MercadoLibreScraper:
    def __init__(self, headless=False):
        self.options = Options()
        
        # --- RUTA DE CHROME (Si ya te funciona, no toques esto) ---
        # ---------------------------

        if headless:
            self.options.add_argument("--headless")
        
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--log-level=3")
        self.options.add_argument("--disable-notifications") # Bloquea notificaciones nativas
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        self.driver = None

    def start_driver(self):
        print("🔧 Iniciando navegador...")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            print("🔌 Navegador cerrado.")

    def get_product_data(self, url):
        if not self.driver:
            self.start_driver()

        print(f"🔍 Analizando: {url}...")
        try:
            self.driver.get(url)
            
            url_actual = self.driver.current_url
            if url_actual != url:
                print(f"   ⚠️ ALERTA: Redirección detectada a -> {url_actual}")
            # 1. INTENTO DE CERRAR POP-UPS (Ubicación / Cookies)
            try:
                # Espera breve para ver si sale el popup de ubicación y cerrarlo
                wait = WebDriverWait(self.driver, 3) 
                close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'cookie') or contains(text(), 'Más tarde') or contains(text(), 'Entendido')]")))
                close_btn.click()
                print("   🛡️ Pop-up cerrado.")
            except:
                pass # Si no hay popup, seguimos.

            # 2. EXTRACCIÓN DEL TÍTULO (SÓLO CABECERA)
            # Usamos WebDriverWait para asegurar que el título PRINCIPAL cargó
            try:
                wait = WebDriverWait(self.driver, 5)
                # Buscamos h1 que tenga la clase específica, ignorando carruseles
                title_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.ui-pdp-title")))
                title = title_element.text
            except:
                print("   ⚠️ Título principal no detectado. Posible redirección o producto inexistente.")
                title = "ERROR: Producto no encontrado"

            # 3. EXTRACCIÓN DEL PRECIO
            price = 0.0
            try:
                # Meta tag es lo más seguro
                price_element = self.driver.find_element(By.CSS_SELECTOR, "meta[itemprop='price']")
                price = float(price_element.get_attribute("content"))
            except:
                pass # Si falla, se queda en 0.0

            # 4. DISPONIBILIDAD
            # Si el título es error, asumimos no disponible
            is_available = "Sí"
            if "ERROR" in title or "pausada" in self.driver.page_source:
                is_available = "No"

            return {
                "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
                "titulo": title,
                "precio": price,
                "disponible": is_available,
                "url": url
            }

        except Exception as e:
            print(f"❌ Error crítico: {e}")
            return None