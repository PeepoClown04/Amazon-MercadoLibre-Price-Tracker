# Amazon/MercadoLibre Price Tracker ![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

Herramienta de automatización diseñada para monitorear fluctuaciones de precios en plataformas de comercio electrónico. Rastrea URLs específicas, extrae datos de precios en tiempo real y notifica al usuario cuando se detecta un descuento objetivo, eliminando la necesidad de verificación manual.

## Funcionalidades
- **Scraping Dinámico:** Extracción robusta de Título, Precio y Disponibilidad usando Selenium/BeautifulSoup.
- **Sistema de Alertas:** Notificación automática vía correo electrónico (SMTP) cuando el precio cae por debajo del umbral definido.
- **Histórico de Datos:** Registro de precios en CSV para análisis de tendencias.
- **Modo Headless:** Ejecución en segundo plano sin interfaz gráfica para servidores.

## Stack Tecnológico
- Python 3.x
- Selenium WebDriver
- Pandas (Data Management)
- SMTP Library (Notificaciones)

## Instalación y Uso
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Configurar URLs y precio objetivo en `config.py`.
4. Ejecutar: `python scraper.py`

## Estado del Proyecto
Funcional. Próximas mejoras: Integración con Telegram Bot API.
